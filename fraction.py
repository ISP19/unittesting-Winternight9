import math
from math import gcd 


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        #check numerator and denominator type
        if type(numerator) is not int: 
            raise TypeError
        
        elif type(denominator) is not int: 
            raise TypeError

        #if input is 0/0 raise ValueError if it 1/0 or -1/0 give it infinity value by using mathematical function.
        if denominator ==0:
            if numerator == 0:
                self.numerator = 0
                self.denominator = 0

            elif numerator > 0:
                self.numerator = 1
                self.denominator = 0
            
            elif numerator < 0:
                self.numerator = -1
                self.denominator = 0 
               
        else:
            #check if input in form 5/-6 change it to -5/6 and check if both negative than turn the two signs into a plus sign
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)

            elif numerator > 0 and denominator < 0:
                numerator = -numerator
                denominator = abs(denominator)
                    
            self.gcd = gcd(numerator, denominator)
            self.numerator = int(numerator/self.gcd)
            self.denominator = int(denominator/self.gcd)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if not isinstance(frac,Fraction):
            return False
        else:    
            new_nume = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
            new_deno = self.denominator * frac.denominator 
            return Fraction(new_nume,new_deno)

    def __mul__(self, frac):
        #a/b * c/d = a*c/b*d
        if not isinstance(frac,Fraction):
            return False
        else:    
            return Fraction(self.numerator * frac.numerator,self.denominator * frac.denominator)

    def __sub__(self, frac):
        #a/b - c/d = (ad-bc)/(b*d)
        if not isinstance(frac,Fraction):
            return False
        else:    
            new_nume = (self.numerator * frac.denominator) - (frac.numerator * self.denominator)
            new_deno = self.denominator * frac.denominator 
            return Fraction(new_nume,new_deno)

    def __gt__(self, frac):
        #a/b > c/d = a*d > c*b 
        if not isinstance(frac,Fraction):
            return False
        else:
            return (self.numerator * frac.denominator) > (frac.numerator * self.denominator) 

    def __neg__(self):
        #a/b ==> -a/b
        return Fraction(-self.numerator,self.denominator)

    def __pow__(self,frac):
        #(a/b)**c/d   
        if not isinstance(frac,Fraction):
            return False 
        return Fraction(int(self.numerator) ** int(frac.numerator/frac.denominator),int(self.denominator) ** int(frac.numerator/frac.denominator))


    def __ge__(self,frac):
        #a/b >= c/d = a*d >= c*b 
        if not isinstance(frac,Fraction):
            return False
        else:
            return (self.numerator * frac.denominator) >= (frac.numerator * self.denominator)

    def __truediv__(self,frac):
        #(a/b) / (c/d)) = a*d / b*c 
        if not isinstance(frac,Fraction):
            return False   
        else:
            return Fraction(self.numerator * frac.denominator,self.denominator * frac.numerator)        

    def __str__(self):
        #output if it can divide we will show it number but if it 
        if self.numerator % self.denominator == 0:
            return f"{int(self.numerator/self.denominator)}"   
        else:
            return f"{int(self.numerator)}/{int(self.denominator)}"    

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
