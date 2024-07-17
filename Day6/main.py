#Demonstration of different Datatypes
a = 1
b = 1.1
c = complex(8, 2)
d = True
e = "Lavesh"
f = None
print(a)
print(b)
print(c)
print(d)
print(e)
print(f,'\n')

#Types of each variable
print("The Type of a is", type(a))
print("The Type of b is", type(b))
print("The Type of c is", type(c))
print("The Type of d is", type(d))
print("The Type of e is", type(e))
print("The Type of f is", type(f), '\n')

#Integers (int)
x1 = 5
x2 = -3
sum_x = x1 + x2
print("Sum of integers:", sum_x, "\n")

#Floating-Point Numbers (float)
y1 = 3.14
y2 = -0.001
result = y1 * y2 
print("Product of floating-point numbers:", result, "\n")

print("Sum of complex numbers, using same values:")
#Complex Numbers (complex)
z1 = 3 + 4j
z2 = 1 - 2j
sum_z1 = z1 + z2
print("Method 1:", sum_z1)


#Complex Numbers (complex)
z1 = complex(3, 4)
z2 = complex(1, -2)
sum_z2 = z1 + z2
print("Method 2:", sum_z2, "\n")

#Boolean
b1 = True
b2 = 3
sum_b = b2 * (1 + b1)
print("Sum using Boolean value 'True':", sum_b, "\n")

#Text Data: str
str = "Hello, World!"
uc = (str.upper())
print("The value on 0th index of string 'str':", str[0])
print("'str' in UPPERCASE:", uc, "\n")

#Sequenced Data: list, tuple
list = ['l', [1,2], [3.5], [complex(4,5)], True]
tuple = ('t', (1), (2.5,4.5), (complex(3, 6)), False) 
print("List:", list)
print("Tuple:", tuple,)
list.append(False)
print("List after appending 'False' Boolean in list:", list)
print("Item on 2nd index in the tuple:", tuple[2], "\n")

#Mapped Data: dict
programming_languages = {"HTML": "Hyper Text Markup Language", 
                         "CSS": "Cascading Sheet Style",
                         "JS": "JavaScript"}
print("Programming languages with their Full forms:", programming_languages)
print("Incorrect Full form of CSS:", programming_languages["CSS"])
programming_languages = {"CSS": "Cascading Style Sheets"}
print("Corrected Full form of CSS:", programming_languages["CSS"], "\n")

#Fixed-Point Numbers (decimal.Decimal)
from decimal import Decimal
d1 = Decimal(2.7)
d2 = Decimal(49.90)
sum_d = d1 + d2
print("Sum using Fixed-Point Numbers, showing precise and exact value:", sum_d, "\n")

#Rational Numbers (fractions.Fraction)
from fractions import Fraction
f1 = Fraction(2, 10)
f2 = Fraction(3, 10)
sum_f = f1 + f2
print("Sum using Rational Numbers, performing exact arithmentic fractions:", sum_f, "\n")

#Arbitrary-Precision Integers (int in Python)
large_num = 10**100
print("Arbitrary-Precision Integer Number:", large_num, "\n")

#NumPy Numeric Types
import numpy as np
array = np.array([1, 2, 3], dtype=np.int16)
print(array)