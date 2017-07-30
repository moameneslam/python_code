import pandas as pd
import matplotlib.pyplot as plt 


data  = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
data.head()