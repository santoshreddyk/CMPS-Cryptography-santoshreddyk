
#Name:Santosh Reddy Kandukuri
#Course:CMPS-Cryptography5363
#Program: Elipticl curve


import argparse
import sys
import main as my
import fractions as fract

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()

    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    a = fract.Fraction(args.a)
    b = fract.Fraction(args.b)
    x1= fract.Fraction(args.x1)
    x2= fract.Fraction(args.x2)
    y1= fract.Fraction(args.y1)
    y2= fract.Fraction(args.y2)
    
	#slope eauation
   
    if (y1**2) == (x1**3) + (a*x1) + b and (y2**2) == (x2**3) + (a*x2) + b:
        print(" The given points  lie on the curve")
    else:
        print(" The given points does't lie on the curve")    
    
    if x1 == x2:
        m = (3*x1**2+a)/(2*y1)
    else:
        m = (y1-y2)/(x1-x2)
    
   #to caluculate the point values x3 and y3
    x3 = fract.Fraction((m**2) - x1 - x2).limit_denominator(1000)
    y3 = fract.Fraction(y1 + m * (x3-x1)).limit_denominator(1000)
    print(x3,y3)
    my.plotcurve(m,a,b,x1,y1,x2,y2,x3,y3)


if __name__ == '__main__':
    main()