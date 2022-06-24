# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
#
# Driver for the code
#
# ------------------------------------------------------------
# Imports and namespaces
# ------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt

import plots
import data
import util



# ------------------------------------------------------------
# Main code
# ------------------------------------------------------------
# Check to see if this file is being run as the "main" file.
if __name__ == "__main__":
    # Load data for Travis county
    travis_new_cases_dates, travis_new_cases = data.load_new_cases('data/DSHS/Cases_by_County.xlsx')

    # Load data for Dallas county
    dallas_new_cases_dates, dallas_new_cases = data.load_new_cases('data/DSHS/Cases_by_County.xlsx', county='Dallas')

    # Plot the data
    plots.plot_new_cases(travis_new_cases_dates, travis_new_cases, 'Travis')
    plots.plot_new_cases(dallas_new_cases_dates, dallas_new_cases, 'Dallas')