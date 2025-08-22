import pandas as pd
import numpy as np
from sklearn.datasets import load_wine

wine = load_wine()
x = pd.DataFrame(wine.data, columns=wine.feature_names)

print(type(x))
print(x)

# 0. Stworzyć inetraktywne okno
# 1. Wyprintować nazwy kolumn
# 2. Wyprintować średnie wartości dla kaźdej kolumny
# 3. wczytać cvskę z bohaterami uzywając pd.read_csv()
# 4. Wyprintować nazwy kolumn bohaterów
# 5. Stworzyć skryp pythonowy z inetraktywnego okna -> pusnąć na repo

# przymnieć sobie Beautiful Soup - jak uywać, co robi i jak znajdować wartości z tabel