from .transmit import PCSTransmit


class PCS:
    def __init__(self, phy):
        self.phy = phy
        self.transmit = PCSTransmit(phy)
