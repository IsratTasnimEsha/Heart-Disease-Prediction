import os
import csv
import pandas as pd
import numpy as np
from phe import paillier
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from math import ceil

with open('Public_Key.pkl', 'rb') as public_key_file:
    public_key = pickle.load(public_key_file)

input_file = 'Encoded_Data.csv'
output_file = 'Encrypted_ST_Slope.csv'

encrypted_values = {}

with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

    for row in rows:
        plaintext_value = int(row['ST_Slope'])
        if plaintext_value not in encrypted_values:
            encrypted_values[plaintext_value] = public_key.encrypt(plaintext_value)
        row['ST_Slope'] = encrypted_values[plaintext_value]
    
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)