#!/usr/bin/python

import os
import sys
import shutil

rootdir = sys.argv[1]
enhance_times = 1

if __name__ == '__main__':
    for folder, subs, files in os.walk(rootdir):
        if len(subs) == 0:
            file_counts = len(files)
            for full_filename in files:
                temp = full_filename.split(".")
                filename = temp[0]
                ext = temp[1]
                temp = filename.split("_")
                prefix = temp[0]
                idx = int(temp[1])
                source = os.path.join(folder, full_filename)

                for _ in range(enhance_times):
                    idx += file_counts
                    output_full_filename = prefix + "_" + "{:04d}".format(idx) + "." + ext
                    print output_full_filename
                    destination = os.path.join(folder, output_full_filename)
                    shutil.copyfile(source, destination)
