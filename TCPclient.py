#Immportojme librarine per socket komunikim
import socket
import sys

serverName = '127.0.0.1'    #formati i IP: 127.0.0.1
serverPort = 14000

pergj = input("A deshironi te perdorni emer dhe port te serverit te ndryshem nga default(127.0.0.1 - 14000)? ")
if pergj == "po" or pergj == "Po" or pergj == "PO":
    serverName = input("Shkruani emrin(IP adresen) e serverit: ")
    serverPort = input("Shkruani portin e serverit: ")

while True:
    try:
        soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print ("Error creating socket: %s" %e)
        soketi.close()
        sys.exit(1)

    try:
        soketi.connect((serverName,serverPort))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" %e)
        soketi.close()
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" %e)
        soketi.close()
        sys.exit(1)


    kerkesa = input("Jeni lidhur me serverin, Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, NDERRO_SISTEMIN_NUMERIK, NUMERO_FJALET)?: ")

    try:
        #dergojme kerkesen tek serveri (ne kete rast localhost me portin 1400)
        soketi.sendall(str.encode(kerkesa)) #default encoding=utf-8
    except socket.error as e:
        print("Error sending data: %s" %e)
        soketi.close()
        sys.exit(1)

    #duhet te presim....
    mesazhi = ''
        #unaze e pafundme
    while True:
        try:
            data = soketi.recv(4)
        except socket.error as e:
            print("Error receiving data: %s" %e)
            soketi.close()
            sys.exit(1)

        if len(data) <= 0:
            break

        mesazhi += data.decode("utf-8")

    print("Pergjigjja nga serveri: ", mesazhi)

    soketi.close()

#socket komandat e perdorura - connect, close, sendall, recv