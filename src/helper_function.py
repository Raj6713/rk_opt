import numpy as np
import pandas as pd


def calculate_enter_and_exit(dataframe, minimum_value, variable_name, index_value):
    dataframe['Calculation'] = "true"
    dataframe.loc[index_value, "Calculation"] = "false"
    # data = dataframe[dataframe['Calculation'] == 'true']
    dataframe['Enter_or_Exit'] = dataframe['C']/dataframe[variable_name]
    min_in_enter_or_exit = np.min(dataframe[dataframe['Calculation'] == 'true']['Enter_or_Exit'])
    print(dataframe)
    # get index where min_in_enter_or_exit
    index_where_value_is_min = dataframe[dataframe['Enter_or_Exit'] == min_in_enter_or_exit].index.values[0]
    print(min_in_enter_or_exit, index_where_value_is_min)


