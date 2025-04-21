import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ECO3.tsv', sep='\t', header=1)

df.columns = df.columns.str.replace(r" \(.+\)", '', regex=True)

df = df[(df["RPM"] > 100) & (df["RPM"] < df["RPM"].max())]

plt.title("T04 vs Thrust")
plt.plot(df["Thrust"], df["T4"])
