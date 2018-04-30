import glob
import os
import shutil

filelist = glob.glob("puyofuData/*")
files = [x.split('_')[0] if ("_" in x) is True else x.replace(".txt", "") for x in filelist]
dirname = list(set(files))
[os.makedirs(x, exist_ok=True) for x in dirname]
for d in dirname:
    for f in filelist:
        if (d in f) is True:
            shutil.move(f, d)
