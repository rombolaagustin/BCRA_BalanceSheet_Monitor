# Objects

class dataObj:
    def __init__(self, nominal_df):
        self.nominal = nominal_df

    def make_var_yearly(self):
        self.yearly = self.nominal.pct_change(freq='Y')
    