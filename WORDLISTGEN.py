#!/usr/bin/env python3
#github.com/intrackeable
#Simple wordlist generator USER:PASSWORD format
import pyfiglet
import os
from colorama import Fore, Style

global green, red, blue 
green = Fore.GREEN
red = Fore.RED
blue = Fore.CYAN + Style.BRIGHT

def open_file(file_list):
    with open (file_list,'r') as file:
        credentials = file.read().split('\n')
    credentials = [x for x in credentials if x != '']
    return credentials

def generate_wordlist(user_list,pass_list,wordlist):
    for i in user_list:
        for x in pass_list:
            generate_file(i,x,wordlist)

def generate_file(user,password,wordlist):
    with open(wordlist,'a') as file:
        file.write(user + ':' + password + '\n')

def display_banner():
    os.system('clear')
    draw = pyfiglet.figlet_format('WORDLISTGEN',font='bubble')
    print(blue + draw)
    print('{}Welcome to WORDLISTGEN, a simply program to make wordlist in USER:PASS format!'.format(green))

def main():
    try:
        display_banner()
        users = input('USERS FILE: ')
        passwords = input('PASSWORDS FILE: ')
        wordlist = input('WORDLIST NAME: ')
        if (users == '' or passwords == '' or wordlist == ''):
            print('{}INVALID DATA, TRY IT AGAIN!'.format(red))
            exit()
        else:
            user_list = open_file(users)
            pass_list = open_file(passwords)
            generate_wordlist(user_list,pass_list,wordlist)
    except KeyboardInterrupt:
        print('\n{}CLOSING PROGRAM'.format(red))

if __name__ == '__main__':
    main()

