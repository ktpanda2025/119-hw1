import os 
import pandas as pd
file_path = "data/population.csv"

output = os.popen(f'wc -l < {file_path}').read().strip()
print(type(output))

a= pd.read_csv(file_path)

print(a.shape[0])
