import pandas as pd


df = pd.ExcelFile(r'D:\01PythonMUL\datasets\List of participants (ELIGIBLE).xlsx')
sheetX = df.parse(0)
for index, row in sheetX.iterrows():
    print(row[0])


