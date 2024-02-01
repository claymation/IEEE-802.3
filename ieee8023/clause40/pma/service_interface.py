"""
§40.2.2 PMA Service Interface
"""


class ServiceInterface:
    def __init__(self, phy):
        self.phy = phy


class PMA_TXMODE(ServiceInterface):
    def indication(self, tx_mode):
        """
        §40.2.3 PMA_TXMODE.indication
        """
        pass


class PMA_CONFIG(ServiceInterface):
    def indication(self, config):
        """
        §40.2.4 PMA_CONFIG.indication
        """
        pass


class PMA_UNITDATA(ServiceInterface):
    def request(self, tx_symb_vector):
        """
        §40.2.5 PMA_UNITDATA.request
        """
        self.phy.mdi.output(tx_symb_vector)

    def indication(self):
        """
        §40.2.6 PMA_UNITDATA.indication
        """
        rx_symb_vector = self.mdi.sample()
        return rx_symb_vector


class PMA_SCRSTATUS(ServiceInterface):
    def request(self, scr_status):
        """
        §40.2.7 PMA_SCRSTATUS.request
        """
        pass


class PMA_RXSTATUS(ServiceInterface):
    def indication(self, loc_rcvr_status):
        """
        §40.2.8 PMA_RXSTATUS.request
        """
        pass


class PMA_REMRXSTATUS(ServiceInterface):
    def request(self, rem_rcvr_status):
        """
        §40.2.9 PMA_REMRXSTATUS.request
        """
        pass
