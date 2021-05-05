# -*- coding: utf-8 -*-
###############################################################
##                                                           ##
##   Author : Zviez                                          ##
##   Description : Project for OC TP6                        ##
##   Year : 2021                                             ##
##                                                           ##
##                                                           ##
###############################################################

from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Plotter import CustomWidget, sniffer
from functools import partial
from pexpect import pxssh
from threading import *
from scapy.all import *
from pypxe import http, dhcp
from time import sleep

import numpy as np
import os

class Application:
    '''
	Main Application Class
	'''

    def __init__(self):

        self.interface = ""

        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()

        self.procHost = None
        self.procSniffer = None
        self.procSSH = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        
        ##############################################################
        ### Command for Kernel Hardening

        self.cmd = '''echo `cat << EOF
			kernel.kptr_restrict=2\\n
			kernel.dmesg_restrict=1\\n
			kernel.printk=3 3 3 3\\n
			kernel.unprivileged_bpf_disabled=1\\n
			dev.tty.ldisc_autoload=0\\n
			net.core.bpf_jit_harden=2\\n
			vm.unprivileged_userfaultfd=0\\n
			kernel.kexec_load_disabled=1\\n
			kernel.sysrq=4\\n
			kernel.unprivileged_userns_clone=0\\n
			kernel.perf_event_paranoid=3\\n
			net.ipv4.tcp_syncookies=1\\n
			net.ipv4.tcp_rfc1337=1\\n
			net.ipv4.conf.all.rp_filter=1\\n
			net.ipv4.conf.default.rp_filter=1\\n
			net.ipv4.conf.all.accept_redirects=0\\n
			net.ipv4.conf.default.accept_redirects=0\\n
			net.ipv4.conf.all.secure_redirects=0\\n
			net.ipv4.conf.default.secure_redirects=0\\n
			net.ipv6.conf.all.accept_redirects=0\\n
			net.ipv6.conf.default.accept_redirects=0\\n
			net.ipv4.conf.all.send_redirects=0\\n
			net.ipv4.conf.default.send_redirects=0\\n
			net.ipv4.icmp_echo_ignore_all=1\\n
			net.ipv4.conf.all.accept_source_route=0\\n
			net.ipv4.conf.default.accept_source_route=0\\n
			net.ipv6.conf.all.accept_source_route=0\\n
			net.ipv6.conf.default.accept_source_route=0\\n
			net.ipv6.conf.all.accept_ra=0\\n
			net.ipv6.conf.default.accept_ra=0\\n
			net.ipv4.tcp_sack=0\\n
			net.ipv4.tcp_dsack=0\\n
			net.ipv4.tcp_fack=0\\n
			kernel.yama.ptrace_scope=2\\n
			vm.mmap_rnd_bits=32\\n
			vm.mmap_rnd_compat_bits=16\\n
			fs.protected_symlinks=1\\n
			fs.protected_hardlinks=1\\n
			fs.protected_fifos=2\\n
			fs.protected_regular=2\\n
			` >> /etc/sysctl.conf'''

        ###########################################################################################"
        # listing interfaces depending on os and populating interface combo box

        if platform == "linux" or platform == "linux2":

            self.ui.comboInterfaces.addItems(get_if_list())
            self.ui.comboHardenInterface.addItems(get_if_list())
            self.ui.comboIfaceAdminOp.addItems(get_if_list())

        elif platform == "win32":
            for i in ifaces.data:

                self.ui.comboInterfaces.addItem(ifaces.data[i].name)
                self.ui.comboHardenInterface.addItems(ifaces.data[i].name)
                self.ui.comboIfaceAdminOp.addItems(ifaces.data[i].name)

        self.test = CustomWidget(parent=self.ui.tab_2)

        self.launched = False

        self.ip = None
        self.selectIP = None

        ##############################################################################
        ### Linking Button to their functions

        self.ui.sniffStartButton.clicked.connect(self.clickedSniffing)
        self.ui.sniffStopButton.clicked.connect(self.stopper)

        self.ui.buttonPingHost.clicked.connect(self.lala)

        self.ui.buttonGetHostDiag.clicked.connect(self.getHostRange)
        self.ui.buttonGetHostAdmOp.clicked.connect(self.getHostRange)
        self.ui.buttonGetHostsHard.clicked.connect(self.getHostRange)

        ###############################################################################

        self.ui.buttonInstall.clicked.connect(partial(self.packageInstall, "apt install -y"))
        self.ui.buttonRemove.clicked.connect(partial(self.packageInstall, "apt remove -y"))
        self.ui.buttonUpdate.clicked.connect(partial(self.packageInstall, "apt update"))
        self.ui.buttonUpgrade.clicked.connect(partial(self.packageInstall, "apt upgrade -y"))


        self.ui.buttonNetInterface.clicked.connect(self.NetInterfaceClicked)
        self.ui.buttonExtractDmesg.clicked.connect(self.dmesgExtractClick)

        self.ui.buttonHarden.clicked.connect(partial(self.packageInstall, self.cmd))

        ###############################################################################
        # Linking tool buttons

        self.ui.toolPathDiag.clicked.connect(self.logsPathSave)
        self.ui.isoOsInstallTool.clicked.connect(self.isoFilePXE)

        self.ui.comboHostsDiag.currentIndexChanged.connect(self.selectDiagIp)
        self.ui.comboHostsAdminOp.currentIndexChanged.connect(self.selectAdminOpIP)
        self.ui.comboHostsHard.currentIndexChanged.connect(self.selectHardIP)

        ###############################################################################
        # Linking ComboBoxes behaviour to functions
        self.ui.comboInterfaces.currentIndexChanged.connect(self.selectDiagIface)
        self.ui.comboHardenInterface.currentIndexChanged.connect(self.selectHardenIface)
        self.ui.comboIfaceAdminOp.currentIndexChanged.connect(self.selectAdminOpIface)

        self.ui.comboHostsAdminOp.addItem("Ip")
        self.ui.comboHostsAdminOp.addItem("127.0.0.1")
        self.ui.comboHostsHard.addItem("Ip")
        self.ui.comboHostsHard.addItem("127.0.0.1")
        self.ui.comboHostsDiag.addItem("Ip")
        self.ui.comboHostsDiag.addItem("127.0.0.1")


        MainWindow.show()

        sys.exit(app.exec_())

    ###############################################################################
    
    def getHostRange(self):
        '''
        Pops a messageBox asking for the start IP
        Scanning x.x.x.x/24
        '''

        ip , pressed = QtGui.QInputDialog.getText(None, "Input Text", "Please enter IP ending by 0 ",
                                           QtWidgets.QLineEdit.Normal, "")

        if ip != "":
          self.ip = ip
          self.clickedGetHost()
          

    def sshCreds(self):
        '''
        Storing ssh credentials
        '''

        user , pressed = QtGui.QInputDialog.getText(None, "Input Text", "Username ",
                                           QtWidgets.QLineEdit.Normal, "")
        if user != '':
          password , pressed = QtGui.QInputDialog.getText(None, "Input Text", "Password", QtWidgets.QLineEdit.Normal, "")

          if password != "":

             return user, password

    def packageInstall(self, command):

        user, password = self.sshCreds()

        if "apt" in command:

         if self.ui.linePackages.text() == '':

             self.ui.consoleOutput.addItem("[+] Please enter packages")

         else:

             packages = self.ui.linePackages.text()

             command = "echo -n %s |sudo -S %s %s" % (password, command, packages)

        elif "dmesg" in command or "ip" in command:

             print ("[+] ok")
             p = netcat()
             p.start()

             sleep(0.5)
             command = "echo -n %s |sudo -S %s" % (password, command)


        if self.selectIP == "Ip" or self.selectIP == None:
            return

        if self.procSSH is None:

            self.procSSH = ssh(self.selectIP, command, user, password)
            self.procSSH.start()

        elif self.procSSH is not None and self.procSSH.running == False:

            self.procSSH.join()
            self.procSSH = ssh(self.selectIP, command, user, password)
            self.procSSH.start()

        else:

            self.ui.consoleOutput.addItem("[+] Process already running")


    def NetInterfaceClicked(self):

        self.packageInstall("ip a | tee /tmp/ipInfo.log && echo 'EOF' | tee -a /tmp/ipInfo.log && nc -w1 " + get_if_addr("eth0") + " 4444 < /tmp/ipInfo.log")

    def dmesgExtractClick(self):

        self.packageInstall("dmesg | tee /tmp/dmesg.log && echo 'EOF' | tee -a /tmp/dmesg.log && nc -w1 " + get_if_addr("eth0") + " 4444 < /tmp/dmesg.log")

    def selectAdminOpIP(self):

        self.selectIP = (self.ui.comboHostsAdminOp.currentText())

    ####################################################################
    # Network iface selections
    def selectHardenIface(self):

        self.interface = (self.ui.comboHardenInterface.currentText())

    def selectDiagIface(self):

        self.interface = (self.ui.comboInterfaces.currentText())

    def selectAdminOpIface(self):

        self.interface = (self.ui.comboIfaceAdminOp.currentText())


    ####################################################################
    def selectHardIP(self):

        self.selectIP = (self.ui.comboHostsHard.currentText())

    def selectDiagIp(self):
        '''
		Selecting an element within combo box and puting it in out Line
        '''

        self.selectIP = self.ui.comboHostsDiag.currentText()

    def logsPathSave(self):
        '''
		Popping a dialog to select a directory
		Store the directory and print it in line
        '''

        dialog = QtGui.QFileDialog()
        fname = dialog.getExistingDirectory(None, "Select Folder")

        print('fname : ', fname)
        if fname != '':
           self.ui.linePathDiag.setText(fname)

    def isoFilePXE(self):

        #dialog = QtGui.QFileDialog()
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', '.',"Iso file (*.iso)")
        print('fname : ', fname)

        if fname[0] != '':
           self.ui.isoOsInstallLine.setText(fname[0])

    def clickedGetHost(self):
        '''
		Function check if we didn't already launched a sweep scan
		'''
        if self.procHost is not None and self.procHost.status is None:

            self.procHost.join()

            print("[+]Process ended")
            self.procHost = None
            self.getHost()

        elif self.procHost is None:

            self.getHost()

        else:

            self.ui.consoleOutput.addItem("[+] Sweep Scanning still in progress")

    def getHost(self):
        '''
        Launching the Sweep Scan to get Activ Hosts in the network
	'''

        ip = self.ip

        # Checking if we haven' already launch a scan
        if self.procHost is None:
            self.procHost = Scanner(ip, self.ui, self.interface)
            self.ui.consoleOutput.addItem("[+] Sweep Scanning Network")
            self.procHost.start()

            print("[+] " + self.procHost.status)

    def lala(self):

        p = pinger(self.ui, self.interface)
        p.start()

    def stopper(self):
        '''
        Stopping the Sniffer
        '''

        self.procSniffer.status = False
        self.procSniffer.StopMonitor()
        self.procSniffer.join()

        if self.procSniffer.is_alive() == False:
            print("[+] ok")

    def clickedSniffing(self):
        '''
	Function checking if we didn't already have a thread running to avoid conflict
        '''

        if self.procSniffer is None:

            print("[+] Sniffing")
            self.sniffing()

        elif self.procSniffer is not None and self.procSniffer.status == False:
            print("[+] Sniffing")
            self.sniffing()
        else:

            self.ui.consoleOutput.addItem("[+] Sniffer still in progress")

    def sniffing(self):
        '''
	Function launching sniffer
        '''	

        # storing ip from within line
        ip , pressed = QtGui.QInputDialog.getText(None, "Input Text", "Please enter IP",
                                           QtWidgets.QLineEdit.Normal, "")

        if ip == "":

            print("[+] error while trying Monitor, please specify ip\n")
            self.ui.consoleOutput.addItem("[+] error while trying Monitor, please specify ip")

        else:

            self.test.data1 = np.zeros(10)
            self.test.curve1 = self.test.p1.plot(self.test.data1)
            self.test.ptr1 = 0

            self.procSniffer = sniffer(ip, self.test.data1, self.test.curve1, self.test.ptr1, self.test.p1,
                                       self.interface)
            self.procSniffer.start()


