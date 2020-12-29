## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


# # Let us print the files in the directory in which you are running this script
# print(os.listdir("."))
#
# # Let us check if this file is indeed a file!
# print(os.path.isfile("./ex.py"))
#
# # Does the file end with .py?
# print("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return find_files_recursive(suffix, path, [])


def find_files_recursive(suffix, path, out_list=[]):
    try:
        if os.path.isfile(path):
            if path.endswith(suffix):
                out_list.append(path)
        else:
            files = os.listdir(path)
            for item in files:
                complete_path = os.path.join(path, item)
                find_files_recursive(suffix, complete_path, out_list, )
        if out_list:
            return out_list
        return "No file found for the given extension"
    except Exception as e:
        return e


print(find_files(".c", "./testdir"))
print(find_files(".c", "./invalid_folder"))
print(find_files(".unkownextension", "./testdir"))
path = "./testdir/t1.c"
suffix = ".c"
print(find_files(suffix, path, ))
