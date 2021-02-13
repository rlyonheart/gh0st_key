# Author Info;
# Github | rlyonheart
# Twitter | rly0nheart
# Instagram | rlyonheart

# importing required modules #
import requests
import sys
import hashlib as hash
from os import path
import os
import time
from datetime import datetime
from termcolor import colored,cprint
cprint('''
     ####                            #   #
    #    # #       #    ####  #      #  #   ####   #   #  
   #       #     #   # #      #      # #   #    #  #  # 
   #  ###  ####  #   #  ####  ###    ##    #    #   ##
   #    # #   # #   #      # #      # #   # ###       #
   #    # #   # #   #      # #      #  #  #          #
    ####  #   #   #    ####   ###   #   #  ####    ##''','red',attrs=['bold'])
inp = input('   '+os.path.dirname(os.path.realpath(__file__))+' ')



# defining the GH0ST KEY function #
def GHOST_KEY():
	# main title
	
    
	# Asking user for input(s) #
	pass_hash = input(colored('\n\t[?] Enter hash: ','white'))
	time.sleep(0.3)
	wordlist = input(colored('\t[?]Enter wordlist directory: ','white'))
	print('\n\t')
	print('\t[..][gh0st key started...] at',datetime.now())

	if path.isfile(wordlist) == False:
		# if the user specified wordlist file does not exist #
		cprint(f'\n\t[!E101] No such file found; {wordlist}','red',attrs=['bold'])
		time.sleep(0.5)
		print('\t[.][gh0st key stopped] at',datetime.now())
		quit()

	# Extracting the passwords to be tried #
	passwords = []
	wordlist = open(wordlist, 'r')
	for i in wordlist:
		text = ''
		for char in i:
			if char == '\n':
				break
			else:
				text += char
		passwords.append(text)

	# Hashing each passwords in the list objects to all the hashing algorithms to atleast match one #
	for password in passwords:
		blake2b = hash.blake2b(password.encode()).hexdigest()
		blake2s = hash.blake2s(password.encode()).hexdigest()
		md4 = hash.md4(password.encode()).hexdigest()
		md5 = hash.md5(password.encode()).hexdigest()
		sha1 = hash.sha1(password.encode()).hexdigest()
		sha224 = hash.sha224(password.encode()).hexdigest()
		sha256 = hash.sha256(password.encode()).hexdigest()
		sha384 = hash.sha384(password.encode()).hexdigest()
		sha512 = hash.sha512(password.encode()).hexdigest()

		# Checking whether any hashing algorithm cracked the password or not #
		if pass_hash == blake2s or pass_hash == blake2b or pass_hash == md5 or pass_hash == md4 or pass_hash == sha1 or pass_hash == sha256 or pass_hash == sha384 or pass_hash == sha512:

			# If any of the hashing algorithm cracks the password, loop breaks #
			time.sleep(0.3)
			cprint(f'\t[#] [hash cracked] password; {password}','green',attrs=['bold'])
			time.sleep(0.5)
			print('\t[.][gh0st key stopped] at',datetime.now())
			quit()
		else:
			cprint(f'\t[...] [retrying...] password; {password}','red',attrs=['bold'])
			
	# If the loop completes and the password is still not cracked, program returns an error message #
	cprint('\t[!E108] password not found in wordlist','white','on_red')
	time.sleep(0.5)
	print('\t[.][gh0st key stopped] at',datetime.now())
	quit()

# calling Ghost key function #
if inp == 'gh0st -h':
	if __name__ == '__main__':
		try:
			GHOST_KEY()
		except KeyboardInterrupt:
			quit()
elif 'info' in inp:
    time.sleep(1)
    cprint('''
    __PR0GRAM INF0__
    Name: Gh0st key
    Version: 5.0 - APE02
    Language: Python
    Requirements: Hashlib, Termcolor
    Supported Hashes: blake2b, blake2s, SHA1,
                      SHA224, SHA256, SHA384,
                      SHA512, MD4, MD5
                      
    __AUTH0R INF0__
    Name: eihctir
    Other Alias(es): rlyonheart
    Github: www.github.com/rlyonheart
    Twitter: www.twitter.com/rly0nheart
    Instagram: www.instagram.com/rlyonheart
    Telegram: www.t.me/eihctir''','red')

else:
	sys.exit(colored('\t[!E906] invalid input!!]\n   \t[program terminated]','red',attrs=['bold']))

                 # END ©2020 #