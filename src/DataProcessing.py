#data processing
import numpy as np 
import os 
import random 
import pickle 
import csv 
import pandas as pd 

y = []
X = []

df = pd.read_csv('../Data/bitcoinData.csv')
df = df.dropna()
data = df.as_matrix()[:,1:]

#split into samples 
samples = list()
length = 223
for i in range(0, len(data), length):
	sample = data[i:i+length]
	samples.append(sample)

#13 samples and 223 time steps per sample 

y = data[:,0].reshape((len(samples), length, 1))
X = data[:,1:].reshape((len(samples), length, data[:,1:].shape[1]))
print (X)
