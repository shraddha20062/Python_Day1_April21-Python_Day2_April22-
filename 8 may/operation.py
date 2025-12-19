
#approch 1 by adding import module name
import calculator

calculator.add(10,20)
calculator.mul(20,10)

#approch2 from module name import function1 and Function2
from calculator import add,mul

add(1,2)
mul(10,20)

#approch 3 from module name import* [its represent all function name]

from calculator import*
add(69,2)
mul(8,9)

