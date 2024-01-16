#!/usr/bin/env python3
"""
Cmd line interface for producing, saving and comparing file hash values.
"""
# imports argparse module
import argparse
# imports haslib module 
import hashlib
# imports the three functions defined in makehash.py
from makehash import fhash, savehsh, comphsh
# defines main function, entry point for the module
def main():
    """
    main function sets up argparse, 
    parses the cmd-line args,
    calls fhash function from makehash with fpath and alg,
    prints hash to std out, 
    saves hash with -s option, 
    or compares hash with -c option.
    """

# argparse

# var parser is given new ArgumentParser object
    parser = argparse.ArgumentParser(
# describes help for this, probably uneeded but I was paranoid and it works so it stayed
    description='Makes file hashes.')
# use argparse's add_argument method to add argument fpath as a string, describes help 
    parser.add_argument('fpath', 
    type=str, 
    help='Path to your target file.')
# use argparse's add_argument method to add argument alg as a string, describes help  
    parser.add_argument('alg', 
    type=str,
# alg arg has to be a recognized hashlib algorithm. list is defined in README.md
    choices=hashlib.algorithms_available, 
    help='Your desired hashing algorithm.')

# make options mutually exclusive to avoid conflict by adding group 'group'
    group = parser.add_mutually_exclusive_group()

# add option to save to group 'group' with add_argument method, describes help
    group.add_argument('-s', '--save',
# if save option is used, value stored as 'True'
    action='store_true', 
    help='Save hash to hash.txt')

# option to compare added to 'group' with add_argument method, store as 'True' if 
# present, describe help
    group.add_argument('-c', '--compare', 
    action='store_true', 
    help='Compare hash with hash currently in hash.txt')
# parses arguments passed to script by user, passes them to 'args' as args.alg and
# args.fpath, and if chosen one of args.save or args.compare
    args = parser.parse_args()
    
# call fhash function, incl. fpath and alg args, store as 'hashdoc'
    hashdoc = fhash(args.fpath, args.alg)
    
# print hash with alg used to hash it
    print(f'The {args.alg} hash of your file is: {hashdoc}')
    
# if save option was used, call savehsh function using fpath, alg and result
# of fhash as 'hashdoc', print result saved 
    if args.save:
        savehsh(args.fpath, args.alg, hashdoc)
        print(f'Hash was saved to hash.txt')
        
# if compare option was used 
    if args.compare:
# call comphsh function with args fpath, alg and results of fhash as 'hasdoc',
# store as 'result'
        result = comphsh(args.fpath, args.alg, hashdoc)
# comphash result was 'None' meaning there are either no lines in the file to check, 
# the file does not exist, matches were found or permission is denied. ambiguous print
# statement provided to cover all four potentials, but fhash and comphsh will inform 
# the user if file doesn't exist or permission is denied. 
        if result is None:
            print(f'No hash found for {args.fpath}.')
# comphsh returned 1, meaning the hash checked has the same fpath, alg, and hash as the 
# last stored hash in hash.txt, print statement
        elif result == 1:
            print(f'This hash matches the last stored hash in hash.txt.')
# comphsh returned 2, meaning the hash checked has the same fpath, alg, and hash as any 
# of the other stored hashes in hash.txt that aren't the last one, print statement
        elif result == 2:
            print(f'This hash matches a previously stored hash in hash.txt.')
# comphsh didn't return 1, 2 or None so the hash didn't match any stored hashes in
# hashes.txt, print statement
        else:
            print(f'This hash differs from all previously stored hashes.')
# common line in python modules, makes sure this only runs when run directly 
if __name__ == "__main__":
# calls main function
    main()
