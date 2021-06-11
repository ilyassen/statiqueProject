import json
import csv
import subprocess
import os

import matplotlib.pyplot as plt

ApplicationName = "moodley"

list_files = {}

pathFolder = "C:/Project/statiqueProject/"
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

with open(pathFolder + '/Results/resultq2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        CyclomaticComplexity = int(row["CyclomaticComplexity"])
        ExcessiveClassLength = int(row["ExcessiveClassLength"])
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

# fig = plt.figure()

# ax = fig.add_axes(["CyclomaticComplexity","ExcessiveClassLength","ExcessiveMethodLength"])
# ax = fig.add_axes([0,0,1,1])

# Create the boxplot
# bp = ax.boxplot(box_plot_data)
# don't show outlier points
# fig, axs = plt.subplots(1, 1)

fig, axs = plt.subplots()

plt.boxplot(box_plot_data, showfliers=False, labels=['HMC', 'ECL','EML','EPL', 'HNPC', 'HC','ECB', 'EDOI', 'GS'])



plt.suptitle("Distribution des codes puants dans les projets étudier")


plt.show()





