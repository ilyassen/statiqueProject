import json
import csv
import subprocess
import os

ApplicationName = "phpunit"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"
pathGitRepo = "C:/Project/statiqueProject/repositories/" + ApplicationName





os.chdir(pathGitRepo)

with open(pathFolder + "/Survival/Cleaned_Survival_Statistique_Analyse_" + ApplicationName + '.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = False
    ListFiles = []
    zero_flag = False
    LastfilePath = ""
    filePath = ""
    for row in csv_reader:
        # If not the first itteration and not the last file and line not smelly
        # (It means not smelly and last row for a file)

        if row["filename"] != LastfilePath:
            LastcommitId = ""
            BLastCyclomaticComplexity = -1
            BLastExcessiveClassLength= -1
            BLastExcessiveMethodLength = -1
            BLastExcessiveParameter = -1
            BLastNPathComplexity = -1
            BLastCouplingBetweenObjects = -1
            BLastEmptyCatchBlock = -1
            BLastDepthOfInheritance = -1
            BLastGotoStatement = -1
            BLastCommit_number = -1

        line_count = True
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


        if commitId != LastcommitId :

                ListFiles.append([commitId, date, filePath, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
                              ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement,Commit_number])

        LastcommitId = commitId
        LastDate = date
        LastfilePath = filePath
        LastCyclomaticComplexity = CyclomaticComplexity
        LastExcessiveClassLength= ExcessiveClassLength
        LastExcessiveMethodLength = ExcessiveMethodLength
        LastExcessiveParameter = ExcessiveParameter
        LastNPathComplexity = NPathComplexity
        LastCouplingBetweenObjects = CouplingBetweenObjects
        LastEmptyCatchBlock = EmptyCatchBlock
        LastDepthOfInheritance = DepthOfInheritance
        LastGotoStatement = GotoStatement
        LastCommit_number = Commit_number



csvfile1 = open(pathFolder + "/Survival/Test_Cleaned_Survival_Statistique_Analyse_" + ApplicationName + '.csv', 'a', newline='')

with csvfile1:

    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Commit id','Date','filename','CyclomaticComplexity','ExcessiveClassLength','ExcessiveMethodLength', \
                     'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                     'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'Commit number'))
    for element in ListFiles:
        writer.writerow((element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12]))


csvfile1.close()



