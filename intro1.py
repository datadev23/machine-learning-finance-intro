import pandas as pd

df = pd.read_csv("data/HCP.csv");
# print all frames
#print df;
# shows rows 10 to 20
#print df[10:21];
print df['Close'].max();
