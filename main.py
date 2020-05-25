
from pydriller import RepositoryMining
import subprocess

import json
import os

import csv
import shutil

import subprocess
import shutil
import os
import stat
from os import path
import patoolib

from pyunpack import Archive


ApplicationName = "phpunit"
pathFolder = "C:\Project\statiqueProject"
pathRepositories = pathFolder + "/repositories"
pathDirectory = pathRepositories + '/' + ApplicationName

os.chdir(pathRepositories)


Projet_GIT_URL = "https://github.com/laravel/laravel"

# subprocess.check_output("git clone " + Projet_GIT_URL , shell=True)


# REMOVE REPO
try:
    for root, dirs, files in os.walk(pathDirectory):
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    shutil.rmtree(pathDirectory)
    # END REMOVE REPO
except:
    print("An exception occurred at removing the repo")


# patoolib.extract_archive("foo_bar.rar", outdir="path here")

Archive(pathRepositories + '/' + ApplicationName + '.zip').extractall(pathRepositories)

os.chdir(pathFolder)



f = open(pathFolder + '/config_' + ApplicationName +'.json')

json_file = json.load(f)
# print(json_file)

if not json_file['name']:

    row = 2
    Files = []
    start_commit = json_file['first_commit']
    numberCommit = 0
    firstCommit = json_file['first_commit']
    csvfile = open(pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName  + ".csv", 'w', newline='')

    with csvfile:

        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(('Commit id', 'Date', 'filename',
                        'CyclomaticComplexity', 'ExcessiveClassLength',
                        'ExcessiveMethodLength', 'ExcessiveParameterList', 'NPathComplexity', 'CouplingBetweenObjects',
                        'EmptyCatchBlock', 'DepthOfInheritance', 'GotoStatement', 'author'))
    csvfile.close()

    with open(pathFolder + "/" + ApplicationName + "/commitHistoy_" + ApplicationName + ".csv", 'w', newline='') as commitFile:
        writer = csv.writer(commitFile, delimiter=',')

        writer.writerow(('commitID', 'Date'))
    commitFile.close()
else:
    row = json_file['row']
    start_commit = json_file['commit']
    Files = json_file['files']
    numberCommit = json_file['numberCommit']
    firstCommit = json_file['first_commit']

f.close()






def smell_cmd(commit, row, commit_date):
    try:
        # phpmd C:\Project\statiqueProject\myRuleset.xml text C:\Project\statiqueProject\myRuleset.xml
        out = subprocess.check_output("phpmd " + pathDirectory + " json " + pathFolder + "/myRuleset.xml ", shell=True)

        result_dict = json.loads(out)
        # print(result_dict)

        date_time = commit_date.strftime("%m/%d/%Y, %H:%M:%S")

        copy_files = Files.copy()
        # print('Files:', len(result_dict['files']))

        for file in result_dict['files'].split("\\\\", 5)[-1:][0]:

            if file['file'] not in Files:
                Files.append(file['file'])
            else:
                copy_files.remove(file['file'])


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

            csvfile1 = open(pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + '.csv', 'a', newline='')

            with csvfile1:

                writer = csv.writer(csvfile1, delimiter=',')

                writer.writerow((commit, date_time, file['file'],
                                 CyclomaticComplexity, ExcessiveClassLength,
                                 ExcessiveMethodLength, ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects,
                                 EmptyCatchBlock, DepthOfInheritance, GotoStatement))
            csvfile1.close()


            row += 1

        for elemet_file in copy_files:
            row += 1
            csvfile1 = open(pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + '.csv', 'a', newline='')

            with csvfile1:
                writer = csv.writer(csvfile1, delimiter=',')
                writer.writerow((commit, date_time, elemet_file, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            csvfile1.close()
    except subprocess.CalledProcessError as e:
        print(e.output)
        print("out")




        # print(Files)
        # print(copy_files)

    return row


count = 0


os.chdir(pathDirectory)
for commit in RepositoryMining(pathDirectory, from_commit=start_commit, only_in_branch="master", only_releases=True,
                               only_modifications_with_file_types=[".php"])\
                                    .traverse_commits():
    count += 1
    print("Commit :", count)

    if numberCommit == 0:
        firstCommit = commit.hash

    cmd_Checkout = "git checkout " + commit.hash + " -f"
    # print(cmd_Checkout)
    # print('CLEAN')
    # os.system("git reset --hard")
    subprocess.check_output(cmd_Checkout, shell=True)
    # os.system(cmd_Checkout)
    print("start")

    json_file = {
        'name': pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + ".csv",
        'row': row,
        'commit': commit.hash,
        'first_commit': firstCommit,
        'files': Files,
        'numberCommit': numberCommit
    }

    with open(pathFolder + '/config_' + ApplicationName +'.json', 'w') as gg:
        # print(json_file)
        gg.seek(0)
        json.dump(json_file, gg)

    row = smell_cmd(commit.hash, row, commit.committer_date)
    numberCommit += 1
    json_file = {
        'name': pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + ".csv",
        'row': row,
        'commit': commit.hash,
        'first_commit': firstCommit,
        'files': Files,
        'numberCommit': numberCommit
    }
    with open(pathFolder + '/config_' + ApplicationName + '.json', 'w') as gg:
        print(json_file)
        gg.seek(0)
        json.dump(json_file, gg)

    f = open(pathFolder + '/config_' + ApplicationName +'.json')
    json_file = json.load(f)
    # print(json_file)
    f.close()

    with open(pathFolder + "/" + ApplicationName + "/commitHistoy_" + ApplicationName  + ".csv", 'a', newline='') as commitFile:

        writer = csv.writer(commitFile, delimiter=',')

        writer.writerow((commit.hash, commit.committer_date, commit.in_main_branch, commit.branches, commit.parents))
    commitFile.close()
    #
    # cmd_reset_checkout = "git reset --hard HEAD"
    #
    # subprocess.check_output(cmd_reset_checkout, shell=True)

print("Closed")

f = open(pathFolder + '/config_' + ApplicationName +'.json')
json_file = json.load(f)
print(json_file["row"])
f.close()
