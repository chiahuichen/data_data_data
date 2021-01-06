This repository showcases data manipulation and plotting techniques. 

In the script 'covid_sns_heatmap.py', the raw covid cases dataset is downloaded from data.cdc.gov. 
(Each state submits its data daily since January 22nd, 2020.
At the time of writing, the latest update of the CDC dataset is on December 30th, 2020.)
This plot shows daily new cases in each state using seaborn heatmap.

![USA Covid-19 Daily New Cases in 2020](pictures/covid_heatmap_sorted.png)



In the script 'ny_mega_millions.py,' I explored the NY Mega Millions drawn numbers from 2008/01/01 to 2021/01/01. 
The row data is available at https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD.
In class ny_mega_millions, there are three methods:
"top_millions" by default returns five sets of frequently drawn numbers,
"random_millions" by default returns five sets of randomly chosen numbers,
"least_millions" by default returns five sets of least drawn numbers.

