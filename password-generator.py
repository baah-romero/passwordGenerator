'''
    [*] Author: @baah-romero
'''
import modules.usualFunctions

def main():
    password,chars="",0
    chars=modules.usualFunctions.newPassword()
    chars=int(chars)
    while chars>0:
        nc=modules.usualFunctions.newChars()#Carácter para diccionario
        charNew=modules.usualFunctions.charToPass(nc)#Char para password
        charNew=str(charNew)
        password=password+charNew#Añadir char a password
        chars-=1#-1 en las vueltas de while.
    modules.usualFunctions.endPrinter(password)

if __name__=="__main__":
    main()
