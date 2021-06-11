import json
import csv
import subprocess
import os



list_projects = ["moodle", "laravel", "wordpress", "matomo", "phpunit"]



pathFolder = "C:/Project/statiqueProject/Results/R31/"

for ApplicationName in list_projects:

    list_files = {}
    with open(pathFolder + "Commits_Analysis_" + ApplicationName + '.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            commitId = row["Commit id"]
            date = row["date"]
            filePath = row["file"]
            CyclomaticComplexity = int(row["CyclomaticComplexity"])
            ExcessiveClassLength= int(row["ExcessiveClassLength"])
            ExcessiveMethodLength = int(row["ExcessiveMethodLength"])
            ExcessiveParameterList = int(row["ExcessiveParameterList"])
            NPathComplexity = int(row["NPathComplexity"])
            CouplingBetweenObjects = int(row["CouplingBetweenObjects"])
            EmptyCatchBlock = int(row["EmptyCatchBlock"])
            DepthOfInheritance = int(row["DepthOfInheritance"])
            GotoStatement = int(row["GotoStatement"])
            Effective_commit = int(row["Effective commit"])


            line_count += 1
            if filePath not in list_files.keys() :
                list_files[filePath] = [[commitId, date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                         ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Effective_commit]]

            elif list_files[filePath][-1][2] != CyclomaticComplexity or  list_files[filePath][-1][3] != ExcessiveClassLength or \
                    list_files[filePath][-1][4] != ExcessiveMethodLength or list_files[filePath][-1][5] != ExcessiveParameterList or \
                    list_files[filePath][-1][6] != NPathComplexity or list_files[filePath][-1][7] != CouplingBetweenObjects or \
                    list_files[filePath][-1][8] != EmptyCatchBlock or list_files[filePath][-1][9] != DepthOfInheritance or \
                    list_files[filePath][-1][10] != GotoStatement:

                if (list_files[filePath][-1][2] != CyclomaticComplexity*2 or  list_files[filePath][-1][3] != ExcessiveClassLength*2 or \
                    list_files[filePath][-1][4] != ExcessiveMethodLength*2 or list_files[filePath][-1][5] != ExcessiveParameterList*2 or \
                    list_files[filePath][-1][6] != NPathComplexity*2 or list_files[filePath][-1][7] != CouplingBetweenObjects*2 or \
                    list_files[filePath][-1][8] != EmptyCatchBlock*2 or list_files[filePath][-1][9] != DepthOfInheritance*2 or \
                    list_files[filePath][-1][10] != GotoStatement*2) or (CyclomaticComplexity == 1 or  ExcessiveClassLength == 1 and \
                                                                         (ExcessiveMethodLength <= 1 and ExcessiveParameterList <= 1 and \
                                                                          NPathComplexity <= 1 and CouplingBetweenObjects <= 1 and \
                                                                          EmptyCatchBlock <= 1 and DepthOfInheritance <= 1 and \
                                                                          GotoStatement <= 1)):
                    list_files[filePath].append([commitId, date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
                                                 ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement, Effective_commit])
                    print("Data : " + commitId)


    csvfile1 = open(pathFolder + "/CleanedStatistique_Analyse_" + ApplicationName + '.csv', 'a', newline='')

    with csvfile1:

        writer = csv.writer(csvfile1, delimiter=',')
        writer.writerow(('commit Id','Date','filename','CyclomaticComplexity','ExcessiveClassLength','ExcessiveMethodLength', \
                         'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects', 'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'Effective Commit'))
        list_commits = {}
        for path in list_files:

            for element in list_files[path]:
                writer.writerow((element[0], element[1], path, element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11]))
    csvfile1.close()



