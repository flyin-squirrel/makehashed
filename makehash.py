#!/usr/bin/env python3
"""
Functions for producing, saving and comparing file hashes:
- fhash
- savehsh
- comphsh
"""
# import haslib module
import hashlib

# Please note: Blackbox AI was used to troubleshoot and build parts of this module.
# Specifically:
# comphsh function's ability to compare the current hash value "hashdoc" to previously
# stored hash values and return results 1 or 2 which are then passed to hashed.py. 
# The idea to iterate the file "fpath" in chucks of 4096 bytes to ease memory use.
#
# Comments have been added to show functionality of each line in this module with special
# emphasis placed on explaining the parts I had help with.

# define fhash function; args fpath and alg needed
def fhash(fpath, alg):
    """
    fhash function takes a file path and hashing algorithm as inputs,
    reads provided file in binary and updates the hash,
    returns the hex version of the hash.
    """
# new() function of hashlib creates new hash object and passes it to var 'hasher'
    hasher = hashlib.new(alg)
# start a try block
    try:
# with open() opens the file for reading while allowing it to be auto closed,
# read in binary 'rb' used, update() needs bytes so this is required, doc is
# arbitrary name that file will be referenced as inside with block. 
        with open(fpath, 'rb') as doc:
# read the file in chunks to allow for large files without affecting memory
# for loop started with chunk var, iter() func uses lambda func to read 'doc'
# 4096 bytes at a time and stops when it finds an empty byte string (b"") which
# indicates the end of the file 
            for chunk in iter(lambda: doc.read(4096), b""):
# passes the 4096 byte 'chunk' to 'hasher' for each loop, creating a binary
# representation of the file stored in 'hasher'
                hasher.update(chunk)
# handle FileNotFound and Permission errors

# start except block, handle a FileNotFoundError, related print statement,
# None returned and passed to main()
    except FileNotFoundError:
        print(f"File {fpath} doesn't exist.")
        return None
# start except block, handle PermissionError, related print statement,
# None returned and passed to main()
    except PermissionError:
        print(f"You don't have permission to access file {fpath}.")
        return None
# return hex value of stored binary data currently in 'hasher' using hexdigest() method,
# passed to main()
    return hasher.hexdigest()
# define savehsh function; args fpath, alg and hashdoc (the var where main stores result
# of fhash) required
def savehsh(fpath, alg, hashdoc):
    """
    savehsh function takes a file path, hashing algorithm and hash value as inputs,
    appends to a file named hash.txt in the format fpath,alg,hashdoc.
    """
# with open opens or creates and opens hash.txt and tells it to append, 'a', refers to
# file as 'f' in this block.
    with open('hash.txt', 'a') as f:
# write (append) vars fpath, alg, hashdoc to file 'f'(hash.txt) seperated by pipes
        f.write(f'{fpath}|{alg}|{hashdoc}\n')
# define comphsh function; vars fpath, alg and hashdoc needed
def comphsh(fpath, alg, hashdoc):
    """
    comphsh function takes a file path, hashing algorithm and hash value as inputs,
    searches for match in hash.txt,
    returns results.
    """
# start try block
    try:
# with open opens hash.txt in read mode, 'r', refers to it as 'f' in this block
# with open will not create hash.txt in this func like savehsh does, see except below 
        with open('hash.txt', 'r') as f:
# readlines() reads 'f' (hash.txt) and stores a list of strings for each line in 'lines'
            lines = f.readlines()
# grabs the last line from hash.txt (lines[-1]), removes spaces(strip()), and splits
# split() at pipes ('|'), storing the list of str in var last_entry, if hash.txt empty
# returns None 
            last_entry = lines[-1].strip().split('|') if lines else None
# initiates for loop that will loop over each line in 'lines'
            for line in lines:
# for each line in 'lines', removes spaces(strip()), and splits split() at pipes ('|'),
# storing the list of str in var entry
                entry = line.strip().split('|')
# if the first element of 'entry' matches current fpath var and the second matches the
# alg var, continue
                if entry[0] == fpath and entry[1] == alg:
# if the current hash checked with -c matches the last stored hash in hash.txt, then
                    if entry == last_entry:
# return 1, passed to main() as 'result'
                        return 1  # matches the last stored hash
# otherwise it matches one line checked but it wasn't the last
                    else:
# return 2, passed to main() as 'result'
                        return 2  # matches a previously stored hash
# otherwise it didn't match any lines checked, return None, passed to main() as 'result'
            return None  # no hash found
# start except block, handle a FileNotFoundError, related print statement,
# None returned and passed to main()
    except FileNotFoundError:
        print("The hash.txt file doesn't exist.")
        return None

