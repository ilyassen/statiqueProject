import json
import csv
import subprocess
import os
import pandas as pd

import matplotlib.pyplot as plt

from datetime import datetime
import matplotlib.pyplot as plt
list_app = ["moodle"]

ApplicationName = "moodle"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"

for ApplicationName in list_app:
    list_files = {}
    pathFolder = "C:/Project/statiqueProject/" + ApplicationName
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

            if commitId not in list_files.keys():
                # print(list(list_files.keys())[-1])
                list_files[commitId] = {
                    filePath: [date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
                               ExcessiveParameter, NPathComplexity, CouplingBetweenObjects,
                               EmptyCatchBlock, DepthOfInheritance, GotoStatement]
                }

            else:
                list_files[commitId][filePath] = [date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
                                                  ExcessiveParameter, NPathComplexity, CouplingBetweenObjects,
                                                  EmptyCatchBlock, DepthOfInheritance, GotoStatement]


            line_count += 1
            # print((line_count/88444)*100)


    # with open(pathFolder + '/Analyse_Commits_Files_' + ApplicationName + '.json', 'w') as fp:
    #     json.dump(list_files, fp)


    csvfile1 = open("C:/Project/statiqueProject/results/R31/Commits_Analysis_" + ApplicationName + '.csv', 'a', newline='')

    with csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(('Commit id', 'date', 'file', 'CyclomaticComplexity', 'ExcessiveClassLength',
                         'ExcessiveMethodLength', 'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                         'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'Effective commit'))

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
        list_comits = {}
        for commit in list_files:
            nbr_commit += 1
            for file in list_files[commit]:
                if file not in list_comits:
                    list_comits[file] = {"number": 1}
                else:
                    list_comits[file]["number"] += 1
                writer.writerow((commit, list_files[commit][file][0], file,
                                 list_files[commit][file][1], list_files[commit][file][2],
                                 list_files[commit][file][3], list_files[commit][file][4],
                                 list_files[commit][file][5], list_files[commit][file][6],
                                 list_files[commit][file][7], list_files[commit][file][8],
                                 list_files[commit][file][9], list_comits[file]["number"]))

                # print(list_files[commit][file])
            print((nbr_commit/len(list_files))*100)


    csvfile1.close()






