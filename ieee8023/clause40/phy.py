from .gmii import GMII
from .mdi import MDI
from .pcs.transmit import PCSTransmit
from .pma import PMA


class PHY:
    def __init__(self):
        self.gmii = GMII()
        self.mdi = MDI()
        self.pma = PMA(self.mdi)
        self.pcs_transmit = PCSTransmit(self.gmii, self.pma)

    def connect(self, link_partner):
        self.mdi.connect(link_partner)

    def dispatch(self):
        self.pcs_transmit.dispatch()
        peer = self.mdi.link_partner
        print(f"TX_EN={self.gmii.TX_EN:d} TXD={self.gmii.TXD:02x} "
              f"({self.mdi.BI_DA:+2d},{self.mdi.BI_DB:+2d},{self.mdi.BI_DC:+2d},{self.mdi.BI_DD:+2d})"
              f" -> "
              f"({peer.mdi.BI_DA:+2d},{peer.mdi.BI_DB:+2d},{peer.mdi.BI_DC:+2d},{peer.mdi.BI_DD:+2d})")

        
    def transmit(self, TXD):
        self.gmii.TX_EN = True
        self.dispatch() # Idle

        for byte in TXD:
            self.gmii.TXD = byte
            self.dispatch()

        self.gmii.TX_EN = False
        self.gmii.TXD = 0x00

        self.dispatch() # 1st CSReset
        self.dispatch() # 2nd CSReset
        self.dispatch() # ESD1
        self.dispatch() # ESD2


def connect(p, q):
    p.connect(q)
    q.connect(p)
