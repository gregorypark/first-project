import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set seed for random numbers
seed_for_prng = 78557
prng = np.random.default_rng(
    seed_for_prng
)  # prng=probabilistic random number generator

df = pd.read_csv(
    "sw.csv",
    index_col=0,
).dropna(subset=["species"])
# Check info about dataframe
df.info()

#looking at first 10 rows
df.head(10)

#filtering brown hair, blue eyes and showing who's left
df.loc[(df["hair_color"] == "brown") & (df["eye_color"] == "blue"), ["name", "species", "height"]]

#sorting in ascending order
df.sort_values(["height"])

#random sample and percentage
df.sample(5)
df.sample(frac=.03)

#renaming stuff
df.rename(columns={"homeworld": "home_world"})

#adding a column
df["height_m"] = df["height"] / 100
df.head()

#alphabetically sorting columns
(df.assign(height_m=df["height"] / 100).sort_index(axis=1))

#quick summary
df.describe()

#simple graphs
df.plot.scatter("mass", "height", alpha=0.5)
df.plot.box(column="height")

#exporting a table to latex
table = df[["mass", "height"]].agg(["mean", "std"])
table
print(table.style.to_latex(caption="A Table", label="tab:descriptive"))