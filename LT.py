"""LAST TIME."""

__author__ = "ixyz99"
__email__ = "xyzforads@gmail.com"
__telegram__ = "https://t.me/xyz99dev"

import time
import requests
import os
import subprocess
import random
import re
import long_responses as long
import helpmessage as helpC
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
BFT = "\033[1;36;40m"
wit = '\033[1;32;40m'



class title():
	print(f"\n                 LAST TIME\n")


def bomb():
	os.system('clear')

uname = input(f"\n[$] USERNAME: ")
	
		
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('...!', ['Yes', 'yes', 'YES', 'yeah', 'Yeah', 'YEAH', 'of course', 'Y','y','Ok','OK','ok'], single_response=True)
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_NAME, ['what is your name', 'you', 'name','who','are'], required_words=['who'])
    response(long.R_FUCK, ['fuck', 'you','Fuck you'], required_words=['fuck'])
    
    response(long.why(), ['why'], required_words=['why'])
    
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
def AI():
	print('AI: ' + get_response(input(f'{uname}$  ')))
	return AI()



def PLATFORM():
	PlatformX =input("""
1) [ Desktop ]
2) [ iphone / android ]""")
	if PlatformX == "1":
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		print(f"\n\nHello @{uname}")
		root = input(f"\n{BFT}┌──(LT㉿root)-[{wit}~root{BFT}]\n└─${wit} ")
		if root == 'AI':
			AI()
		if root == 'help':
			print(helpC.R_help)
		else:
			print(f'''
{root} Not Found
Write 'help' to show help message 
			''')
			PLATFORM()
		
	
	if PlatformX == "2":
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		print(f"\nHello @{uname}")
		root = input(f"\n┌──(LT㉿root)-[~root]\n└─$ ")
		if root == 'AI':
			AI()
		if root == 'help':
			print(helpC.R_help)
		else:
			print(f'''
{root} Not Found
Write 'help' to show help message 
			''')
			PLATFORM()
		
	else:
		print(f"{PlatformX} Not Found.\nYou Should Enter 1 Or 2.")
		PLATFORM()
		
def comingSoon():
	time.sleep(2)
	print(f"Coming Soon...")
	

if __name__ == "__main__":
	title(),PLATFORM()
