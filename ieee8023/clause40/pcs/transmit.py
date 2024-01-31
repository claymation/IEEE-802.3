CSReset      = (+2, -2, -2, +2)
SSD1         = (+2, +2, +2, +2)
SSD2         = (+2, +2, +2, -2)
ESD1         = (+2, +2, +2, +2)
ESD2_Ext_0   = (+2, +2, +2, -2)
ESD2_Ext_1   = (+2, +2, -2, +2)
ESD2_Ext_2   = (+2, -2, +2, +2)
ESD2_Ext_Err = (-2, +2, +2, +2)
IDLE         = (-2, +0, +0, +0)

class PCSTransmit:
    def __init__(self, gmii, pma):
        self.gmii = gmii
        self.pma = pma
        self.state_fn = self.send_idle

    def dispatch(self):
        self.state_fn()

    def send_idle(self):
        self.pma.unit_data.request(IDLE)
        if self.gmii.TX_EN:
            self.state_fn = self.ssd1

    def ssd1(self):
        self.pma.unit_data.request(SSD1)
        self.state_fn = self.ssd2

    def ssd2(self):
        self.pma.unit_data.request(SSD2)
        self.state_fn = self.error_check

    def error_check(self):
        if self.gmii.TX_EN:
            self.transmit_data()
        else:
            self.first_cs_reset()

    def transmit_data(self):
        self.pma.unit_data.request(self.encode(self.gmii.TXD))

    def first_cs_reset(self):
        self.pma.unit_data.request(CSReset)
        self.state_fn = self.second_cs_reset

    def second_cs_reset(self):
        self.pma.unit_data.request(CSReset)
        self.state_fn = self.esd1

    def esd1(self):
        self.pma.unit_data.request(ESD1)
        self.state_fn = self.esd2_ext_0

    def esd2_ext_0(self):
        self.pma.unit_data.request(ESD2_Ext_0)
        self.state_fn = self.send_idle

    def encode(self, TXD):
        return (0, 0, 0, 0)
