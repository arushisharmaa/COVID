import matplotlib.pyplot as plt
import csv
cases_per_day = False
cumulative_vaccines = False
cumulative_cases = False
cumulative_deaths = False
cumulative_tests = True
tests_per_day = True
percentage_positive_tests = True

if cases_per_day == True:
    x = []
    y = []
    with open('perday_cases_hayes.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(row[0])
                y.append(int(row[1]))
            
        
    plt.plot(x,y, label='cases per day')
    plt.xlabel('dates')
    plt.ylabel('number of cases')
    plt.title('cases per day')
    plt.legend()
    plt.show()
#cumulative vaccines
if cumulative_vaccines == True:
    x = []
    y = []
    with open('vaccines_hayesb.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(row[0])
                y.append(int(row[1]))
            
        
    plt.semilogy(x,y, label='Cumulative Vaccines')
    plt.xlabel('dates')
    plt.ylabel('number of vaccines administered')
    plt.title('Cumulative Vaccines')
    plt.legend()
    plt.show()

#cumulative cases

if cumulative_cases == True:
    x = []
    y = []
    with open('cum_cases_hayes.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(row[0])
                y.append(int(row[1]))
            
        
    plt.plot(x,y, label='Cumulative Cases')
    plt.xlabel('dates')
    plt.ylabel('cases')
    plt.title('Cumulative Cases')
    plt.legend()
    plt.show()

#cumulative deaths

if cumulative_deaths == True:
    x = []
    y = []
    with open('deaths_hayes.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x.append(row[0])
                y.append(int(row[1]))
            
        
    plt.plot(x,y, label='Cumulative Deaths')
    plt.xlabel('dates')
    plt.ylabel('deaths')
    plt.title('Cumulative deaths')
    plt.legend()
    plt.show()
    #cumulative tests
if cumulative_tests == True:
    x = []
    y = []
    with open('tests_hayesbb.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                 x.append(row[0])
                 y.append(int(row[1]))
    plt.plot(x,y, label='Cumulative tests')
    plt.xlabel('dates')
    plt.ylabel('tests')
    plt.title('Cumulative Tests')
    plt.legend()
    plt.show()


if tests_per_day == True:
    x1 =[]
    y1 = []
    with open('tests_per_day_hayes.csv','r') as csvfile_t:
            plots_t = csv.reader(csvfile_t, delimiter=',')
            for row in plots_t:
                    x1.append(row[0])
                    y1.append(int(row[1]))
    plt.plot(x1, y1, label = "Tests Per Day")
    plt.xlabel('dates')
    plt.ylabel('tests')
    plt.title('Tests Per day')
    plt.legend()
    plt.show()


if percentage_positive_tests == True:
    x1 =[]
    y1 = []
    with open('vaccines_pos_perc_hayes.csv','r') as csvfile_t:
            plots_t = csv.reader(csvfile_t, delimiter=',')
            for row in plots_t:
                    x1.append(row[0])
                    y1.append(int(row[1]))
    plt.semilogy(x1, y1, label = "percentage positive tests")
    plt.xlabel('dates')
    plt.ylabel('percentage')
    plt.title('Percentage of Positive Tests')
    plt.legend()
    plt.show()