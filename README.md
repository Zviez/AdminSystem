# AdminSystem

<H2> Context </H2>

This tool is aimed to help Sys Admin to administrate remotely Computers. It works mainly on Linux and partially on Windows as functionnalities using SSH are not yet implemented for Win32.

<H2> Functionnalities </H2>

The gui is divided between 3 tabs:

<h4> os Install </h4>

  Using <b>PyPXE</b> library this part will help you create a PXE server for remote OS installation. It can also act as a DHCP server in the case you don't have a DHCP server yet. You have the possibility to use HTPP, TFTP protocol for remote install. Chose an iso file and once you have selected a protocol or wether or not you need DHCP, click <b>launch pxe server</b>
  
<h4> Harden </h4>

This tab is used for kernel hardening. 
You need first to select a network interface in the combobox, then sweepscan the network for Host Discovery using <b> Get Hosts</b>. Once it's done, select an host or "All Hosts" to harden the box.
It uses SSH protocol to send commands, so be sure the hosts is running an ssh server.

<h4> Diag </h4>

This tab is for diagnosis.
In the case a technical problem happened, thos commands will helps you troubleshoot.
First select an interface in combo box down.
Then you can :

<ul>
  <li> Ping </li>
  Simply input an ip and select ping to send an ICMP packet to the host
  
  <li> Get Host </li>
  Sweep scan the network using ICMP packets
  
  <li> DMESG, NetworkInterface, Hardware buttons </li>
  Will run, through SSH, a bunch of commands to generates logs and transfer it to your computer for analysis.
  You cna select a path where you cant to save your files
  
  <li> Sniff </li>
  Sniff command will help you monitor packets exchange with the host. The graph in the monitor tab on the right will show you activity
  
  <li> Ping From Host </li>
  This command will make the host you chose ping an other host
  
</ul>

<h4> Admin Op</h4>

This tab is used for classic Administration operation such as package managements. Other options will be added later

<ul>
  <li>Get Hosts</li>
  
  Sweep scan the network for hosts and add them in the combo list for selection
  
  <li> Install, remove buttons</li>
 
  Put a list of packages you wish to install or remove in the edit line and hit the button of your choice. It will send the command through ssh and output the result inthe "output console"
  
  <li> Update/Upgrade</li>
  
  For Os updates and upgrade on linux. Use SSH to send the command
</ul>

<H2> Launching Scripts </H2>
<H3> Requirements </H3>

To run this script require the following libraries :

<ul>
<li>numpy~=1.20.2</li>
<li>PyQt5~=5.15.4</li>
<li>pexpect~=4.8.0</li>
<li>scapy~=2.4.5</li>
<li>pyqtgraph~=0.12.1</li>
<li>PyPXE~=1.8.2</li>
</ul>

you can simply use the requirements file :

  <b>pip3 install -r requirements.txt </b>

<H3> Launching </H3>

Use sudo privileges commands as i didnt implement elevation script yet. Using interfaces with scapy requires elevation
Launch using the command with <b>sudo python3 main.py</b> in SysAdmin directory

Todo :

Implement Try and catch to deal with errors
Implement console output within GUI
Finish PXE server

