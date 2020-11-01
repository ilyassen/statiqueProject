import json
import csv
import subprocess
import os

ApplicationName = "moodle"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"
pathGitRepo = "C:/Project/statiqueProject/repositories/" + ApplicationName





os.chdir(pathGitRepo)

with open(pathFolder + "/Survival/Survival_Statistique_Analyse_" + ApplicationName + '.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = False
    ListFiles = []
    zero_flag = False
    LastfilePath = ""
    filePath = ""
    for row in csv_reader:
        if(line_count and row["filePath"] != LastfilePath and
                LastCyclomaticComplexity + LastExcessiveClassLength + LastExcessiveMethodLength +
                LastExcessiveParameter + LastNPathComplexity + LastCouplingBetweenObjects +
                LastEmptyCatchBlock + LastDepthOfInheritance + LastGotoStatement <= 0
        ):

            ListFiles.append([LastcommitId, LastDate, LastfilePath, LastCyclomaticComplexity, LastExcessiveClassLength, LastExcessiveMethodLength,
                              LastExcessiveParameter, LastNPathComplexity, LastCouplingBetweenObjects,
                              LastEmptyCatchBlock, LastDepthOfInheritance, LastGotoStatement, LastCommit_number])
            zero_flag = False
        if row["filePath"] != LastfilePath:
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
        commitId = row["commitID"]
        date = row["Date"]
        filePath = row["filePath"]
        CyclomaticComplexity = int(row["CyclomaticComplexity"])
        ExcessiveClassLength= int(row["ExcessiveClassLength"])
        ExcessiveMethodLength = int(row["ExcessiveMethodLength"])
        ExcessiveParameter = int(row["ExcessiveParameter"])
        NPathComplexity = int(row["NPathComplexity"])
        CouplingBetweenObjects = int(row["CouplingBetweenObjects"])
        EmptyCatchBlock = int(row["EmptyCatchBlock"])
        DepthOfInheritance = int(row["DepthOfInheritance"])
        GotoStatement = int(row["GotoStatement"])
        Commit_number = int(row["Commit number"])

        if (filePath == "file_ 96"):
            print("hello")

        # if(zero_flag):
        #     if (CyclomaticComplexity == BLastCyclomaticComplexity and
        #         ExcessiveClassLength == BLastExcessiveClassLength and
        #         ExcessiveMethodLength == BLastExcessiveMethodLength and
        #         ExcessiveParameter == BLastExcessiveParameter and
        #         NPathComplexity == BLastNPathComplexity and
        #         CouplingBetweenObjects == BLastCouplingBetweenObjects and
        #         EmptyCatchBlock == BLastEmptyCatchBlock and
        #         DepthOfInheritance == BLastDepthOfInheritance and
        #         GotoStatement == BLastGotoStatement ):
        #
        #         ListFiles.append([commitId, date, filePath, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
        #                           ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock,
        #                           DepthOfInheritance, GotoStatement, Commit_number])
        #     else:
        #         ListFiles.append([BLastcommitId, BLastDate, BLastfilePath, BLastCyclomaticComplexity, BLastExcessiveClassLength, BLastExcessiveMethodLength, \
        #                           BLastExcessiveParameter, BLastNPathComplexity, BLastCouplingBetweenObjects,
        #                           BLastEmptyCatchBlock, BLastDepthOfInheritance, BLastGotoStatement, BLastCommit_number])



        if (CyclomaticComplexity + ExcessiveClassLength + ExcessiveMethodLength +
                ExcessiveParameter + NPathComplexity + CouplingBetweenObjects +
                EmptyCatchBlock + DepthOfInheritance+ GotoStatement <= 0):
            if not zero_flag:
                zero_flag = True
                BLastcommitId = LastcommitId
                BLastDate = LastDate
                BLastfilePath = LastfilePath
                BLastCyclomaticComplexity = LastCyclomaticComplexity
                BLastExcessiveClassLength= LastExcessiveClassLength
                BLastExcessiveMethodLength = LastExcessiveMethodLength
                BLastExcessiveParameter = LastExcessiveParameter
                BLastNPathComplexity = LastNPathComplexity
                BLastCouplingBetweenObjects = LastCouplingBetweenObjects
                BLastEmptyCatchBlock = LastEmptyCatchBlock
                BLastDepthOfInheritance = LastDepthOfInheritance
                BLastGotoStatement = LastGotoStatement
                BLastCommit_number = LastCommit_number
        else:
            if(zero_flag):
                if (CyclomaticComplexity == BLastCyclomaticComplexity and
                        ExcessiveClassLength == BLastExcessiveClassLength and
                        ExcessiveMethodLength == BLastExcessiveMethodLength and
                        ExcessiveParameter == BLastExcessiveParameter and
                        NPathComplexity == BLastNPathComplexity and
                        CouplingBetweenObjects == BLastCouplingBetweenObjects and
                        EmptyCatchBlock == BLastEmptyCatchBlock and
                        DepthOfInheritance == BLastDepthOfInheritance and
                        GotoStatement == BLastGotoStatement ):
                    ListFiles.append([commitId, date, filePath, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
                                                 ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement,Commit_number])
                else:
                    ListFiles.append([LastcommitId, LastDate, LastfilePath, LastCyclomaticComplexity, LastExcessiveClassLength,
                                      LastExcessiveMethodLength, LastExcessiveParameter, LastNPathComplexity, LastCouplingBetweenObjects,
                                      LastEmptyCatchBlock, LastDepthOfInheritance, LastGotoStatement, LastCommit_number])
                    ListFiles.append([commitId, date, filePath, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
                                      ExcessiveParameter, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement,Commit_number])



                zero_flag = False
            else:
                ListFiles.append([commitId, date, filePath, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength, \
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



        # print(list_files[filePath][-1])
        # print(CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,\
        #     ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement)
        # print(list_files[filePath][-1][0], CyclomaticComplexity)


# print(json.dumps(list_files, indent = 4))

csvfile1 = open(pathFolder + "/Survival/Cleaned_Survival_Statistique_Analyse_" + ApplicationName + '.csv', 'a', newline='')

with csvfile1:

    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('Commit id','Date','filename','CyclomaticComplexity','ExcessiveClassLength','ExcessiveMethodLength', \
                     'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                     'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'Commit number'))
    for element in ListFiles:
        writer.writerow((element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12]))


csvfile1.close()



