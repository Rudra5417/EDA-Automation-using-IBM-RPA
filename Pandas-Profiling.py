import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests

import pandas_profiling
df = pd.read_csv("D:\\DataScience\\IBM\\adult.csv")

profile = pandas_profiling.ProfileReport(df,)
#%%
profile.to_widgets
#%%
print(profile)
#%%
profile.to_file("D:\\DataScience\\IBM\Adult.html")
