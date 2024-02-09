import math


class Fraction:
    def __init__(self, numerator=0, denominator=0) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        fraction_1, fraction_2 = self.denominator_of_Kashtrak(other)
        sum_numerator = fraction_1.numerator + fraction_2.numerator
        sum_denominator = fraction_1.denominator
        new_fraction = Fraction(sum_numerator, sum_denominator)
        return new_fraction

    def __sub__(self, other):
        fraction_1, fraction_2 = self.denominator_of_Kashtrak(other)
        sub_numerator = fraction_1.numerator - fraction_2.numerator
        sub_denominator = fraction_1.denominator
        new_fraction = Fraction(sub_numerator, sub_denominator)
        return new_fraction

    def __mul__(self, other):
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        new_fraction = Fraction(mul_numerator, mul_denominator)
        return new_fraction

    def __truediv__(self, other):
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        new_fraction = Fraction(div_numerator, div_denominator)
        return new_fraction
    
    def denominator_of_Kashtrak(self, other):
        if self.denominator != other.denominator:
            fraction_1 = Fraction()
            fraction_2 = Fraction()
            fraction_1.denominator = self.denominator * other.denominator
            fraction_2.denominator = self.denominator * other.denominator
            fraction_1.numerator = self.numerator * other.denominator
            fraction_2.numerator = other.numerator * self.denominator
            return fraction_1, fraction_2
        else:
            return self, other
        
    def get_number(self):
        return self.numerator / self.denominator
    
    def simplify_the_fraction(self):
        num = math.gcd(self.numerator, self.denominator)
        if num == 1: 
            return self
        else:
            return Fraction(self.numerator / num, self.denominator / num)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    

fraction_1 = Fraction(2, 2)
fraction_2 = Fraction(2, 4)
print(fraction_1)
print(fraction_2)

sum_fraction = fraction_1 + fraction_2
sub_fraction = fraction_1 - fraction_2
mul_fraction = fraction_1 * fraction_2
div_fraction = fraction_1 / fraction_2

print(f'sum: {sum_fraction}')
print(f'sub: {sub_fraction}')
print(f'mul: {mul_fraction}')
print(f'div: {div_fraction}')


print(sum_fraction.simplify_the_fraction())