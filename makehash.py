#!/usr/bin/env python3
"""
Functions for producing, saving and comparing file hashes:
- fhash
- savehsh
- comphsh
"""

import hashlib

def fhash(fpath, alg):
    """
    fhash function takes a file path and hashing algorithm as inputs,
    reads provided file in binary and updates the hash,
    returns the hex version of the hash.
    """
    hasher = hashlib.new(alg)
    try:
# read in binary
        with open(fpath, 'rb') as doc:
# read the file in chunks to allow for large files without affecting memory
            for chunk in iter(lambda: doc.read(4096), b""):
                hasher.update(chunk)
# handle FileNotFound and Permission errors
    except FileNotFoundError:
        print(f"File {fpath} doesn't exist.")
        return None
    except PermissionError:
        print(f"You don't have permission to access file {fpath}.")
        return None
# return hex value
    return hasher.hexdigest()

def savehsh(fpath, alg, hashdoc):
    """
    savehsh function takes a file path, hashing algorithm and hash value as inputs,
    appends to a file named hash.txt in the format fpath,alg,hashdoc.
    """
    with open('hash.txt', 'a') as f:
        f.write(f'{fpath}|{alg}|{hashdoc}\n')

def comphsh(fpath, alg, hashdoc):
    """
    comphsh function takes a file path, hashing algorithm and hash value as inputs,
    searches for match in hash.txt,
    returns results.
    """
    try:
        with open('hash.txt', 'r') as f:
            lines = f.readlines()
            last_entry = lines[-1].strip().split('|') if lines else None
            for line in lines:
                entry = line.strip().split('|')
                if entry[0] == fpath and entry[1] == alg:
                    if entry == last_entry:
                        return 1  # matches the last stored hash
                    else:
                        return 2  # matches a previously stored hash
            return None  # no hash found
    except FileNotFoundError:
        print("The hash.txt file doesn't exist.")
        return None

