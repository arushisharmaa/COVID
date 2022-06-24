# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
#
# Functions for general purpose utility
#
# ------------------------------------------------------------
# Imports and namespaces
# ------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime



# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------
# Create a 
def calculate_x_axis_days(dates):
    '''
    Convert a list of dates in MM-DD-YYYY format into a numpy array of integers containing the number of days since the first date in the list.

    Parameters:
    dates -- A list of strings containing dates in MM-DD-YYYY format.

    Returns:
    days -- A numpy array of days since the data starts.
    '''
    
    # Split the first date string and convert to integers
    m1 = int(dates[0].split('-')[0])
    d1 = int(dates[0].split('-')[1])
    y1 = int(dates[0].split('-')[2])

    # Split the terminal date string and convert to integers
    m2 = int(dates[-1].split('-')[0])
    d2 = int(dates[-1].split('-')[1])
    y2 = int(dates[-1].split('-')[2])

    # Calculate the days between the two dates
    days_elapsed = (datetime.date(y2, m2, d2) - datetime.date(y1, m1, d1)).days + 1

    # Construct a numpy array of integers for days
    days = np.arange(days_elapsed)

    # Return the days
    return days



# Get the ticks and labels for the X-axis for specific dates
def calculate_x_ticks_and_labels(dates):
    '''
    <Docstring goes here>
    '''
    
    # Code goes here

    # This is a placeholder; add a return statement for your data when you fill this out.
    return None