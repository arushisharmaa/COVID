import numpy as np
import matplotlib.pyplot as plt
casesPerDayTravis = True 


# Plot the cumulative tests for HAYES COUNTY 
if casesPerDayTravis== True :
    # -------------------------------------------------------------------------------------------------
    # Load in the dates. These are strings, so we cannot use numpy.loadtxt() and must instead read the file manually.
    # -------------------------------------------------------------------------------------------------

    # This will go into the folder 'data/Hayes/' and will open the file 'dates.txt' with the 'read' permission, denoted by 'r'
    with open('data/Travis/datescasesPerDay.txt', 'r') as file:
        # Now read all the lines from the file into a list where each element is one line
        dates = file.readlines()

    # -------------------------------------------------------------------------------------------------
    # Now we must strip out the newline character "\n" from each string
    # -------------------------------------------------------------------------------------------------

    # Loop over each elements in the "dates" list
    for i in range(len(dates)):
        # Check to see if the newline character '\n' is present in the element
        if '\n' in dates[i]:
            # Split the element into two strings and take the first part. This assumes the newline character will always be at the end of the string. Look up the split() command online for more info.
            dates[i] = dates[i].split('\n')[0]

    # -------------------------------------------------------------------------------------------------
    # Load in the the confirmed case counts. These are numbers, so we can use numpy.loadtxt().
    # -------------------------------------------------------------------------------------------------
    cases = np.loadtxt('data/Travis/casesperDay.txt')

    # -------------------------------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------------------------------
    plt.plot(dates, cases, label='Loaded from file!')
    plt.xlabel("Time (days from 07/01/20-07/10/21)")
    plt.ylabel("New COVID-19 Confirmed Cases (number of individuals)")
    plt.title("New COVID-19 Confirmed Cases Per Day in Travis County")
    plt.show()