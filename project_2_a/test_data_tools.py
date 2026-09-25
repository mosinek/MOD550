import data_tools
import numpy as np

df = data_tools.create_data()
report = data_tools.integrity_check(df,n_col=6)
report

df_corrupted = df.copy()


df_corrupted.mask(np.random.rand(*df_corrupted.shape) < 0.01, np.nan, inplace=True)

cols = ["Humidity", "Wind speed", "Average rainfall"]
df_corrupted[cols] = df_corrupted[cols].mask(np.random.rand(len(df_corrupted), len(cols)) < 0.05, -df_corrupted[cols])

# duplicate should be at the end of transformation (beside drop), so that we don't accidentally make it unique
# added one duplicate, maybe more?
df_corrupted.loc[len(df_corrupted)] = df_corrupted.loc[100]

# if we drop a column, theres a good chance that the check_ranges will fail bc the column we delete isnt there
# is it something to be fixed? or should we leave it like that
df_corrupted.drop(columns=np.random.choice(df_corrupted.columns), inplace=True)

report_corrupted = data_tools.integrity_check(df_corrupted,n_col=6)
report_corrupted