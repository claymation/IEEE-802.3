class MDI:
    def __init__(self):
        # Bidirectional data differential pairs
        self.BI_DA = 0
        self.BI_DB = 0
        self.BI_DC = 0
        self.BI_DD = 0

        self.link_partner = None

    def connect(self, link_partner):
        self.link_partner = link_partner

    def output(self, tx_symb_vector):
        if self.link_partner is None: return

        (BI_DA, BI_DB, BI_DC, BI_DD) = tx_symb_vector
        
        # FIXME
        self.BI_DA = BI_DA
        self.BI_DB = BI_DB
        self.BI_DC = BI_DC
        self.BI_DD = BI_DD

        # §40.8.2 Crossover function
        self.link_partner.mdi.BI_DA = BI_DB
        self.link_partner.mdi.BI_DB = BI_DA
        self.link_partner.mdi.BI_DC = BI_DD
        self.link_partner.mdi.BI_DD = BI_DC

    def sample(self):
        return (self.BI_DA, self.BI_DB, self.BI_DC, self.BI_DD)
