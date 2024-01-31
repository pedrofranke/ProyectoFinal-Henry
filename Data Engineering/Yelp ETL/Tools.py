import pandas as pd
import jsonlines

def analyze_data(dataframe):
    """
    This function takes a DataFrame as input and returns another DataFrame with 5 columns:
    1) Name: The name of the column.
    2) Unique Data Types: The unique data types present in the column.
    3) % of Non-null Values: Percentage of values that are not null.
    4) % of Null Values: Percentage of values that are null.
    5) Number of Null Values: Count of null values in the column.

    Parameters:
    DataFrame (pandas.DataFrame): The DataFrame to be processed.

    Returns:
    resume_dataframe (pandas.DataFrame): The resulting DataFrame after processing.
    """


    resume_dict = {"Name": [], "Unique Data Types": [], "% of Non-null Values": [], "% of Null Values": [], "Number of Null Values": []}

    for column in dataframe.columns:
        percentage_non_null = (dataframe[column].count() / len(dataframe)) * 100
        resume_dict["Name"].append(column)
        resume_dict["Unique Data Types"].append(dataframe[column].apply(type).unique())
        resume_dict["% of Non-null Values"].append(round(percentage_non_null, 2))
        resume_dict["% of Null Values"].append(round(100 - percentage_non_null, 2))
        resume_dict["Number of Null Values"].append(dataframe[column].isnull().sum())

    resume_dataframe = pd.DataFrame(resume_dict)
        
    return resume_dataframe

def count_and_percentage(dataframe, column):
    """
    This function processes a DataFrame and a specified column, 
    and returns the count of occurrences for each unique value in the column
    and the percentage representation of each value in the total data of that column.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be processed.
    column (str): The column on which operations are performed.

    Returns:
    The function prints information for the specified column.
    """
    
    quantity = dataframe.shape[0]
    quantity_column = dataframe[column].value_counts(dropna=False)
    Percentage_column = round((quantity_column / quantity) * 100, 2)
    
    print(f'The values of {column}:\n{quantity_column.to_string(header=False)}')
    print(f'\nThe percentage that each value represents:\n{Percentage_column.to_string(header=False)}')

def OpenJsonYelp(file_path):
    """
    This function takes a file path in JSON format and returns the file as a DataFrame.

    Parameters:
    file_path (str): The file path in JSON format.

    Returns:
    The function returns a DataFrame from the provided file.
    """
    json_objects = []

    with jsonlines.open(file_path) as reader:
     for line in reader:
          json_objects.append(line)

    dataframe = pd.DataFrame(json_objects)
    return dataframe

def duplicates(dataframe):
    """
    This function takes a DataFrame and returns a DataFrame with duplicate records.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be processed.

    Returns:
    duplicates (pandas.DataFrame): The resulting DataFrame after processing.
    """
    
    if dataframe.empty:
        print(f"The DataFrame {dataframe} has no duplicates")
        return {}

    duplicates = dataframe[dataframe.duplicated(keep=False)]
    
    return duplicates

def nulls(DataFrame,column):
    """
    This function takes a DataFrame and a column to analyze, and returns a DataFrame if it has null values.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be processed.

    Returns:
    null (pandas.DataFrame): The resulting DataFrame after processing.
    """

    null = DataFrame[DataFrame[column].isna()]
    null = pd.DataFrame(null)
    if null.empty:
        print(f'The column "{column}" does not have nulls')

    return null

def empty_values(DataFrame,column):
    """
    This function takes a DataFrame and a column to analyze, and returns a DataFrame if it has empty values.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be processed.
    column (str): The column on which operations are performed.
    
    Returns:
    emptys (pandas.DataFrame): The resulting DataFrame after processing.
    """

    emptys = [x for x in DataFrame[column] if x == '' or x is None]

    if not emptys:
        print(f'The column "{column}" does not have empty values')
        return None
    
    return pd.DataFrame(emptys)