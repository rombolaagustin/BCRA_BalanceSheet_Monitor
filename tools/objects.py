# Objects

class dataObj:
    def __init__(self, nominal_df):
        self.nominal = nominal_df

    def make_var_yearly(self, base100: bool = True):
        self.yearly = self.nominal.pct_change(periods=365, fill_method='ffill') #freq
        if base100:
            self.yearly = self.yearly*100
    