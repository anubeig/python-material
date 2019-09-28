import os

with open("sample.txt","w") as f:
    pass
print os.stat("sample.txt")

"""
sh-4.3$ python main.py
posix.stat_result(st_mode=33188, st_ino=1105467552, st_dev=64770, st_nlink=1, st_uid=50018, st_gid=50018, st_size=0,
                  st_atime=1496147447, st_mtime=1496147468, st_ctime=1496147468)
"""
