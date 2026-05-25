import pandas as pd
import numpy as np

data = {
    'Cell_ID':  ['Cell_01', 'Cell_02', 'Cell_03', 'Cell_04', 'Cell_05',
                 'Cell_06', 'Cell_07', 'Cell_08', 'Cell_09', 'Cell_10'],
    'OCV':      [3.72, 'N/A', 3.81, 3.91, 3.63,
                 3.55, 3.78, None, 3.88, 3.69],
    'Capacity': [2.85, 2.91, 2.78, 2.95, 2.88,
                 None, 2.82, 2.90, 2.76, 2.93]
}

df = pd.DataFrame(data)

df['OCV'] = df['OCV'].replace("N/A", np.nan)
df['OCV'] = pd.to_numeric(df['OCV'])
df['OCV'] = df['OCV'].fillna(df['OCV'].mean())
df['Capacity'] = df['Capacity'].fillna(df['Capacity'].mean())
#df['Result'] = np.where((df['OCV']<3.60) | (df['OCV']>3.85), 'FAIL', 'PASS')
result = []
for i in df['OCV']:
    if (i<3.60) or (i>3.85):
        result.append('FAIL')

    else:
        result.append('PASS')
df['Result'] = result
print(df['Result'])

print('===== Formation QC Report =====')
for _, row in df.iterrows():
    print(f"{row['Cell_ID']} -> OCV:{row['OCV']:.2f} -> {row['Result']}")
print('Total Cells:', len(df['Result']))
print('PASS:', (df['Result'] == 'PASS').sum())
print('FAIL:', (df['Result'] == 'FAIL').sum())
print('FAIL RATE:', (df['Result'] == 'FAIL').sum()/len(df['Result'])*100,'%')