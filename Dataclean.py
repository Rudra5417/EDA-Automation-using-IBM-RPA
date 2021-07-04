from datacleaner import autoclean
import pandas as pd

#%%

my_data = pd.read_csv('D:\\DataScience\\IBM\\adult.csv', sep=',')
my_clean_data = autoclean(my_data)
my_data.to_csv('D:\\DataScience\\IBM\\my_clean_data.csv', sep=',', index=False)

#%%
import pandas as pd
import pandas_profiling

#%%
df = pd.read_csv("D:\\DataScience\\IBM\\my_clean_data.csv")
#%%
profile = pandas_profiling.ProfileReport(df,)
#%%
profile.to_widgets
#%%
profile
#%%
profile.to_file("D:\\DataScience\\IBM\\cleandata.html")