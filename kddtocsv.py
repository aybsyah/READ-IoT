import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import time

path='/home/aymen/kdd.csv'
print(path) 

df = pd.read_csv(path, header=None)

print("Read {} rows.".format(len(df)))
df = df.sample(frac=0.1, replace=False) # Uncomment this line to sample only 10% of the dataset
print("Extracted {} rows.".format(len(df)))
#df.dropna(inplace=True,axis=1) # For now, just drop NA's (rows with missing values)

df.to_csv("/home/aymen/kdd011.csv")
