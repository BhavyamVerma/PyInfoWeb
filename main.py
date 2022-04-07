import os
import subprocess
from bs4 import BeautifulSoup
import requests
import ipinfo
import socket
from colorama import Fore, Back
import random
import socket
import string
import sys
import threading
import time


class Pyinfoweb():
    def __init__(self):
        self.command = input(Fore.LIGHTBLUE_EX + "[+] Enter your command: ")
        if self.command == "website":
            print("")
            self.website_information()
        
        elif self.command == "help":
            print(Fore.GREEN + """type 'website' to get website information.
type 'download' to download the internet files.
type 'quit' to quit.
type 'help' for help""")
            Pyinfoweb()
        
        elif self.command == "download":
            self.downloadfile()
        
        elif self.command == "ddos":
            self.ddos_attack()
        
        elif self.command == "":
            print(Fore.GREEN+"[+] Invalid command")
            return Pyinfoweb()
    
    def downloadfile(self):
        try:
            print("")
            self.url = input(Fore.GREEN + "[+] Enter url:")
            self.local_filename = self.url.split('/')[-1]
            self.r = requests.get(self.url)
            self.f = open(self.local_filename, 'wb')
            for self.chunk in self.r.iter_content(chunk_size = 512 * 1024): 
                if self.chunk:
                    self.f.write(self.chunk)
            self.f.close()
            print(Fore.CYAN + "[+] File successfully downloaded.")
            print("")
            return Pyinfoweb()
        except:
            print(Fore.RED + "[+] Please try again later!")
            print("")
            return Pyinfoweb()

    def website_information(self):
        try:
            self.website = input(Fore.GREEN + "[+] Enter url of website: ")
            if self.website == "exit":
                print("")
                Pyinfoweb()
            self.r = requests.get(f"https://www.wmtips.com/tools/info/s/{self.website}")
            self.soup = BeautifulSoup(self.r.text, "html.parser")
            self.information = self.soup.find_all("p")[0].get_text()
            self.information2 = self.soup.find_all("p")[1].get_text()
            print(self.information, self.information2)

            try:
                self.new = self.website.replace("https://", "")
                self.new2 = self.new.replace("http://", "")
                self.new3 = self.new2.replace("/", "")
                self.new4 = self.new3.replace("://", "")
                self.new5 = self.new4.replace("www.", "")
                self.ip = socket.gethostbyname(self.new5)
                print(Fore.GREEN + f"[+] IPaddress of {self.new5}: ", self.ip)
            except:
                print(Fore.RED + "[+] Oops something went wrong! Try again.")
        
            handler = ipinfo.getHandler("e33ffe7402286f")
            self.d = handler.getDetails(self.ip)
            print("                                     ")
            print(Fore.GREEN + "[+] ip: ", self.d.details['ip'])
            print(Fore.GREEN + "[+] hostname: ", self.d.details['hostname'])
            print(Fore.GREEN + "[+] city: ", self.d.details['city'])
            print(Fore.GREEN + "[+] region: ", self.d.details['region'])
            print(Fore.GREEN + "[+] country: ", self.d.details['country'])
            print(Fore.GREEN + "[+] latitude: ", self.d.details['latitude'])
            print(Fore.GREEN + "[+] longitude: ", self.d.details['longitude'])
            print("                                            ")
            return Pyinfoweb()
        
        except:
            print(Fore.RED + "[+] Try Again!")
            print("")
            return Pyinfoweb()
    
    def ddos_attack(self):
        try:
            self.hostname = input(Fore.GREEN+"Enter the website: ")
            self.port = input(Fore.GREEN+"Enter the port: ")
            self.attacks = input(Fore.GREEN+"Enter the number of attacks: ")
            self.result = subprocess.getoutput(['python', 'pyflooder.py', f"{self.hostname}", f"{self.port}", f"{self.attacks}"])
            print (f"[#] Attack started on {self.hostname}) || Port: {str(self.port)} || # Requests: {str(self.attacks)}")
            return Pyinfoweb()
        except:
            return Pyinfoweb()

s = Pyinfoweb()
