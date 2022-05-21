import collections
import time
import bluetooth
import sys
import subprocess

CONTINUOUS_REPORTING = "04"
COMMAND_LIGHT = 11
COMMAND_REPORTING = 12
COMMAND_REGISTER = 16
COMMAND_READ_REGISTER = 17
INPUT_STATUS = 20
INPUT_READ_DATA = 21
EXTENSION_8BYTES = 32
BUTTON_DOWN_MASK = 8
TOP_RIGHT = 0
BOTTOM_RIGHT = 1
TOP_LEFT = 2
BOTTOM_LEFT = 3


class wii_board:
    def __init__(self):
        pass
    def connect(self):
        
        ret = True

        # Bluetooth Sockets
        self.recieveSocket = None
        self.controlSocket = None

        self.address = None

        self.status = "Disconnected"

        try:
            self.recieveSocket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
            self.controlSocket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        except ValueError:
            ret = False
            
        return ret
    def isConnect(self):
        ret = True
        return ret
    def getCommand(self):
        gb_stop = 0
        gb_go = 1
        gb_back = 2
        rl_stop = 0
        rl_right = 1
        rl_left = 2
        
        ret_gb = gb_stop
        ret_rl = rl_stop
        return (ret_gb, ret_rl)
    def getControlStatus(self):
        var = []
        return var