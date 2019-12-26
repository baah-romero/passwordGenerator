'''
Fichero que contiene las funciones generales usadas
en todos los ficheros de python desarrollados por:
    [*] Author: @baah-romero
'''
import random

def newPassword(): #Función que define el número de caracteres de la password
    nchars=input(str("Cuantos chars debe tener la password (8 mínimo): "))
    nchars=int(nchars)
    try:
        if nchars >= 8:
            return nchars
    except:
        print(f'\033[1;33m[!] Error 01.01 \033[1;37m -> El número de caractéres para la contraseña debe ser mínimo de 8.')
        newPassword()

def newChars(): #Función que genera unnúmero aleatorio para escoger diccionario
    opts=random.randint(1,4)
    return opts

def ndict1(): #Función que genera número para letra
    opts=random.randint(1,26)
    return opts

def ndict2(): #Función que genera número para letra
    opts=random.randint(1,30)
    return opts

def charToPass(a): #Función para obtener carácter de un diccionario
    try:
        if a==1:#Retrona mayúsculas
            try:
                dict1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                try:
                    ndicVal=ndict1()
                except:
                    print(f'\033[1;33m[!] Error 02.021 \033[1;37m -> Fallo al ejecturar nDict1() para obtener número aleatorio.')
                #print(dict1[ndicVal])
                charToPa=dict1[ndicVal]
                return charToPa
            except:
                print(f'\033[1;33m[!] Error 02.02 \033[1;37m -> Fallo al generar MAYÚSCULAS para la contraseña.')
        if a==2:#Retrona números
            try:
                charToPa=random.randint(0,9)
                return charToPa
            except:
                print(f'\033[1;33m[!] Error 02.03 \033[1;37m -> Fallo al generar un número para la contraseña.')
        if a==3:#Retrona minúsculas
            try:
                dict2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                try:
                    ndicVal=ndict1()
                except:
                    print(f'\033[1;33m[!] Error 02.041 \033[1;37m -> Fallo al ejecturar nDict1() para obtener número aleatorio.')
                charToPa=dict2[ndicVal]
                return charToPa
            except:
                print(f'\033[1;33m[!] Error 02.04 \033[1;37m -> Fallo al generar MINÚSCULAS para la contraseña.')
        if a==4:#Retrona carácteres
            try:
                dict3=['\'','*','+','-','_',',','.',':',';','/','\\','=','?','!','|','@','#','~','$','€','&','(',')','{','}','[',']','^','<','>']
                try:
                    ndicVal=ndict2()
                except:
                    print(f'\033[1;33m[!] Error 02.051 \033[1;37m -> Fallo al ejecturar nDict2() para obtener número aleatorio.')
                charToPa=dict3[ndicVal]
                return charToPa
            except:
                print(f'\033[1;33m[!] Error 02.05 \033[1;37m -> Fallo al generar CHAR para la contraseña.')
    except:
        print(f'\033[1;33m[!] Error 02.01 \033[1;37m -> Fallo al obtener carácter del diccionario.')

def endPrinter(a): #Función para mostrar por pantalla la contraseña generada
    print('|---------------------------------------------------------------|')
    print(f'|\t\033[1;34m Password: \033[1;37m {a}')
    print('|---------------------------------------------------------------|')
