from sys import argv
import os
import shutil
import sys
import fileinput

script_name = argv[0]
project_name = argv[1]


print "\nThe project name: %s" % project_name
print "os.name is : %s " % os.name
print "the home directory is: %s " % os.environ['HOME']
print "current directory is: %s" % os.getcwd()
print "current process is: %s\n\n" % os.getpid()



folder_name = os.getcwd() + "/" + project_name
skeleton = os.getcwd() + "/skeleton"

def rename_project():
    print "Making folder at %s " % folder_name
    shutil.copytree(skeleton, folder_name)
    rename_NAME_folder()
    rename_NAME_tests()
    replaceAll(folder_name + "/setup.py", 'NAME', project_name)
    replaceAll(folder_name + "/tests/" + project_name + "_tests.py", 'NAME', project_name)

def rename_NAME_folder():
    Name = folder_name + "/NAME"
    New = folder_name + "/" + project_name
    shutil.copytree(Name, New)
    shutil.rmtree(Name)

def rename_NAME_tests():
    old = folder_name + "/tests/NAME_tests.py"
    new = folder_name + "/tests/" + project_name + "_tests.py"
    os.rename(old, new)

def replaceAll( file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace = 1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

if os.path.isdir(folder_name):
    print "Folder already exists. Would you like to erase? Press enter to not erase : "
    erase = raw_input()
    if erase:
        shutil.rmtree(folder_name)
        rename_project()

else:
    rename_project()
