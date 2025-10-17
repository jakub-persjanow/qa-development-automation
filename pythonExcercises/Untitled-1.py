# %%
import pandas as pd
from sklearn.datasets import load_wine

# %%
x = [1, 2, 3]

# %%
for i in x:
    print(i)

# %%
x

# %%
wine = load_wine()

# %%
x = pd.DataFrame(wine.data, columns=wine.feature_names)

# %%
x

# %%
heroes = pd.read_csv("/Users/jpersjan/Documents/qa-development-automation/resources/data/superheroes.csv")

# %%
heroes

# %%
heroes[""]

# %%
heroes.superhero_name

# %%
heroes.real_name

# %%
x.describe()


