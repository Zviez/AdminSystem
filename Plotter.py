import pyqtgraph as pg
import numpy as np

from pyqtgraph.Qt import QtCore, QtGui
from scapy.all import *
from threading import *


class CustomWidget(pg.GraphicsWindow):
    '''
    Plotter widget to monitor Traffic on a given IP
    '''

    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    ptr1 = 0

    def __init__(self, parent=None, **kargs):

        pg.GraphicsWindow.__init__(self, **kargs)

        self.setParent(parent)
        self.setWindowTitle('Traffic Monitoring')
        self.setGeometry(QtCore.QRect(10, 10, 711, 431))

        self.p1 = self.addPlot(labels={'left': 'packets', 'bottom': 'Time'})

        self.p1.setYRange(0, 1000, padding=0)
        self.p1.setXRange(0, 20, padding=0)

        self.data1 = None
        self.curve1 = None


class sniffer(Thread):
    '''
    Thread Worker to monitor
    '''

    def __init__(self, ip, data, curve, ptr, p1, interface):

        Thread.__init__(self)

        self.ip = ip
        self.interface = interface

        self.packets = []

        self.p1 = p1
        self.data1 = data
        self.curve1 = curve
        self.ptr1 = ptr

        self.status = False

    def run(self):

        self.status = True

        while True:
            self.update()

            if self.status:
                pass
            else:
                print("[+] Stop Loop")
                break

    def update(self):
        ''' Updating Plot with packets sniffed on interface'''

        # Forging Filter
        sniffFilter = "host " + self.ip

        # Sniffing Traffic
        self.packets = sniff(filter=sniffFilter, timeout=0.5, iface=self.interface)

        # Updating datas and plot
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = len(self.packets)

        self.ptr1 += 1

        self.curve1.setData(self.data1)
        self.curve1.setPos(self.ptr1, 0)

    def StopMonitor(self):

        # Clearing Plots
        self.p1.clear()

