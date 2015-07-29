import random

    
symbols= """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
T = [[0 for i in range(len(symbols))] for i in range(len(symbols))]
key = ""
msg = ""
ctext = ""

def printMatrix():
        i = 0
        j = 0
        k = 0
        line = ""
        for i in range(95*95):
            line = line + T[j][k]
            j = j+1
            if j >= 95:
                print(line)
                line = ""
                j = 0
                k = k+1

def keywordFromSeed(seed):
        Letters = []

        while seed > 0:
            Letters.insert(0,chr((seed % 100) % 26 + 65))
            seed = seed // 100
        key = "".join(Letters)
        buildVigenere(seed)
        return key
 
def buildVigenere(seed):
        random.seed(seed)
        temp = list(symbols)
        random.shuffle(temp)
        temp = ''.join(temp)

        for sym in temp:
            random.seed(seed)
            myList = []
            for i in range(len(temp)):
                r = random.randrange(len(temp))
                if r not in myList:
                    myList.append(r)
                else:
                    while(r in myList):
                        r = random.randrange(len(temp))
                    myList.append(r)
                while(T[i][r] != 0):
                    r = (r + 1) % len(temp)
                T[i][r] = sym

def encryption(msg,key):
        ctext=""
        for i in range(len(msg)):
            b = i
            a = i % len(key)
            ctext = ctext + eVal(msg,key,a,b)
        return ctext

def eVal(msg,key,a,b):       
        i = ord(msg[b]) - 32
        j = ord(key[a]) - 32
        return T[i][j]
  
def decryption(msg,key):
        ctext = ""
        for i in range(len(msg)):
            b = i
            a = i % len(key)
            ctext = ctext + dVal(msg,key,a,b)
        return ctext

def dVal(msg,key,a,b):
        n = len(symbols)
        r = ord(key[a]) - 32
        for i in range(n):
            if T[i][r] == msg[b]:
                decChar = chr(i + 32)
                return(decChar)
