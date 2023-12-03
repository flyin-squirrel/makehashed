#!/usr/bin/env python3
"""
Cmd line interface for producing, saving and comparing file hash values.
"""

import argparse
import hashlib
from makehash import fhash, savehsh, comphsh

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
    parser = argparse.ArgumentParser(
    description='Makes file hashes.')
    
    parser.add_argument('fpath', 
    type=str, 
    help='Path to your target file.')
    
    parser.add_argument('alg', 
    type=str, 
    choices=hashlib.algorithms_available, 
    help='Your desired hashing algorithm.')

# make options mutually exclusive to avoid conflict  
    group = parser.add_mutually_exclusive_group()

# add option to save   
    group.add_argument('-s', '--save', 
    action='store_true', 
    help='Save hash to hash.txt')

# option to compare
    group.add_argument('-c', '--compare', 
    action='store_true', 
    help='Compare hash with hash currently in hash.txt')
    
    args = parser.parse_args()
    
# call fhash, incl. fpath and alg
    hashdoc = fhash(args.fpath, args.alg)
    
# print hash
    print(f'The {args.alg} hash of your file is: {hashdoc}')
    
# save hash
    if args.save:
        savehsh(args.fpath, args.alg, hashdoc)
        print(f'Hash was saved to hash.txt')
        
# compare hash
    if args.compare:
        result = comphsh(args.fpath, args.alg, hashdoc)
        if result is None:
            print(f'No hash found for {args.fpath}.')
        elif result == 1:
            print(f'This hash matches the last stored hash in hash.txt.')
        elif result == 2:
            print(f'This hash matches a previously stored hash in hash.txt.')
        else:
            print(f'This hash differs from all previously stored hashes.')

if __name__ == "__main__":
    main()
