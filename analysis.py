import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('ECO3.tsv', sep='\t', header=1)

df.columns = df.columns.str.replace(r" \(.+\)", '', regex=True)

df = df[df["RPM"] > 100]
df = df.truncate(after=df["RPM"].idxmax())

P_rc = np.mean(df["P2"]/df["P1"])

print(f"{P_rc:5d}")

plt.title("T04 vs Thrust")
plt.xlabel("Thrust (lbs)")
plt.ylabel("T04 (C)")
x = df["Thrust"]
y = df["T4"]

plt.plot(x, y)

plt.title("RPM vs Thrust")
plt.xlabel("Thrust (lbs)")
plt.ylabel("RPM")

plt.plot(df["Thrust"], df["RPM"])

plt.title("T04 vs RPM")
plt.xlabel("RPM")
plt.ylabel("T04 (C)")

plt.plot(df["RPM"], df["T4"])
