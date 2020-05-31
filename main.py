
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

from dataBase import db

from pyunpack import Archive



def commit_files(commit):
    dictFiles = {"modifiedFiles": [],
                 "addedFiles": [],
                 "removedFiles": []
                 }

    for m in commit.modifications:
        # if m.change_type.name != 'DELETE':
        #     print(m.change_type.name)

        filename, file_extension = os.path.splitext(m.filename)
        if file_extension == '.php':
            if m.change_type.name == "RENAME":
                dictFiles['modifiedFiles'].append({
                    'old_path': m.old_path,
                    'new_path': m.new_path
                })
            elif m.change_type.name == "ADD" or "MODIFY":
                dictFiles['addedFiles'] = {
                    'new_path': m.new_path
                }
            elif m.change_type.name == "DELETE":
                dictFiles['removedFiles'] = {
                    'old_path': m.old_path
                }
        # elif m.change_type.name == "MODIFY":
        #     print("Modified")

    return dictFiles



ApplicationName = "laravel"
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
    countfile = 0
    db.reset_table()
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
    Files = db.get_filenames()
    numberCommit = json_file['numberCommit']
    firstCommit = json_file['first_commit']
    countfile = json_file['countfile']

f.close()


def get_index_simalirity():
    cmd = "git diff [<options>] <commit> [--] [<path>…​]"
    out = subprocess.getoutput("phpmd " + pathDirectory + " json " + pathFolder + "/myRuleset.xml ")


def smell_cmd(commit, row, commit_date):
    global countfile
    try:
        # phpmd C:\Project\statiqueProject text C:\Project\statiqueProject\myRuleset.xml
        # out = subprocess.check_output("phpmd " + pathDirectory + " json " + pathFolder + "/myRuleset.xml ", shell=True)
        # out = subprocess.run(['phpmd', pathDirectory, 'json', 'C:/Project/statiqueProject/myRuleset.xml'], stdout=subprocess.PIPE)
        out = subprocess.getoutput("phpmd " + pathDirectory + " json " + pathFolder + "/myRuleset.xml --ignore-violations-on-exi")
        print(out)
        result_dict = json.loads(out)


        date_time = commit_date.strftime("%m/%d/%Y, %H:%M:%S")

        removed_files = db.get_filenames()
        # print('Files:', len(result_dict['files']))

        dict_commit_files = commit_files(commit)
        db_files = db.get_filepaths()

        for file in result_dict['files']:
            # filename = '/'.join(file['file'].rsplit('\\', 2)[-2:])
            filename = file['file'].replace('C:\\Project\\statiqueProject\\Repositories\\' + ApplicationName + '\\', '')

            for element_dict in dict_commit_files['modifiedFiles']:
                if element_dict['old_path'] == filename:
                    db.modify_line(filename, element_dict['old_path'])

            if filename not in db_files:
                countfile += 1
                # New file or changed path.
                db.add_line("file_ " + str(countfile), filename)
                Files.append(filename)
            else:
                element_remove = db.get_filename(filename)
                removed_files.remove(element_remove)



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

                writer.writerow((commit.hash, date_time, db.get_filenames(filename),
                                 CyclomaticComplexity, ExcessiveClassLength,
                                 ExcessiveMethodLength, ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects,
                                 EmptyCatchBlock, DepthOfInheritance, GotoStatement))
            csvfile1.close()


            row += 1

        for elemet_file in removed_files:
            row += 1
            csvfile1 = open(pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + '.csv', 'a', newline='')

            with csvfile1:
                writer = csv.writer(csvfile1, delimiter=',')
                writer.writerow((commit.hash, date_time, elemet_file, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            csvfile1.close()
    except subprocess.CalledProcessError as e:
        print(e.output)
        print("out ERROR")




        # print(Files)
        # print(copy_files)

    return row


count = 0


os.chdir(pathDirectory)
print("Commit start : ", start_commit)
for commit in RepositoryMining(pathDirectory, from_commit=start_commit, only_in_branch="master",
                               only_modifications_with_file_types=[".php"])\
                                    .traverse_commits():

    # print(commit_files(commit))

    count += 1
    print("Commit :", count)
    print("HASH : ", commit.hash)

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
        'numberCommit': numberCommit,
        'countfile': countfile
    }

    with open(pathFolder + '/config_' + ApplicationName +'.json', 'w') as gg:
        # print(json_file)
        gg.seek(0)
        json.dump(json_file, gg)

    row = smell_cmd(commit, row, commit.committer_date)
    numberCommit += 1
    json_file = {
        'name': pathFolder + "/" + ApplicationName + "/Analyse_" + ApplicationName + ".csv",
        'row': row,
        'commit': commit.hash,
        'first_commit': firstCommit,
        'files': Files,
        'numberCommit': numberCommit,
        'countfile': countfile
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