class Scanner(Thread):
    '''
    Scanning network for hosts using ICMP packets
    '''
    def __init__(self, ip, ui, interface):

        Thread.__init__(self)

        self.threadlock = Lock()
        self.ip = ip.split('.')
        self.ui = ui
        self.status = None
        self.interface = interface

    def run(self):

        self.status = "running"
        checked = False

        for i in range(1, 255):

            self.ip[3] = str(i)
            fullIp = self.ip[0] + '.' + self.ip[1] + '.' + self.ip[2] + '.' + self.ip[3]

            # Sending ICMP packet and storing answsers
            ans, unans = sr(IP(dst=fullIp) / ICMP(), iface=self.interface, timeout=0.01, verbose=0)

            if ans is not None:
                for elem in ans:
                    # Checking if we got a reply and verifying if we didnt already checked this ip
                    if elem[1].type == 0:
                        for i in range(self.ui.comboHostsDiag.count()):
                            if self.ui.comboHostsDiag.itemText(i) == elem[1].src:
                                checked = True
                                break

                        # Storing ips in combo boxes
                        if checked == False:

                            self.ui.consoleOutput.addItem("[+] Hosts Found : %s" % elem[1].src)
                            self.ui.comboHostsDiag.addItem(elem[1].src)
                            self.ui.comboHostsAdminOp.addItem(elem[1].src)
                            self.ui.comboHostsHard.addItem(elem[1].src)

                        else:
                            checked = False

        self.ui.consoleOutput.addItem("[+] Sweep Scan complete")
        self.status = None

