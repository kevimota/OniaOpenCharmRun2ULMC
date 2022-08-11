#!/usr/bin/env python3

import subprocess, os, re
from pprint import pprint

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

processing = 'CRAB_PrivateMC'
dataset = 'UpsilonPt9To30ToMuMuDstarToD0piPtHat9_2018'
crab_folder = '220804_191624'
n_folders = 2

cmds = [ 
   f'xrdfs xrootd-redir.ultralight.org ls -u /store/group/uerj/kmotaama/{processing}/{dataset}/{crab_folder}/{i:04}/' for i in range(n_folders)
]
print("Following commands will be used!")
pprint(cmds)

cat = ""
out_file = dataset + ".txt"
for i in cmds:
    os.system(f"{i} > {i.split('/')[-2]}")
    cat += f" {i.split('/')[-2]}"

os.system(f"cat {cat} > {out_file}")
os.system(f"rm -rf {cat}")
file_list = open(out_file, 'r').readlines()

for idx, f in enumerate(file_list):
   file_list[idx] = re.sub('transfer-\d*', 'xrootd-redir', f)

list(set(file_list))
file_list.sort(key=natural_keys)

final_list = []
for i in file_list:
    if i not in final_list:
        final_list.append(i)

print(f"Saving to {out_file}")

with open(out_file, 'w') as f:
    for i in final_list:
        f.write(i)