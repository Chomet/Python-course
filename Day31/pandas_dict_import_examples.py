# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("data\\nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# converting to dict
data_dict_normal = data.to_dict()
data_dict_dict = data.to_dict(orient="dict")  # equal to default value
                                              # name of column is key
                                              # value of column is tuple with with index as key and column value by index as value
data_dict_list = data.to_dict(orient="list")  # name of column is key, list of all values under column is value
# data_dict_series = data.to_dict(orient="series")  # not really useful
# data_dict_split = data.to_dict(orient="split")  # not really useful
data_dict_records = data.to_dict(orient="records")  # list of rows with key-value pairs of column name/column value
data_dict_index = data.to_dict(orient="index")  # dictionary where index is key and value is key-value pairs of column name/column value

# display
print(data_dict_normal)
print(data_dict_dict)
print(data_dict_list)
# print(data_dict_series)
# print(data_dict_split)
print(data_dict_records)
print(data_dict_index)
