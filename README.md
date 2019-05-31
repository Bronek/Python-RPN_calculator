# RPN_Python

Uses python to create a class for easier Reverse Polish Notation calculations.  
Currently only supports basic functions: add, subtract, multiply, divide, power.  

## Use
* Import this local file  
> from RPNpython import *
* Create an instance of the class RPN
  * It is possible to add parts of the stack now
> i = RPN(1, 2, 3)
  * It is possible to add more to the stack with stackadd method
    > i.stackadd(4, 5)
* Methods called act upon the last two indexes of the stack
> i.add()  
> [1, 2, 3, 9]
