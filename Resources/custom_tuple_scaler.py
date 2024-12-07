from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
import numpy as np

class CustomTupleScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scaler = StandardScaler()  

    def _extract_c2(self, tuple_str):
        if isinstance(tuple_str, str): 
            tuple_val = eval(tuple_str)  
            if isinstance(tuple_val, tuple) and len(tuple_val) == 2:
                return tuple_val[1] 
        return np.nan  

    def fit(self, X, y=None):
        c2_values = X.applymap(self._extract_c2)
        self.scaler.fit(c2_values)
        return self

    def transform(self, X):
        c2_values = X.applymap(self._extract_c2)
        c2_scaled = self.scaler.transform(c2_values)
        return c2_scaled

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)