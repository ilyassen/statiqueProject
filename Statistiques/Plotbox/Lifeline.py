import json
import csv
import subprocess
import os
import pandas as pd

import matplotlib.pyplot as plt

from datetime import datetime
import matplotlib.pyplot as plt
list_app = ["wordpress", "moodle", "laravel", "matomo", "phpunit"]

ApplicationName = "moodle"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"
pathGitRepo = "C:/Project/statiqueProject/repositories/" + ApplicationName






os.chdir(pathGitRepo)

CyclomaticComplexityList = []
ExcessiveClassLengthList = []
ExcessiveMethodLengthList = []
ExcessiveParameterList = []
NPathComplexityList = []
CouplingBetweenObjectsList = []
EmptyCatchBlockList = []
DepthOfInheritanceList = []
GotoStatementList = []

with open(pathFolder + '/Analyse_' + ApplicationName + '.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    count_commit = 0
    last_commit = ""
    for row in csv_reader:
        commitId = row["Commit id"]
        date = row["Date"]
        filePath = row["filename"]
        CyclomaticComplexity = int(row["CyclomaticComplexity"])
        ExcessiveClassLength= int(row["ExcessiveClassLength"])
        ExcessiveMethodLength = int(row["ExcessiveMethodLength"])
        ExcessiveParameter = int(row["ExcessiveParameterList"])
        NPathComplexity = int(row["NPathComplexity"])
        CouplingBetweenObjects = int(row["CouplingBetweenObjects"])
        EmptyCatchBlock = int(row["EmptyCatchBlock"])
        DepthOfInheritance = int(row["DepthOfInheritance"])
        GotoStatement = int(row["GotoStatement"])

        if line_count == 0 :
            list_files[commitId] = {
                filePath: [CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                           ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement]
            }

        elif commitId not in list_files.keys():
            # print(list(list_files.keys())[-1])
            list_files[commitId] = (list_files[list(list_files.keys())[-1]].copy())
            list_files[commitId][filePath] = [CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                              ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement]

        else:
            list_files[commitId][filePath] = [CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                           ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement]


        line_count += 1
        print((line_count/88444)*100)


# with open(pathFolder + '/Analyse_Commits_Files_' + ApplicationName + '.json', 'w') as fp:
#     json.dump(list_files, fp)

csvfile1 = open("C:/Project/statiqueProject/results/Commits_Analysis_" + ApplicationName + '.csv', 'a', newline='')

with csvfile1:
    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Commit id', 'CyclomaticComplexity', 'ExcessiveClassLength',
                     'ExcessiveMethodLength', 'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                     'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement'))

    nbr_commit = 0
    list_c1 = []
    list_c2 = []
    list_c3 = []
    list_c4 = []
    list_c5 = []
    list_c6 = []
    list_c7 = []
    list_c8 = []
    list_c9 = []

    for commit in list_files:
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0

        nbr_commit += 1
        for file in list_files[commit]:

            c1 += list_files[commit][file][0]
            c2 += list_files[commit][file][1]
            c3 += list_files[commit][file][2]
            c4 += list_files[commit][file][3]
            c5 += list_files[commit][file][4]
            c6 += list_files[commit][file][5]
            c7 += list_files[commit][file][6]
            c8 += list_files[commit][file][7]
            c9 += list_files[commit][file][8]

            # print(list_files[commit][file])
        print((nbr_commit/len(list_files))*100)
        writer.writerow((commit, c1, c2, c3, c4, c5, c6, c7, c8, c9))
        list_c1.append(c1)
        list_c2.append(c2)
        list_c3.append(c3)
        list_c4.append(c4)
        list_c5.append(c5)
        list_c6.append(c6)
        list_c7.append(c7)
        list_c8.append(c8)
        list_c9.append(c9)

csvfile1.close()
# smells_data = pd.read_csv("C:/Project/statiqueProject/results/Commits_Analysis_" + ApplicationName + ".csv",
#                           index_col=1, parse_dates=True)
# smells_data.plot()
#
# plt.show()
# df = pd.DataFrame(c1, index=ts.index, columns=list('A'))
# for element_range_smell in range(0, 9):
#     for element_file in list_files.keys():
#         cc = 0
#         date = 0
#         list_cc = []
#         cpt = 1
#         lenght = len(list_files[element_file])
#         for element in list_files[element_file]:
#
#             if cc < int(element[(2 + element_range_smell)]):
#                 while cc < int(element[2 + element_range_smell]):
#                     list_cc.append({"date": element[1], "cc": int(element[2 + element_range_smell]), "file": filePath})
#                     cc += 1
#             elif cc > int(element[2]):
#                 while cc > int(element[2]):
#                     fe = list_cc.pop(0)
#
#                     cc -= 1
#
#             elif lenght == cpt:
#                 while list_cc:
#                     fe = list_cc.pop(0)
#
#                     cc -= 1
#             cpt += 1
#
#
# print(list_files.keys())








