#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

# import module of file Banner.py
import Banner as Banner

OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def bomb():
	# os.system('clear') # Console-terminal
	os.system('cls') # cmd
	print (OKGREEN + '''
			 \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: Mazen Elzanaty
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''' + ENDC)

# os.system('clear') # Console-terminal
os.system('cls') # cmd 
try:
	Banner.Banner()
except IOError:
	print('Banner File not found')

#Input
print(WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + '--------------------------------------------------------------' + ENDC)
try:
	server = input(OKGREEN + 'Mail Server:' + ENDC)
	user = input(OKGREEN + 'Your Email: ' + ENDC)
	pwd = getpass.getpass(OKGREEN + 'Password: ' + ENDC)
	to = input(OKGREEN + 'To: ' + ENDC)
	subject = input(OKGREEN + 'Subject (Optional): ' + ENDC)
	body = input(OKGREEN + 'Message: ' + ENDC)
	nomes = int(input(OKGREEN + 'Number of Emails to send: ' + ENDC))
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print (FAIL + '\nCanceled' + ENDC)
	sys.exit()

# Gmail
# Only can send messages since account Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials)
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + ENDC)
		sys.exit()
	while no < nomes:
		try:
			server.sendmail(user, to, message)
			print(WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(FAIL + '\nCanceled' + ENDC)
			sys.exit()
		except:
			print("Failed to Send ")
			no == nomes
	server.close()
	
# Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print( WARNING + '''Your Username or Password is incorrect, please try again using the correct credentials)
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + ENDC)
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(FAIL + '\nCanceled'+ ENDC)
			sys.exit()
		except:
			print("Failed to Send")
			no == nomes
	server.close()
	
#Hotmail/Outlook
# Only can send messages since account outlook/Gmail
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	bomb()
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + ENDC)
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(FAIL + '\nCanceled' + ENDC)
			sys.exit()
		except:
			print("Failed to Send ")
			no = nomes
	server.close()
else:
	print('Works only with Gmail, Yahoo, Outlook and Hotmail.')
	sys.exit()