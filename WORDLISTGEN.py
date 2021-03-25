#!/usr/bin/env python3
#github.com/intrackeable
#Simple wordlist generator USER:PASSWORD format
from colorama import Fore

global green, red 
green = Fore.GREEN
red = Fore.RED

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
        file.close()

def main():
    try:
        print('{}Welcome to WORDLISTGEN, a simply program to make wordlist in USER:PASS format!'.format(green))
        users = input('Select a file with users: ')
        passwords = input('Select a file with passwords: ')
        wordlist = input('Insert a name for new wordlist: ')
        if (users == '' or passwords == '' or wordlist == ''):
            print('{}INVALID DATA, TRY IT AGAIN!'.format(red))
            exit()
        else:
            user_list = open_file(users)
            pass_list = open_file(passwords)
            generate_wordlist(user_list,pass_list,wordlist)
    except KeyboardInterrupt:
        print('{}CLOSING PROGRAM'.format(red))

if __name__ == '__main__':
    main()

