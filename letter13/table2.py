import pandas as pd

kospi = [
    ['삼성전자', '005930'],
    ['SK하이닉스', '000660'],
    ['NAVER', '035420'],
    ['LG화학', '051910'],
    ['현대차', '005380']
]

col_index = ['name', 'code']

df = pd.DataFrame(kospi, columns = col_index)
row_picked = df.iloc[3]

print(row_picked)
print(row_picked['name'])