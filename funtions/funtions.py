import pandas as pd
import numpy as np


data = pd.read_csv('Dataset/DataCluster.csv')
#////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_numeric_columns(df):
    numeric_columns = []
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            numeric_columns.append(column)

    return numeric_columns

def show_numeric_columns():
    numeric_columns = get_numeric_columns(data)
    list = []
    for numeric in numeric_columns:
        list.append(numeric)

    return list
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_string_columns(df):
    string_columns = []
    for column in df.columns:
        if df[column].dtype in ['object']:
            string_columns.append(column)

    return string_columns

def show_string_columns():
    string_columns = get_string_columns(data)
    list = []
    for string in string_columns:
        list.append(string)

    return list
#//////////////////////////////////////////////////////////////////////////////////////////////
def get_unique_values(df, column_name):


    # Obtener los valores únicos de la columna.
    unique_values = df[column_name].unique()
    unique_values.append('Combined')

    # Devolver los valores únicos.
    return unique_values

def show_unique_values():
    unique = get_unique_values(df=data, column_name='Cluster')
    return unique

#////////////////////////////////////////////////////////////////////////////////////////////////////


def filter_cluster(dataframe, cluster):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe
        return data_cluster_combined

#////////////////////////////////////////////////////////////////////////////////////////////////////////

def cardsCashAmount(dataframe, cluster):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        data_cluster_1 = data_cluster_1['CashbackAmount'].mean()
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        data_cluster_2 = data_cluster_2['CashbackAmount'].mean()
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe['CashbackAmount'].mean()
        return data_cluster_combined

def daysincelastorder(dataframe, cluster):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        data_cluster_1 = data_cluster_1['DaySinceLastOrder'].mean()
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        data_cluster_2 = data_cluster_2['DaySinceLastOrder'].mean()
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe['DaySinceLastOrder'].mean()
        return data_cluster_combined

def OrderCount(dataframe, cluster):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        data_cluster_1 = data_cluster_1['OrderCount'].mean()
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        data_cluster_2 = data_cluster_2['OrderCount'].mean()
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe['OrderCount'].mean()
        return data_cluster_combined

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

def BarPlotCategorical(dataframe, cluster, column):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        data_cluster_1 = data_cluster_1[column].value_counts()
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        data_cluster_2 = data_cluster_2[column].value_counts()
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe[column].value_counts()
        return data_cluster_combined
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

def PiePlotCategorical(dataframe, cluster):
    if cluster == '0':
        data_cluster_1 = dataframe[dataframe['Cluster'] == 0]
        data_cluster_1 = data_cluster_1['Cluster'].value_counts()
        return data_cluster_1
    elif cluster == '1':
        data_cluster_2 = dataframe[dataframe['Cluster'] == 1]
        data_cluster_2 = data_cluster_2['Cluster'].value_counts()
        return data_cluster_2
    elif cluster == 'Combined':
        data_cluster_combined = dataframe['Cluster'].value_counts()
        return data_cluster_combined