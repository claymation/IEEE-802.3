class PMA:
    class UnitData:
        def __init__(self, mdi):
            self.mdi = mdi

        def request(self, tx_symb_vector):
            self.mdi.output(tx_symb_vector)

        def indication(self):
            rx_symb_vector = self.mdi.sample()
            return rx_symb_vector

    def __init__(self, mdi):
        self.unit_data = PMA.UnitData(mdi)
