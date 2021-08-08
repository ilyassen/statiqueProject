import json
import csv
import subprocess
import os

import matplotlib.pyplot as plt

ApplicationName = "laravel"

list_files = {}

rootFolder = "C:/Project/statiqueProject"
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
lastcommitId = ""

CyclomaticComplexityCount = 0
ExcessiveClassLengthCount = 0
ExcessiveMethodLengthCount = 0
ExcessiveParameterCount = 0
NPathComplexityCount = 0
CouplingBetweenObjectsCount = 0
EmptyCatchBlockCount = 0
DepthOfInheritanceCount = 0
GotoStatementCount = 0

try:
    subprocess.check_output("git checkout master ", shell=True)
    out = subprocess.check_output("phpmd " + pathGitRepo + " json " + rootFolder + "/myRuleset.xml ", shell=True)
    result_dict = json.loads(out)
except:
    print('Error')

NPathComplexity = 0
CyclomaticComplexity = 0
ExcessiveClassLength = 0
ExcessiveMethodLength =0
ExcessiveParameterList = 0
CouplingBetweenObjects = 0
EmptyCatchBlock = 0
DepthOfInheritance = 0
GotoStatement = 0

for file in result_dict['files']:



    for violation in file['violations']:

        if violation['rule'] == 'CyclomaticComplexity':
            CyclomaticComplexity = CyclomaticComplexity + 1
        if violation['rule'] == 'NPathComplexity':
            NPathComplexity = NPathComplexity + 1
        if violation['rule'] == 'ExcessiveClassLength':
            ExcessiveClassLength = ExcessiveClassLength + 1
        if violation['rule'] == 'ExcessiveMethodLength':
            ExcessiveMethodLength = ExcessiveMethodLength + 1
        if violation['rule'] == 'ExcessiveParameterList':
            ExcessiveParameterList = ExcessiveParameterList + 1
        if violation['rule'] == 'CouplingBetweenObjects':
            CouplingBetweenObjects = CouplingBetweenObjects + 1
        if violation['rule'] == 'EmptyCatchBlock':
            EmptyCatchBlock = EmptyCatchBlock + 1
        if violation['rule'] == 'DepthOfInheritance':
            DepthOfInheritance = DepthOfInheritance + 1
        if violation['rule'] == 'GotoStatement':
            GotoStatement = GotoStatement + 1

box_plot_data=[CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,
               ExcessiveParameterList,NPathComplexity,CouplingBetweenObjects,EmptyCatchBlock,
               DepthOfInheritance,GotoStatement]
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





