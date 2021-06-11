import pandas as pd
import csv
import matplotlib.pyplot as plt
import ast

from itertools import zip_longest

plot_list = []
list_app = [ "wordpress", "moodle", "laravel", "matomo", "phpunit"]
results_list = {}

for ApplicationName in list_app:
    results_list[ApplicationName] = []
    # ApplicationName = "laravel"
    path = "C:/Project/statiqueProject/results/Commits_Analysis_" + ApplicationName + ".csv"
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                row.pop(0)
                results_list[ApplicationName].append(list(map(int, row)))

i = 0

csvfile1 = open('C:/Project/statiqueProject/results/R1/Analysis_projects.csv', 'a', newline='')

with csvfile1:
    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Commit id', 'CyclomaticComplexity', 'ExcessiveClassLength',
                     'ExcessiveMethodLength', 'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                     'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement'))

    for l1, l2, l3, l4, l5 in zip_longest(
            results_list["wordpress"],
            results_list["moodle"],
            results_list["laravel"],
            results_list["matomo"],
            results_list["phpunit"],
            fillvalue=[]):
        result = [x + y + z + a + b for x, y, z, a, b in zip_longest(l1, l2, l3, l4, l5, fillvalue=0)]
        result.insert(0, i)
        plot_list.append(result)
        writer.writerow(result)
        i = i + 1


# for ApplicationName in list_app:
#     result = [x + y + z + a + b for x, y, z, a, b in zip_longest(
#         results_list["wordpress"],
#         results_list["moodle"],
#         results_list["laravel"],
#         results_list["matomo"],
#         results_list["phpunit"],
#         fillvalue=0)]

    # results_list = map(lambda x, y: x + y, results_list, smells_data)
    # print(results_list)

    # smells_data.plot(title="Évolution des codes puants du projet '" + ApplicationName + "'", xlabel = "#Commit")

    # plt.show()
    # plt.savefig("C:/Project/statiqueProject/Results/R1/" + ApplicationName)