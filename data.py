# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
#
# Functions for loading data from files
#
# ------------------------------------------------------------
# Imports and namespaces
# ------------------------------------------------------------
import os
import numpy as np
import pandas as pd



# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------
# Load the data for case counts
def load_new_cases(filepath, county='Travis'):
    '''
    Load in the data for cumulative cases and return the new cases per day for the desired county.
    
    Parameters:
    filepath -- The path of the file containing the data.
    county -- A string of the county name.

    Returns:
    dates -- A numpy array of the dates on which the data was collected.
    cases -- A numpy array of the new case counts on each specific date.
    '''

    # Load the file with pandas
        # "header" is the zero-indexed row in the spreadsheet containing column labels
        # "index_col" is the zero-indexed column in the spreadsheet containing row labels
        # "nrows" is the number of rows of data to read in from the spreadsheet
    x = pd.read_excel(filepath, header=2, index_col=0, nrows=255)

    # Rip out the cumulative case count information
        # ".loc[county" searches for the row or column with the label in the county variable
        # ".values" gives the data value corrseponding to the label
    cumulative_cases = x.loc[county].values

    # Convert the cumulative cases to daily new cases by taking the difference between days
    # Note we have to ignore the very first day because don't have data for the zero-th day
    cases = np.ediff1d(cumulative_cases)

    # Rip out the dates information
        # ".index[1:]" takes the labels of the data. In this case, all of the dates after the first reported day
        # ".tolist()" converts the index array into a list of strings
    dates = x.loc[county].index[1:].tolist()

    # Process date strings
    for i in range(len(dates)):
        # Cut out the part of the string containing "Cases "
        dates[i] = dates[i].split(' ')[1]
    
    # Return
    return dates, cases



# Load the data for cumulative case counts
def load_cumulative_cases(filepath, county='Travis'):
    '''
    Load in the data for cumulative cases and return the cumulative cases over time for the desired county.

    Parameters:
    filepath -- The path of the file containing the data.
    county -- A string of the county name.

    Returns:
    dates -- A numpy array of the dates on which the data was collected.
    cases -- A numpy array of the cumulative case counts on each specific date.
    '''

    # Load the file with pandas
    x = pd.read_excel(filepath, header=2, index_col=0, nrows=255)

    # Get the cumulative case count info
    cases = x.loc[county].values

    # Get the dates
    dates = x.loc[county].index.tolist()

    # Process date strings
    for i in range(len(dates)):
        # Cut out the part of the string containing "Cases "
        dates[i] = dates[i].split(' ')[1]
    
    # Return
    return dates, cases



# Load the data for general hospitalization counts
def load_hospitalizations(filepath, TSA='O'):
    '''
    Load the general hospitalizations by for a given traume service area. Travis county is trauma service area "O".
    
    Parameters:
    filepath -- The path of the file containing the data.
    TSA -- A string containing the trauma service area of interest.
    
    Returns:
    dates -- A numpy array of the dates for the associated data.
    hospitalizations -- A numpy array of the hospitalizations for the associated date.
    '''

    # Load the file with pandas
        # "sheet_name=0" is a zero-indexed number choosing which of the excel sheets to load in a spreadsheet. In this case, we load the first sheet in the file.
    x = pd.read_excel(filepath, header=2, index_col=0, nrows=23, sheet_name=0)

    # Get the hospitalization info
    hospitalizations = x.loc[TSA].values[1:]

    # Get the dates
    dates = x.loc[TSA].index[1:].tolist()

    # Process date strings
    for i in range(len(dates)):
        # Cut out the part of the string containing "Cases "
        dates[i] = dates[i].split(' ')[1]
    
    # Return
    return dates, hospitalizations



# Load the data for occupied ICU beds
def load_ICU(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Load the data for news deaths per day by county
def load_new_deaths(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Load the data for cumulative deaths by county
def load_cumulative_deaths(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Load the data for new tests by county
def load_new_tests(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Load the data for cumulative tests by county
def load_cumulative_tests(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Load the data for vaccines administered over time
def load_vaccines_administered(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None