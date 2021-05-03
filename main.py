# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 575)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 331, 501))
        self.groupBox.setObjectName("groupBox")

        self.MenuTabs = QtWidgets.QTabWidget(self.groupBox)
        self.MenuTabs.setGeometry(QtCore.QRect(0, 20, 331, 481))
        self.MenuTabs.setObjectName("MenuTabs")

        self.tabOsInstall = QtWidgets.QWidget()
        self.tabOsInstall.setObjectName("tabOsInstall")

        self.CheckDhcpServer = QtWidgets.QCheckBox(self.tabOsInstall)
        self.CheckDhcpServer.setGeometry(QtCore.QRect(10, 10, 151, 25))
        self.CheckDhcpServer.setObjectName("CheckDhcpServer")
        self.CheckHttpServer = QtWidgets.QCheckBox(self.tabOsInstall)
        self.CheckHttpServer.setGeometry(QtCore.QRect(10, 40, 91, 25))
        self.CheckHttpServer.setObjectName("CheckHttpServer")
        self.CheckTftpServer = QtWidgets.QCheckBox(self.tabOsInstall)
        self.CheckTftpServer.setGeometry(QtCore.QRect(10, 70, 91, 25))
        self.CheckTftpServer.setObjectName("CheckTftpServer")

        self.isoOsInstallLine = QtWidgets.QLineEdit(self.tabOsInstall)
        self.isoOsInstallLine.setGeometry(QtCore.QRect(10, 120, 231, 27))
        self.isoOsInstallLine.setObjectName("isoOsInstallLine")

        self.isoOsInstallTool = QtWidgets.QToolButton(self.tabOsInstall)
        self.isoOsInstallTool.setGeometry(QtCore.QRect(240, 120, 27, 26))
        self.isoOsInstallTool.setObjectName("isoOsInstallTool")

        self.label = QtWidgets.QLabel(self.tabOsInstall)
        self.label.setGeometry(QtCore.QRect(10, 100, 231, 19))
        self.label.setObjectName("label")

        self.buttonPxeLaunch = QtWidgets.QPushButton(self.tabOsInstall)
        self.buttonPxeLaunch.setGeometry(QtCore.QRect(10, 160, 151, 27))
        self.buttonPxeLaunch.setObjectName("buttonPxeLaunch")

        self.MenuTabs.addTab(self.tabOsInstall, "")

        self.tabHardening = QtWidgets.QWidget()
        self.tabHardening.setObjectName("tabHardening")

        self.comboHostsHard = QtWidgets.QComboBox(self.tabHardening)
        self.comboHostsHard.setGeometry(QtCore.QRect(10, 20, 181, 27))
        self.comboHostsHard.setObjectName("comboHostsHard")

        self.buttonGetHostsHard = QtWidgets.QPushButton(self.tabHardening)
        self.buttonGetHostsHard.setGeometry(QtCore.QRect(200, 20, 88, 27))
        self.buttonGetHostsHard.setObjectName("buttonGetHostsHard")

        self.buttonHarden = QtWidgets.QPushButton(self.tabHardening)
        self.buttonHarden.setGeometry(QtCore.QRect(80, 70, 88, 27))
        self.buttonHarden.setObjectName("buttonHarden")

        self.checkAllHostsHard = QtWidgets.QCheckBox(self.tabHardening)
        self.checkAllHostsHard.setGeometry(QtCore.QRect(10, 90, 91, 25))
        self.checkAllHostsHard.setObjectName("checkAllHostsHard")

        self.comboHardenInterface = QtWidgets.QComboBox(self.tabHardening)
        self.comboHardenInterface.setGeometry(QtCore.QRect(10, 120, 160, 25))
        self.comboHardenInterface.setObjectName("comboHardenInterface")

        self.MenuTabs.addTab(self.tabHardening, "")
        self.tabDiag = QtWidgets.QWidget()
        self.tabDiag.setObjectName("tabDiag")

        self.lineIpDiagPing = QtWidgets.QLineEdit(self.tabDiag)
        self.lineIpDiagPing.setGeometry(QtCore.QRect(10, 30, 191, 27))
        self.lineIpDiagPing.setObjectName("lineIpDiagPing")

        self.buttonPingHost = QtWidgets.QPushButton(self.tabDiag)
        self.buttonPingHost.setGeometry(QtCore.QRect(210, 30, 88, 27))
        self.buttonPingHost.setObjectName("buttonPingHost")

        self.label_2 = QtWidgets.QLabel(self.tabDiag)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 66, 19))
        self.label_2.setObjectName("label_2")

        self.comboHostsDiag = QtWidgets.QComboBox(self.tabDiag)
        self.comboHostsDiag.setGeometry(QtCore.QRect(10, 60, 191, 27))
        self.comboHostsDiag.setObjectName("comboHostsDiag")

        self.buttonGetHostDiag = QtWidgets.QPushButton(self.tabDiag)
        self.buttonGetHostDiag.setGeometry(QtCore.QRect(210, 60, 88, 27))
        self.buttonGetHostDiag.setObjectName("buttonGetHostDiag")
        self.buttonExtractDmesg = QtWidgets.QPushButton(self.tabDiag)
        self.buttonExtractDmesg.setGeometry(QtCore.QRect(10, 140, 121, 27))
        self.buttonExtractDmesg.setObjectName("buttonExtractDmesg")

        self.toolPathDiag = QtWidgets.QToolButton(self.tabDiag)
        self.toolPathDiag.setGeometry(QtCore.QRect(210, 110, 27, 26))
        self.toolPathDiag.setObjectName("toolPathDiag")

        self.linePathDiag = QtWidgets.QLineEdit(self.tabDiag)
        self.linePathDiag.setGeometry(QtCore.QRect(10, 110, 191, 27))
        self.linePathDiag.setObjectName("linePathDiag")

        self.label_4 = QtWidgets.QLabel(self.tabDiag)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 131, 19))
        self.label_4.setObjectName("label_4")

        self.buttonNetInterface = QtWidgets.QPushButton(self.tabDiag)
        self.buttonNetInterface.setGeometry(QtCore.QRect(140, 140, 131, 27))
        self.buttonNetInterface.setObjectName("buttonNetInterface")

        self.buttonHardware = QtWidgets.QPushButton(self.tabDiag)
        self.buttonHardware.setGeometry(QtCore.QRect(10, 170, 88, 27))
        self.buttonHardware.setObjectName("buttonHardware")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tabDiag)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 291, 91))
        self.groupBox_2.setObjectName("groupBox_2")

        self.lineIpDiagPingFrom = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineIpDiagPingFrom.setGeometry(QtCore.QRect(10, 50, 151, 27))
        self.lineIpDiagPingFrom.setObjectName("lineIpDiagPingFrom")

        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 66, 19))
        self.label_5.setObjectName("label_5")

        self.buttonPingFrom = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonPingFrom.setGeometry(QtCore.QRect(180, 50, 88, 27))
        self.buttonPingFrom.setObjectName("buttonPingFrom")

        self.sniffStartButton = QtWidgets.QPushButton(self.tabDiag)
        self.sniffStartButton.setGeometry(QtCore.QRect(100, 310, 88, 27))
        self.sniffStartButton.setObjectName("pushButton")

        self.sniffStopButton = QtWidgets.QPushButton(self.tabDiag)
        self.sniffStopButton.setGeometry(QtCore.QRect(20, 310, 88, 27))
        self.sniffStopButton.setObjectName("sniffStopButton")

        self.comboInterfaces = QtWidgets.QComboBox(self.tabDiag)
        self.comboInterfaces.setGeometry(QtCore.QRect(20, 340, 180, 27))
        self.comboInterfaces.setObjectName("comboInterfaces")

        self.MenuTabs.addTab(self.tabDiag, "")

        self.tabAdminOp = QtWidgets.QWidget()
        self.tabAdminOp.setObjectName("tabAdminOp")

        self.buttonInstall = QtWidgets.QPushButton(self.tabAdminOp)
        self.buttonInstall.setGeometry(QtCore.QRect(100, 150, 88, 27))
        self.buttonInstall.setObjectName("buttonInstall")

        self.linePackages = QtWidgets.QLineEdit(self.tabAdminOp)
        self.linePackages.setGeometry(QtCore.QRect(10, 120, 211, 27))
        self.linePackages.setObjectName("linePackages")

        self.label_3 = QtWidgets.QLabel(self.tabAdminOp)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 19))
        self.label_3.setObjectName("label_3")

        self.comboHostsAdminOp = QtWidgets.QComboBox(self.tabAdminOp)
        self.comboHostsAdminOp.setGeometry(QtCore.QRect(10, 30, 211, 27))
        self.comboHostsAdminOp.setObjectName("comboHostsAdminOp")

        self.comboIfaceAdminOp = QtWidgets.QComboBox(self.tabAdminOp)
        self.comboIfaceAdminOp.setGeometry(QtCore.QRect(10, 210, 190, 27))
        self.comboIfaceAdminOp.setObjectName("comboIfaceAdminOp")

        self.buttonGetHostAdmOp = QtWidgets.QPushButton(self.tabAdminOp)
        self.buttonGetHostAdmOp.setGeometry(QtCore.QRect(230, 30, 88, 27))
        self.buttonGetHostAdmOp.setObjectName("buttonGetHostAdmOp")

        self.checkAllHostsAdminOp = QtWidgets.QCheckBox(self.tabAdminOp)
        self.checkAllHostsAdminOp.setGeometry(QtCore.QRect(10, 60, 91, 25))
        self.checkAllHostsAdminOp.setObjectName("checkAllHostsAdminOp")

        self.buttonUpdate = QtWidgets.QPushButton(self.tabAdminOp)
        self.buttonUpdate.setGeometry(QtCore.QRect(10, 180, 88, 27))
        self.buttonUpdate.setObjectName("buttonUpdate")

        self.buttonUpgrade = QtWidgets.QPushButton(self.tabAdminOp)
        self.buttonUpgrade.setGeometry(QtCore.QRect(100, 180, 88, 27))
        self.buttonUpgrade.setObjectName("buttonUpgrade")

        self.buttonRemove = QtWidgets.QPushButton(self.tabAdminOp)
        self.buttonRemove.setGeometry(QtCore.QRect(10, 150, 88, 27))
        self.buttonRemove.setObjectName("buttonRemove")

        self.MenuTabs.addTab(self.tabAdminOp, "")

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(330, 20, 731, 481))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.consoleOutput = QtWidgets.QListWidget(self.tab)
        self.consoleOutput.setGeometry(QtCore.QRect(0, 0, 721, 441))
        self.consoleOutput.setObjectName("consoleOutput")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tabWidget.addTab(self.tab_2, "")

        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1070, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")

        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuExit.addAction(self.actionAbout)
        self.menuExit.addAction(self.actionExit)
        self.menuBar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        self.MenuTabs.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "SysAdmin Swiss Army knife"))

        self.groupBox.setTitle(_translate("MainWindow", "Main"))

        self.CheckDhcpServer.setText(_translate("MainWindow", "Set As DHCP server"))
        self.CheckHttpServer.setText(_translate("MainWindow", "Use HTTP"))
        self.CheckTftpServer.setText(_translate("MainWindow", "Use TFTP"))

        self.isoOsInstallTool.setText(_translate("MainWindow", "..."))

        self.label.setText(_translate("MainWindow", "OS Iso file for NetInstall"))

        self.buttonPxeLaunch.setText(_translate("MainWindow", "Launch PXE server"))

        self.MenuTabs.setTabText(self.MenuTabs.indexOf(self.tabOsInstall), _translate("MainWindow", "OS Install"))

        self.buttonGetHostsHard.setText(_translate("MainWindow", "Get Hosts"))
        self.buttonHarden.setText(_translate("MainWindow", "Harden"))

        self.checkAllHostsHard.setText(_translate("MainWindow", "All Hosts"))

        self.MenuTabs.setTabText(self.MenuTabs.indexOf(self.tabHardening), _translate("MainWindow", "Hardening"))

        self.buttonPingHost.setText(_translate("MainWindow", "Ping"))

        self.label_2.setText(_translate("MainWindow", "IP(s)"))

        self.buttonGetHostDiag.setText(_translate("MainWindow", "Get Hosts"))
        self.buttonExtractDmesg.setText(_translate("MainWindow", "Extract DMESG"))

        self.toolPathDiag.setText(_translate("MainWindow", "..."))

        self.label_4.setText(_translate("MainWindow", "Path To Save Files"))

        self.buttonNetInterface.setText(_translate("MainWindow", "Network Interfaces"))
        self.buttonHardware.setText(_translate("MainWindow", "Hardware"))

        self.groupBox_2.setTitle(_translate("MainWindow", "Ping From Selected host To"))

        self.label_5.setText(_translate("MainWindow", "Ip(s)"))

        self.buttonPingFrom.setText(_translate("MainWindow", "Ping"))

        self.sniffStartButton.setText(_translate("MainWindow", "Start Sniff"))
        self.sniffStopButton.setText(_translate("MainWindow", "Stop Sniff"))

        self.MenuTabs.setTabText(self.MenuTabs.indexOf(self.tabDiag), _translate("MainWindow", "Diag"))

        self.buttonInstall.setText(_translate("MainWindow", "Install"))

        self.label_3.setText(_translate("MainWindow", "Package Lists"))

        self.buttonGetHostAdmOp.setText(_translate("MainWindow", "Get Host"))

        self.checkAllHostsAdminOp.setText(_translate("MainWindow", "All Hosts"))

        self.buttonUpdate.setText(_translate("MainWindow", "Update"))
        self.buttonUpgrade.setText(_translate("MainWindow", "Upgrade"))
        self.buttonRemove.setText(_translate("MainWindow", "Remove"))

        self.MenuTabs.setTabText(self.MenuTabs.indexOf(self.tabAdminOp), _translate("MainWindow", "Admin Op"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Console OutPut"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Graph Monitoring"))

        self.menuExit.setTitle(_translate("MainWindow", "Menu"))

        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))