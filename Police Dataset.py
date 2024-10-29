import pandas as pd
data = pd.read_csv('C:\\Users\\USER-PC\\Desktop\\Code Folder\\Police Dataset.csv')
# review data to check layout and information provided in the dataset
data #provides the column headers and the first and last 5 columns
# identify columns with missing values
data.isnull()
# determine the number of missing values in each column
data.isnull().sum()
# column country_name has no values and the entire column can be removed
data.drop(columns = 'country_name', inplace = True)
# were men or women stopped more often fopr speeding?
# filter speeding in the violation column and count the number of occurances for  male and female
data[data.violation == 'Speeding'].driver_gender.value_counts()
# does gender affect who gets searched during the stop?
data.groupby('driver_gender').search_conducted.sum()
# what is the mean stop duration
# data in the stop_duration column is a string. we need to first change the data type before we can calculate the mean
data.stop_duration.value_counts()
data['stop_duration'] = data['stop_duration'].map( {'0-15 Min': 7.5, '16-30 Min': 23.5, '30+ Min': 4}) # the original stop durations was a range between two numbers. we replaced each with the mediun of each range
# calculate the mean stop duration
data['stop_duration'].mean()
# compare age distribution for each violation
data.groupby('violation').driver_age.describe()