"""
usage: remove the last 4 characters from each data file
"""
import os
import sys
import shutil

def strip_ms_file_names():
    file_path = os.getcwd()
    file_names = os.listdir(file_path)

    folder_names = []

    for f in file_names:
        n = f.split('_')
        folder_names.append({'original': f, 'new': n[1] + '.raw'})

    for folder in folder_names:
        old_name = os.path.join(file_path, folder['original'])
        new_name = os.path.join(file_path, folder['new'])
        shutil.move(old_name, new_name)
        print 'Renamed MS data file %s to %s in %s ' % (folder['original'], folder['new'], file_path)

    return