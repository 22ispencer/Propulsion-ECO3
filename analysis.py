import pandas as pd

df = pd.read_csv('ECO3.tsv', sep='\t', header=1)

df.columns = df.columns.str.replace(r" \(.+\)", '', regex=True)

df = df[df["RPM"] > 100]

print(df)

import matplotlib.pyplot as plt

plt.title("T04 vs Thrust")
plt.plot(df["Thrust"], df["T4"])
