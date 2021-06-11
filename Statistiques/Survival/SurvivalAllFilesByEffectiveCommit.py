import json
import csv
import subprocess
import os

from datetime import datetime
import matplotlib.pyplot as plt

ApplicationName = "wordpress"

list_files = {}

list_projects = ["laravel", "wordpress", "matomo", "phpunit", "moodle"]





for project in list_projects:

    pathFolder = "C:/Project/statiqueProject/" + project
    list_files[project]= {}
    CyclomaticComplexityList = []
    ExcessiveClassLengthList = []
    ExcessiveMethodLengthList = []
    ExcessiveParameterList = []
    NPathComplexityList = []
    CouplingBetweenObjectsList = []
    EmptyCatchBlockList = []
    DepthOfInheritanceList = []
    GotoStatementList = []
    with open(pathFolder + '/Survival/Cleaned_Survival_Statistique_Analyse_' + project + '.csv') as csv_file:

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
            Commit_number = int(row["Commit number"])

            if filePath not in list_files[project].keys():
                list_files[project][filePath] = [[commitId, datetime.strptime(date.replace(',', ''), '%m/%d/%Y %H:%M:%S'), CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                         ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Commit_number]]

            list_files[project][filePath].append([commitId, datetime.strptime(date.replace(',', ''), '%m/%d/%Y %H:%M:%S'), CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                         ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Commit_number])


csvfile1 = open("C:\Project\statiqueProject/Results/R3/Results_All_Commits.csv", 'a', newline='')

with csvfile1:
    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Time','Died','Group'))
    for project in list_projects:
        for element_range_smell in range(0, 9):
            for element_file in list_files[project].keys():
                cc = 0
                date = 0
                list_cc = []
                cpt = 1
                lenght = len(list_files[project][element_file])
                for element in list_files[project][element_file]:

                    if cc < int(element[(2 + element_range_smell)]):
                        while cc < int(element[2 + element_range_smell]):
                            list_cc.append({"commit": element[11], "cc": int(element[2 + element_range_smell]), "file": filePath})
                            cc += 1
                    elif cc > int(element[2]):
                        while cc > int(element[2]):
                            fe = list_cc.pop(0)
                            print("File:" + element_file)
                            print(element[11] - fe['commit'])
                            writer.writerow((abs((element[11] - fe['commit'])), 1, 1 + element_range_smell))
                            cc -= 1

                    elif lenght == cpt:
                        while list_cc:
                            fe = list_cc.pop(0)
                            print("File:" + element_file)
                            print(abs(element[11] - fe['commit']))
                            writer.writerow((abs((element[11] - fe['commit'])), 0, 1 + element_range_smell))
                            cc -= 1
                    cpt += 1


csvfile1.close()




