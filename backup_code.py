# to create the combined dfs for the trip durations

# # # NOTE TO SELF: this file was originally named pandas.py
# https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5?rq=1
# and it caused errors for line 8 - had to rename file
# # # NOTE: do not name files same name as pkgs

# dependencies
import pandas as pd

# read csv dated June 2017
csv1 = "Resources/June-17.csv"
june17_df = pd.read_csv(csv1)
# june17_df

# read csv dated July 2017
csv2 = "Resources/July-17.csv"
july17_df = pd.read_csv(csv2)
# july17_df

# create separate df to hold initial df for appending all other months
csv1 = "Resources/June-17.csv"
initial_df = pd.read_csv(csv1)

# append July 2017
combined_df = initial_df.append(july17_df)
# combined_df

# read csv dated June 2018
csv3 = "Resources/June-18.csv"
june18_df = pd.read_csv(csv3)
# june18_df

# append June 2018
combined_df = combined_df.append(june18_df)
# combined_df

 # read csv dated July 2018
csv4 = "Resources/July-18.csv"
july18_df = pd.read_csv(csv4)
# july18_df

# append July 2018
combined_df = combined_df.append(july18_df)
# combined_df

# read csv dated June 2019
csv5 = "Resources/June-19.csv"
june19_df = pd.read_csv(csv5)
# june19_df

# append June 2019
combined_df = combined_df.append(june19_df)
# combined_df

 # read csv dated July 2019
csv6 = "Resources/July-19.csv"
july19_df = pd.read_csv(csv6)
# july19_df

# append July 2019
# name for all summer months == combined_s_df
combined_s_df = combined_df.append(july19_df)
combined_s_df

# create an output folder and save a new csv there
combined_s_df.to_csv('Output/all_summer_2017-19.csv', index=False)

# read csv dated Jan 2017
csv7 = "Resources/Jan-2017.csv"
jan17_df = pd.read_csv(csv7)
# jan17_df

# read csv dated Feb 2017
csv8 = "Resources/Feb-2017.csv"
feb17_df = pd.read_csv(csv8)
# feb17_df

# create separate df to hold initial df for appending all other months
csv7 = "Resources/Jan-2017.csv"
initial2_df = pd.read_csv(csv7)
# initial2_df

# append Feb 2017 to newly created combined winter months df
winter_df = initial2_df.append(feb17_df)
# winter_df

# print out Jan 2018 list of columns when the formatting changes
jan18_df.columns

# copy and paste this list in order to rename column list for combined_w_df
winter_df.columns = ['tripduration', 'starttime', 'stoptime', 'start station id',
       'start station name', 'start station latitude',
       'start station longitude', 'end station id', 'end station name',
       'end station latitude', 'end station longitude', 'bikeid', 'usertype',
       'birth year', 'gender']
# winter_df

# read csv dated Jan 2018
csv9 = "Resources/Jan-2018.csv"
jan18_df = pd.read_csv(csv9)
# jan18_df

# append Jan 2018
winter_df = winter_df.append(jan18_df)
# winter_df

# read csv dated Feb 2018
csv10 = "Resources/Feb-2018.csv"
feb18_df = pd.read_csv(csv10)
# feb18_df

# append Feb 2018
winter_df = winter_df.append(feb18_df)
# winter_df

# read csv dated Jan 2019
csv11 = "Resources/Jan-2019.csv"
jan19_df = pd.read_csv(csv11)
# jan19_df

# append Jan 2019
winter_df = winter_df.append(jan19_df)
# winter_df

# read csv dated Feb 2019
csv12 = "Resources/Feb-2019.csv"
feb19_df = pd.read_csv(csv12)
# feb19_df

# append Feb 2019
winter_df = winter_df.append(feb19_df)
# winter_df

# output new csv for Jan/Feb 2017-2019 data
winter_df.to_csv('Output/all_winter_2017-19.csv', index=False)

# combine both dfs by pd.append -- called "combined winter summer df"
combined_w_s_df = combined_s_df.append(winter_df)
combined_w_s_df

# out to all combined data to csv
combined_w_s_df.to_csv('Output/all_combined_2017-2019.csv', index=False)