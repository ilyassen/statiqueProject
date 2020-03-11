
from pydriller import RepositoryMining
import subprocess

import re
import json
import os

import xlsxwriter

import shutil

ApplicationName = "vmoex-framework"

os.chdir("D:/Projects/exportMSR/CommitLooper/repositories")

subprocess.check_output("git clone " + "https://github.com/yeskn-studio/vmoex-framework" , shell=True)

os.chdir("D:/Projects/AnalysteProject")

workbook = xlsxwriter.Workbook("D:/Projects/AnalysteProject/" + ApplicationName + "/Analyse.xlsx")
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Commit id')
worksheet.write('B1', 'Date')
worksheet.write('C1', 'filename')
worksheet.write('D1', 'CyclomaticComplexity')
worksheet.write('E1', 'ExcessiveClassLength')
worksheet.write('F1', 'ExcessiveMethodLength')
worksheet.write('G1', 'ExcessiveParameterList')
worksheet.write('H1', 'NPathComplexity')
worksheet.write('I1', 'CouplingBetweenObjects')
worksheet.write('J1', 'EmptyCatchBlock')
worksheet.write('K1', 'DepthOfInheritance')
worksheet.write('L1', 'GotoStatement')


Files = []

row = 1


def smell_cmd(commit, row, commit_date):
    try:
        out = subprocess.check_output("phpmd " + pathDirectory + " json D:/Projects/AnalysteProject/myRuleset.xml ", shell=True)
    except subprocess.CalledProcessError as e:
        out = e.output

    result_dict = json.loads(out)
    print(result_dict)

    copy_files = Files.copy()
    print('Files:', len(result_dict['files']))
    for file in result_dict['files']:
        # print(file)

        if file['file'] not in Files:
            Files.append(file['file'])
            for elem in Files:
                print(elem)
        else:
            copy_files.remove(file['file'])
            # list(filter((file['file']).__ne__, copy_files))


        NPathComplexity = 0
        CyclomaticComplexity = 0
        ExcessiveClassLength = 0
        ExcessiveMethodLength =0
        ExcessiveParameterList = 0
        CouplingBetweenObjects = 0
        EmptyCatchBlock = 0
        DepthOfInheritance = 0
        GotoStatement = 0

        for violation in file['violations']:
            # print("classe :", violation['class'])
            # print("Description :", violation['description'])
            # print("rule :", violation['rule'])


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

        print('CodeSmells Complexite', CyclomaticComplexity)

        date_time = commit_date.strftime("%m/%d/%Y, %H:%M:%S")

        # write operation perform

        worksheet.write(row, 0, commit)
        worksheet.write(row, 1, date_time)
        worksheet.write(row, 2, file['file'])
        worksheet.write(row, 3, CyclomaticComplexity)
        worksheet.write(row, 4, ExcessiveClassLength)
        worksheet.write(row, 5, ExcessiveMethodLength)
        worksheet.write(row, 6, ExcessiveParameterList)
        worksheet.write(row, 7, NPathComplexity)
        worksheet.write(row, 8, CouplingBetweenObjects)
        worksheet.write(row, 9, EmptyCatchBlock)
        worksheet.write(row, 10, DepthOfInheritance)
        worksheet.write(row, 11, GotoStatement)



        # incrementing the value of row by one
        # with each iteratons.
        row += 1

    for elemet_file in copy_files:
        worksheet.write(row, 0, commit)
        worksheet.write(row, 1, date_time)
        worksheet.write(row, 2, elemet_file)
        worksheet.write(row, 3, 0)
        worksheet.write(row, 4, 0)
        worksheet.write(row, 5, 0)
        worksheet.write(row, 6, 0)
        worksheet.write(row, 7, 0)
        worksheet.write(row, 8, 0)
        worksheet.write(row, 9, 0)
        worksheet.write(row, 10, 0)
        worksheet.write(row, 11, 0)
        row += 1

    return row



pathDirectory = "D:/Projects/exportMSR/CommitLooper/repositories/" + ApplicationName
# try:
#     os.mkdir("D:/Projects/AnalysteProject/" + ApplicationName)
# except:
#     print("Creation of the directory %s failed" )
os.chdir(pathDirectory)
# print(RepositoryMining(pathDirectory).__sizeof__())
count = 0
for commit in RepositoryMining(pathDirectory).traverse_commits():
    count = count + 1
    print("Commit :",count)
    # print(commit.hash)
    # cmd_Checkout = "git checkout " + commit.hash +" &&  git submodule foreach --recursive git reset --hard && git submodule update --init --recursive"
    
    cmd_Checkout = "git checkout " + commit.hash
    # cmd_Checkout = "git checkout " + commit.hash
    # print(cmd_Checkout)
    os.system(cmd_Checkout)
    # res = subprocess.call([cmd_Checkout])
    # print(res)

    # proc = subprocess.Popen(["phpmd " + pathDirectory + " text codesize"], stdout=subprocess.PIPE, shell=True)
    # (out, err) = proc.communicate()

    row = smell_cmd(commit.hash, row, commit.committer_date)


    # if count == 30:
    #     break



    # try:
    #     output = subprocess.check_output("phpmd " + pathDirectory + " text codesize ", shell=True)
    # except subprocess.CalledProcessError as e:
    #     output = e.output
    # try:
    #     os.mkdir("D:/Projects/AnalysteProject/" + ApplicationName + "/commit_" + commit.hash)
    #     print("Successfully created the directory %s ")
    # except OSError:
    #     print("Creation of the directory %s failed" )
    # else:
    #
    #     os.chdir("D:/Projects/AnalysteProject/" + ApplicationName + "/commit_" + commit.hash)
    #     f = open("Analyse.txt","wb")
    #     f.write(output)
    #     f.close()
    #     os.chdir(pathDirectory)
    #
    #     f = open("D:/Projects/AnalysteProject/" + ApplicationName + "/commit_" + commit.hash + "/Analyse.txt","r")
    #     Lines = f.readlines()
    #     count = 0
    #     # Strips the newline character
    #     for line in Lines:
    #         # print(line.strip())
    #
    #         result = re.search('(.*)%s' % '.php:', line.__str__())
    #         print(result.group(1))

workbook.close()
print("Closed")

# shutil.rmtree(pathDirectory)
# os.listdir()
# os.removedirs()

# print(commit.hash)
    # res = os.system("phpmd " + pathDirectory + " text codesize")
    # print(res)
