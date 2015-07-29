"""
Name:Santosh Reddy Kandukuri
Course:CMPS-Cryptography5363
Program: Vigenere Cipher
"""

import argparse
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", default = "inputFile.txt", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", default = "outputFile.txt", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed", default =14325107, help="Integer seed")
    args = parser.parse_args()

    seed = int(args.seed)
    f = open(args.inputFile,'r')
    message = f.read()
    keyWord=rv.keywordFromSeed(seed)
    rv.printMatrix()
    if(args.mode == 'encrypt'):
        data = rv.encryption(message,keyWord)
        o = open(args.outputFile,'w')
        o.write(data)
    else:
        
        data = rv.decryption(message,keyWord)
        o = open(args.outputFile,'w')
        o.write(data)

if __name__ == '__main__':
    main()
	
