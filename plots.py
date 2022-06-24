# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
#
# Functions to plot COVID data.
#
# ------------------------------------------------------------
# Imports and namespaces
# ------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt

import util



# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------
# Plot the new cases over time
def plot_new_cases(dates, cases, county):
    '''
    Plot the new covid case counts over time for a specific county.

    Parameters:
    dates -- A list of strings containing the date for a given element of data. Assumes MM-DD-YYYY format
    cases -- Cumulative case counts over time.
    county -- A string containing the county name.

    Returns:
    None -- The plots are generated in function.
    '''
    
    # Convert strings of dates into integer values for use in the x-axis
    days = util.calculate_x_axis_days(dates)

    # Figure
    fig = plt.figure(figsize=[10, 10])

    # Bar plot
    plt.bar(days, cases)

    # Labels and grids
    plt.title('New COVID Cases Over Time for ' + county + ' County')
    plt.xlabel('Days Elapsed') # Note: I am gonna leave you guys to figure out how to re-label the ticks on the x-axis with proper dates. Look into plt.xticks(), plt.set_xticks(), and plt.set_xticklabels().
    plt.ylabel('New COVID Cases')
    plt.grid()

    # Show
    plt.show()

    # Return
    return None



# Plot the cumulative cases over time
def plot_cumulative_cases(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the COVID hospitalizations over time
def plot_hospitalizations(countyName):
    '''
    <Docstring goes here>
    '''   
    x = []
    y = []
    with open(countyName.csv,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(row[0])
                y.append(int(row[1]))
            
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the number of COVID patients in the ICU over time
def plot_ICU(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the data for news deaths per day by county
def plot_new_deaths(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the data for cumulative deaths by county
def plot_cumulative_deaths(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the data for new tests by county
def plot_new_tests(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the data for cumulative tests by county
def plot_cumulative_tests(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None



# Plot the data for vaccines administered over time
def plot_vaccines_administered(function_arguments_go_here):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None