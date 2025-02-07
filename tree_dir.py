import os
from os.path import join, isdir
import sys

STICK='┃'
DIR_TO='┣'
DIR_END='┗'
FILE_TO='┠'
FILE_END='┖'

def srt(els:list[str], path:str)->list[str]:
    dirs = sorted(filter(lambda d: isdir(join(path, d)), els))
    files = sorted(filter(lambda d: not isdir(join(path, d)), els))
    if WITH_FILES:
        return dirs+files
    return dirs

def set_stick(sticks:str):
    if not sticks:
        return ""
    st = sticks[-1]
    new_st= " " if st == DIR_END or st == FILE_END else STICK
    return sticks[:-1] + new_st

def tree(path: str, sticks:str=""):
    cur_dir=os.path.split(path)[1]
    print(sticks+cur_dir)
    sticks = set_stick(sticks)
    
    try:
        els=srt(os.listdir(path), path)
    except PermissionError:
        return
        
    for n, el in enumerate(els):
        if el.startswith(".") and not ALL:
            continue 
        p=os.path.join(path, el)
        if os.path.isdir(p):
            stk= DIR_TO if n+1 != len(els) else DIR_END
            tree(p, sticks+stk)
        else:
            stk= FILE_TO if n+1 != len(els) else FILE_END
            print(sticks+stk+el)
    
WITH_FILES =True
ALL = False

if not sys.argv[1:]:
    cur_path=os.getcwd()
else:
    sp=sys.argv
    
    if "-d" in sp:
        WITH_FILES = False
        sp.remove("-d")
    if "-a" in sp:
        ALL = True
        sp.remove("-a")
        
    if sp:
        cur_path=sp[1]
        if not os.path.exists(cur_path):
            print("error path:", cur_path)
            exit()
        if not os.path.split(cur_path)[1]:
            cur_path=cur_path[:-1]
    else:
        cur_path=os.getcwd()
#cur_path = ""

tree(cur_path)
