from ..types import Signal

from .service_interface import PMA_UNITDATA


class PMA:
    def __init__(self, phy):
        self.phy = phy

        # Service interfaces
        self.unitdata = PMA_UNITDATA(phy)

        # Signals
        self.loc_rcvr_status = Signal(False)

    def transmit(self, tx_symb_vector):
        """
        §40.4.2.2 PMA Transmit function
        """
        self.phy.mdi.output(tx_symb_vector)

    def receive(self):
        """
        §40.4.2.3 PMA Receive function
        """
        rx_symb_vector = self.phy.mdi.sample()
        if rx_symb_vector is None:
            return False

        self.unitdata.indication(rx_symb_vector)

        return True