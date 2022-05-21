class wii_board:
    def __init__(self):
        pass
    def connect(self):
        ret = True
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