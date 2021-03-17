import pandas as pd

lg = [
    [151500,152500,153500,150500],
    [152500,149500,154500,149500],
    [147500,143500,149000,143500],
]

col_index = ['close','start','high','low']
row_index = ['2021.03.15','2021.03.12','2021.03.11']

df = pd.DataFrame(lg, columns = col_index, index = row_index)
print(df)
print(df['close']['2021.03.15'])