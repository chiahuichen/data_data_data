import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# download covid data from data.cdc.gov, load it as dataframe, and sort it
df = pd.read_csv('covid.csv',).sort_values('submission_date')

# find dinctinct states 
states = np.array(df['state'].value_counts().keys())
# set the sorting dictionary
record = defaultdict(list)
# sort column "new_case" into its responding state
for x in range(len(df)):
    record[df.iloc[x]['state']].append(df.iloc[x]['new_case'])
# transform "record" into a dataframe "data"
data = pd.DataFrame(record)
# plotting
fig = plt.figure()
ax = fig.subplots()
ax = sns.heatmap(data, robust=True, linewidths=0, cmap='viridis', xticklabels=True)
ax.set_title('USA Covid-19 Daily New Cases in 2020')
ax.invert_yaxis()
ax.set_xlabel('States')
ax.set_ylabel('# of Day')
plt.show()