class netcat(Thread):

    def __init__(self):

         Thread.__init__(self)
         self.so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         self.filename = "tester.log"
         self.go = True
 
    def run(self):

         print("[+] Starting Server")

         self.so.bind(('0.0.0.0', 4444))
         self.so.listen()
         fil = open(self.filename, 'wb')

         while self.go:

              cli_sock, cli_adr = self.so.accept()

              data = cli_sock.recv(10)

              print ("[+] " + str(data))

              while data:
                  if b'EOF' in data:

                     print ("[+] Closing listener")
                     self.go = False
                     fil.close()
                     cli_sock.close()
                     self.so.close()
               
                     break
           
                  data = cli_sock.recv(1024)
                  fil.write(data)
                  print ("[+] " + str(data))
                 
class pinger(Thread):
    '''
    Sending an ICMP packet
    '''

    def __init__(self, ui, interface):

        Thread.__init__(self)

        self.threadlock = Lock()
        self.rez = None
        self.ui = ui
        self.interface = interface

    def run(self):

        self.threadlock.acquire()
        ip = self.ui.lineIpDiagPing.text()

        if ip == "":

            print("[+] error while trying Monitor, please specify ip\n")
            self.ui.consoleOutput.addItem("[+] error while trying Monitor, please specify ip")

        else:

            rep = sr(IP(dst=ip) / ICMP(), timeout=2, iface=self.interface, verbose=0)
            self.rez = "Testing %s" % rep[0]
            self.ui.consoleOutput.addItem(self.rez)

        self.threadlock.release()


class ssh(Thread):
    '''
    SSH Worker
    '''

    def __init__(self, ip, command, user, passwd):

        Thread.__init__(self)

        self.cmd = command
        self.user = user
        self.passwd = passwd
        self.host = ip
        self.running = False

    def run(self):

        self.running = True

        # file to store ssh logs
        tmpFl = '/tmp/dminOp.log'
        fp = open(tmpFl, 'wb')

        cmd = self.cmd
        user2 = self.user
        pwd = self.passwd
        host2 = self.host

        try:

            s = pxssh.pxssh()

            hostname = host2
            username = user2
            password = pwd

            # sending creds to login
            s.login(hostname, user2, pwd)

            # sending command
            s.sendline(cmd)
            s.prompt()

            s.logout()

        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)

        self.running = False


class pxeServer(Thread):

    def __init__(self, ui):

      http.ip = '0.0.0.0'
      http.port = 88
      http.netboot_directory	
	

    def run(self):
      pass

if __name__ == "__main__":
    launcher = Application()
