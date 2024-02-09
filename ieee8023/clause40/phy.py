from .gmii import GMII
from .mdi import MDI
from .pcs import PCS
from .pma import PMA


class PHY:
    def __init__(self, TXD=None, master=True, mdi_x=False):
        def generator(TXD):
            while TXD is None:
                yield (False, 0x00)

            for byte in TXD:
                yield (True, byte)

            yield (False, 0x00)  # 1st CSReset
            yield (False, 0x00)  # 2nd CSReset
            yield (False, 0x00)  # ESD1
            yield (False, 0x00)  # ESD2

        self.iter = generator(TXD)
        self.master = master
        self.mdi_x = mdi_x

        self.gmii = GMII()
        self.mdi = MDI()
        self.pcs = PCS(self)
        self.pma = PMA(self)

    def run(self):
        while self.transmit() and self.receive():
            pass
    
    def transmit(self):
        try:
            (self.gmii.TX_EN, self.gmii.TXD) = next(self.iter)
        except StopIteration:
            return False

        self.pcs.transmit.dispatch()

        return True

    def receive(self):
        return self.pma.receive()
