# Makehashed

Python module which allows you to generate file hash values using the hashlib library, save them and compare them.

## Usage

This module is used from the command line like this:

	python hashed.py <fpath> <alg> [-s | -c]

Where:
	<fpath> is the path to your target file.
	<alg> is the hash algorithm you'd like to use. 
	-s or --save is optional, stores the hash in a file named hash.txt
	-c or --compare is optional, compares the hash with the stored hashes in hash.txt

Note: The -s and -c options are mutually exclusive. Only one can be used at a time.

Example:
	python hashed.py path/to/yourfile.txt sha256
		
		This will print the SHA256 hash of yourfile.txt to std out.

Example:
	python hashed.py path/to/yourfile.txt sha256 -s

		This will print the SHA256 hash of the file yourfile.txt and save it to hash.txt.

Example:
	python hashed.py path/to/yourfile.txt sha256 -c

		This will print the SHA256 hash of the file yourfile.txt and compare it with the existing hashes in hash.txt.
	
Supported algorithms:
	sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256, blake2b, blake2s, md5.

