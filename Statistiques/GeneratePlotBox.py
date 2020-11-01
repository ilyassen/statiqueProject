import json
import csv
import subprocess
import os

import matplotlib.pyplot as plt

ApplicationName = "phpunit"

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

with open(pathFolder + '/Survival/Cleaned_Survival_Statistique_Analyse_' + ApplicationName + '.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
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

        # print(filePath)

        # print(json.dumps(list_files, indent = 4))


        line_count += 1

        CyclomaticComplexityList.append(CyclomaticComplexity)
        ExcessiveClassLengthList.append(ExcessiveClassLength)
        ExcessiveMethodLengthList.append(ExcessiveMethodLength)
        ExcessiveParameterList.append(ExcessiveParameter)
        NPathComplexityList.append(NPathComplexity)
        CouplingBetweenObjectsList.append(CouplingBetweenObjects)
        EmptyCatchBlockList.append(EmptyCatchBlock)
        DepthOfInheritanceList.append(DepthOfInheritance)
        GotoStatementList.append(GotoStatement)

        print(line_count)






box_plot_data=[CyclomaticComplexityList, ExcessiveClassLengthList, ExcessiveMethodLengthList, ExcessiveParameterList,NPathComplexityList,CouplingBetweenObjectsList,EmptyCatchBlockList,DepthOfInheritanceList,GotoStatementList]
# plt.boxplot(box_plot_data)
# plt.show()

fig = plt.figure()

# ax = fig.add_axes(["CyclomaticComplexity","ExcessiveClassLength","ExcessiveMethodLength"])
# ax = fig.add_axes([0,0,1,1])

# Create the boxplot
# bp = ax.boxplot(box_plot_data)
# don't show outlier points
fig, axs = plt.subplots(1, 1)


plt.boxplot(box_plot_data, 0, '', labels=['CCO', 'ECL','EML','EP', 'NPC', 'CBO','ECB', 'DOI', 'GS'])

plt.show()





