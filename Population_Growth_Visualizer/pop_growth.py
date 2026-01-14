import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Data Load
# ==============================
df = pd.read_csv("population.csv")

# ==============================
# Data Check
# ==============================
print(df.head())

# ==============================
# Line Chart: Population Trends
# ==============================
plt.figure(figsize=(8,5))

plt.plot(df["Year"], df["Pakistan"], marker="o", label="Pakistan")
plt.plot(df["Year"], df["India"], marker="o", label="India")
plt.plot(df["Year"], df["China"], marker="o", label="China")

plt.xlabel("Year")
plt.ylabel("Population (Millions)")
plt.title("Population Growth Comparison")
plt.legend()
plt.grid(True)

plt.show()
