import json
import csv
import subprocess
import os

ApplicationName = "laravel"

list_files = {}

pathFolder = "C:/Project/statiqueProject/" + ApplicationName
pathRepositories = pathFolder + "/repositories"
pathGitRepo = "C:/Project/statiqueProject/repositories/" + ApplicationName

def get_number_commits(commitId):
    cmd_checkout = "git checkout " + commitId + " -f"
    subprocess.check_output(cmd_checkout, shell=True)
    return int(subprocess.check_output("git rev-list --count HEAD", shell=True))


os.chdir(pathGitRepo)

with open(pathFolder + '/analyse_' + ApplicationName + '.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        commitId = row["Commit id"]
        date = row["Date"]
        filePath = row["filename"]
        CyclomaticComplexity = int(row["CyclomaticComplexity"])
        ExcessiveClassLength= int(row["ExcessiveClassLength"])
        ExcessiveMethodLength = int(row["ExcessiveMethodLength"])
        ExcessiveParameterList = int(row["ExcessiveParameterList"])
        NPathComplexity = int(row["NPathComplexity"])
        CouplingBetweenObjects = int(row["CouplingBetweenObjects"])
        EmptyCatchBlock = int(row["EmptyCatchBlock"])
        DepthOfInheritance = int(row["DepthOfInheritance"])
        GotoStatement = int(row["GotoStatement"])
        
        # print(filePath)

        # print(json.dumps(list_files, indent = 4))
        

        line_count += 1
        if filePath not in list_files.keys() :
            list_files[filePath] = [[commitId, date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,\
            ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement]]

        elif list_files[filePath][-1][2] != CyclomaticComplexity or  list_files[filePath][-1][3] != ExcessiveClassLength or\
                list_files[filePath][-1][4] != ExcessiveMethodLength or list_files[filePath][-1][5] != ExcessiveParameterList or\
                list_files[filePath][-1][6] != NPathComplexity or list_files[filePath][-1][7] != CouplingBetweenObjects or\
                list_files[filePath][-1][8] != EmptyCatchBlock or list_files[filePath][-1][9] != DepthOfInheritance or\
                list_files[filePath][-1][10] != GotoStatement:

            list_files[filePath].append([commitId, date, CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,\
            ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement])
            print(get_number_commits(commitId))

        # print(list_files[filePath][-1])
        # print(CyclomaticComplexity, ExcessiveClassLength, ExcessiveMethodLength,\
        #     ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, DepthOfInheritance, GotoStatement)
        # print(list_files[filePath][-1][0], CyclomaticComplexity)


# print(json.dumps(list_files, indent = 4))

csvfile1 = open(pathFolder + "/Statistique_Analyse_" + ApplicationName + '.csv', 'a', newline='')

with csvfile1:

    writer = csv.writer(csvfile1, delimiter=',')
    writer.writerow(('commitID','Date','filePath','CyclomaticComplexity','ExcessiveClassLength','ExcessiveMethodLength',\
            'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects', 'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'Commit number'))
    for path in list_files:
        for element in list_files[path]:
            # print(path,element[0],element[1])
            writer.writerow((element[0], element[1], element[2], path, element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], get_number_commits(commitId)))
csvfile1.close()



