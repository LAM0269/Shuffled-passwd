#coding: utf8
"""
The aim of this program is to creat lists of passwords based on combinasons of given words.
The programme can works line by line with words seprate by a ':' or use the hole file.
"""

from sys import path
from Shuffle import *

import argparse
import os

debug = 0

def dir_path(path):
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError(path)

def argsProgram ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",type=dir_path, help="Path to file containing word list.", required = True)
    parser.add_argument("-o", "--output",type=dir_path, help="Output name of file.", required = False)
    args = parser.parse_args()
    return (args.input,args.output)

def read_input(file_path):
    try :
        with open(file_path,'r') as l:
            return [i.replace('\n','') for i in l.readlines()]
    except :
        print('[+] File cannot be found or open.')
        return 0

def write_output (out_path,return_list):
    try :
        if not os.path.isfile(out_path) :
            f = open(out_path,'x')
        else :
            f = open(out_path,'w')

        [f.write(i+'\n') for i in return_list]
        f.close()
        print('\n[+] File successfully written.')
    except :
        print("\n[+] Can't write or creat output file.")

if __name__ == "__main__" :
    if debug == 1 :
        file_path = r'list.txt'
        out_path = r'./out.txt'
        input_list = read_input(file_path)
    else :
        args = argsProgram()
        input_list = read_input(args[0])
    

    if input_list :
        MyList = shuffle (input_list)
        print('\n[+] Generated passwords :\n')
        [print(i) for i in MyList.return_list]

        if debug == 0 :
            if args[1] :
                write_output(args[1],MyList.return_list)
        else :
            write_output(out_path,MyList.return_list)