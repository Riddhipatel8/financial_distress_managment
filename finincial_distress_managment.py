import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("D:\riddhi - TY\Sem 5\Program\PDS\Financial Distress.csv")

print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Financial Distress.html"
