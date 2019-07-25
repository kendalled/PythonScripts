# Combine and Clean
import pandas as pd

temp_df = pd.read_csv('mergedARFINAL.csv')
#


temp_df = temp_df.drop_duplicates()

print(temp_df)

temp_df.to_csv('cleaned.csv')
