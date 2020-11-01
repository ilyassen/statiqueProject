import json
import csv
import subprocess
import os

from datetime import datetime
import matplotlib.pyplot as plt

ApplicationName = "phpunit"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"
pathGitRepo = "C:/Project/statiqueProject/repositories/" + ApplicationName


Projects = ["phpunit", "laravel", "matomo"]



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



csvfile1 = open("C:/Project/statiqueProject/Results/InstancesTables/Instance_Statistique_Analyse_Projetcs.csv", 'a', newline='')

with csvfile1:

    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Project name','Smell','Created','Deleted'))
    for projetName in Projects:
        list_files = {}
        with open("C:/Project/statiqueProject/" + projetName + '/Survival/Cleaned_Survival_Statistique_Analyse_' + projetName + '.csv') as csv_file:

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

                if filePath not in list_files.keys():
                    list_files[filePath] = [[commitId, datetime.strptime(date.replace(',', ''), '%m/%d/%Y %H:%M:%S'), CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                             ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Commit_number]]

                list_files[filePath].append([commitId, datetime.strptime(date.replace(',', ''), '%m/%d/%Y %H:%M:%S'), CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                             ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Commit_number])
            csv_file.close()

        for element_range_smell in range(0, 9):
            counterCreatedSmell = 0
            counterDeletedSmell = 0
            for element_file in list_files.keys():
                cc = 0
                date = 0
                list_cc = []
                cpt = 1
                lenght = len(list_files[element_file])
                for element in list_files[element_file]:
                    # SMELL CREATED
                    if cc < int(element[(2 + element_range_smell)]):
                        while cc < int(element[2 + element_range_smell]):
                            list_cc.append({"date": element[1], "cc": int(element[2 + element_range_smell]), "file": filePath})
                            cc += 1
                            counterCreatedSmell +=1
                    # SMELL DIED
                    elif cc > int(element[2]):
                        while cc > int(element[2]):
                            fe = list_cc.pop(0)
                            print("File:" + element_file)
                            print(element[1] - fe['date'])
                            # writer.writerow(((element[1] - fe['date']).days, 1, 1 + element_range_smell, element_file))
                            cc -= 1
                            counterDeletedSmell +=1
                    elif lenght == cpt:
                        while list_cc:
                            fe = list_cc.pop(0)
                            print("File:" + element_file)
                            print(element[1] - fe['date'])
                            # writer.writerow(((element[1] - fe['date']).days, 0, 1 + element_range_smell, element_file))
                            cc -= 1
                    cpt += 1
            writer.writerow((projetName ,element_range_smell, counterCreatedSmell, counterDeletedSmell))


csvfile1.close()




