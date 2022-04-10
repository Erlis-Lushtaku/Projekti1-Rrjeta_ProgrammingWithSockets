#Kodimi i nje server aplikacioni me sockets.
#importojme librarite e nevojshme
import socket
import datetime
import random
import math
import sys
from _thread import *

def IP(adresa):
    return "IP Adresa e klientit është: " + adresa[0]

def NRPORTIT(adresa):
    return "Klienti është duke përdorur portin: " + str(adresa[1])

def NUMERO(fjalet):
    vowels = 0
    consonants = 0

    for fjala in fjalet:
        for i in fjala.lower():
            if(i == 'a' or i == 'e' or i == 'ë' or i == 'i' or i == 'o' or i == 'u' or i == 'y'):
                vowels = vowels + 1
            elif i.isalpha():                   # kontrollon nese eshte shkronje
                consonants = consonants + 1

    return "Teksti i pranuar përmban " + str(vowels) + " zanore dhe " + str(consonants) + " bashkëtingëllore"

def ANASJELLTAS(fjalet):
    rezultati = ""
    i = len(fjalet) - 1
    while i >= 0:
        rezultati += fjalet[i][::-1]
        rezultati += " "
        i = i - 1

    return rezultati[:-1]

def PALINDROM(fjalet):
    stringu = ""
    for fjala in fjalet:
        stringu += fjala
        stringu += " "

    if(stringu[:-1].lower() == ANASJELLTAS(fjalet).lower()):
        return "Teksti i dhene eshte palindrome"
    else:
        return "Teksti i dhene nuk eshte palindrome"

def KOHA():
    d = datetime.datetime.now()
    return d.strftime("%d.%m.%Y %I:%M:%S %p")

def LOJA():
    randomList = random.sample(range(1, 36), 5)
    randomList.sort()
    return str(randomList)

def GCF(a, b):
    return str(math.gcd(int(a), int(b)))

def KONVERTO(opcioni, numri):
    if (opcioni == "cmNeInch"):
        return str(numri * 0.393701)
    elif (opcioni == "inchNeCm"):
        return str(numri * 2.54)
    elif (opcioni == "kmNeMiles"):
        return str(numri * 0.621371)
    elif (opcioni == "mileNeKm"):
        return str(numri * 1.60934)

def dec_to_bin(x):
    x = int(x)
    return bin(x)[2:]

def bin_to_dec(x):
    return int(x, 2)

def dec_to_oct(x):
    x = int(x)
    return oct(x)[2:]

def oct_to_dec(x):
    return int(x, 8)

def dec_to_hex(x):
    x = int(x)
    return hex(x)[2:].upper()

def hex_to_dec(x):
    return int(x, 16)

def NDERRO_SISTEMIN_NUMERIK(from_, to_, x):

    if from_ == "10":
        if to_ == "2":
            return str(dec_to_bin(x))
        elif to_ == "8":
            return str(dec_to_oct(x))
        elif to_ == "16":
            return str(dec_to_hex(x))
    elif from_ == "2":
        if to_ == "10":
            return str(bin_to_dec(x))
        elif to_ == "8":
            return str(dec_to_oct(bin_to_dec(x)))
        elif to_ == "16":
            return str(dec_to_hex(bin_to_dec(x)))
    elif from_ == "8":
        if to_ == "2":
            return str(dec_to_bin(oct_to_dec(x)))
        elif to_ == "10":
            return str(oct_to_dec(x))
        elif to_ == "16":
            return str(dec_to_hex(oct_to_dec(x)))
    elif from_ == "16":
        if to_ == "2":
            return str(dec_to_bin(hex_to_dec(x)))
        elif to_ == "8":
            return str(dec_to_oct(hex_to_dec(x)))
        elif to_ == "10":
            return str(hex_to_dec(x))

def NUMERO_FJALET(fjalet):

    numruesi = {}
    for fjala in fjalet:
        fjala = fjala.replace(',', '')
        fjala = fjala.replace('.', '')
        if fjala in numruesi:
            numruesi[fjala] += 1
        else:
            numruesi[fjala] = 1

    return "Numri i fjaleve ne tekst: " + str(numruesi)

def client_thread(clientS, address):
    try:
        kerkesa = clientS.recv(128)           
    except socket.error as e:
        print("Error receiving request from client: %s" %e)
        clientS.close()
        return

    print('Kerkesa nga klienti: ' + str(kerkesa.decode('utf-8')))

    kerkesaS = str(kerkesa.decode('utf-8')).split()
    #e procesojme kerkesen e klientit
    pergjigjja = ''

    if kerkesaS[0] == 'IP':
        pergjigjja = IP(address)
    elif kerkesaS[0] == 'NRPORTIT':
        pergjigjja = NRPORTIT(address)
    elif kerkesaS[0] == 'NUMERO':
        if len(kerkesaS) < 2:
            pergjigjja = "Duhet te shkruani nje argument(tekst)"
        else:
            pergjigjja = NUMERO(kerkesaS[1:])
    elif kerkesaS[0] == 'ANASJELLTAS':
        if len(kerkesaS) < 2:
            pergjigjja = "Duhet te shkruani nje argument(tekst)"
        else:
            pergjigjja = ANASJELLTAS(kerkesaS[1:])
    elif kerkesaS[0] == 'PALINDROM':
        if len(kerkesaS) < 2:
            pergjigjja = "Duhet te shkruani nje argument(tekst)"
        else:
            pergjigjja = PALINDROM(kerkesaS[1:])
    elif kerkesaS[0] == 'KOHA':
        pergjigjja = KOHA()
    elif kerkesaS[0] == 'LOJA':
        pergjigjja = LOJA()
    elif kerkesaS[0] == 'GCF':
        if len(kerkesaS) < 3:
            pergjigjja = "Duhet te shkruani dy argumente(numra te plote)"
        else:
            pergjigjja = GCF(kerkesaS[1], kerkesaS[2])
    elif kerkesaS[0] == 'KONVERTO':
        if len(kerkesaS) < 3:
            pergjigjja = "Duhet te shkruani dy argument"
        else:
            pergjigjja = KONVERTO(kerkesaS[1], float(kerkesaS[2]))
    elif kerkesaS[0] == 'NDERRO_SISTEMIN_NUMERIK':
        if len(kerkesaS) < 4:
            pergjigjja = "Duhet te shkruani tri argumente"
        else:
            pergjigjja = NDERRO_SISTEMIN_NUMERIK(kerkesaS[1], kerkesaS[2], kerkesaS[3])
    elif kerkesaS[0] == 'NUMERO_FJALET':
        if len(kerkesaS) < 2:
            pergjigjja = "Duhet te shkruani nje argument(tekst)"
        else:
            pergjigjja = NUMERO_FJALET(kerkesaS[1:])
    else:
        pergjigjja = "Kerkese jovalide"
          
    print('Pergjigjja nga server: ' + pergjigjja)
    clientS.sendall(str.encode(pergjigjja)) 
    clientS.close()

serverName = ''
serverPort = 14000

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverS.bind((serverName, serverPort))
except socket.error as e:
    print("Error binding: %s" %e)
    serverS.close()
    sys.exit(1)

print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort))

serverS.listen(5)

print('Server eshte duke punuar dhe eshte duke pritur per ndonje kerkese!')

while True:
    clientS, address = serverS.accept()
    print('----------------------------------------')
    print('Klienti eshte lidhur me server %s ne portin %s ' %address)

    start_new_thread(client_thread, (clientS, address,))

serverS.close()