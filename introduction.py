#INTRODUCTION
#python can be use in web development,GUI,Machine Learning
#python is interpreter,high level & oop language
#released in 1989 but java at 1995
#VARIABLE
#string in python is immutable i.e name="youtube" then name[0]='r'show error
# to use previous o/p we use underscore i.e. x=4,x+7,y=8,_ + y gives 19
# data type is not necessary to defined as int x = 3,the system itself identify data type based on value of variable
# the value of variable can be changed i.e. if we have already x= 3 then we can also assign new value to x as x=9
# we can use both single quote and double quote to defined the string as name="youtube" or name='youtube'
# the string can be print any time as 10*name gives ten time concatenated 'youtubeyoyoutubeutubeyoutubeyoutubeyoutubeyoutubeyoutubeyoutubeyoutube'
# \n denotes new line,print()is build in function to which we pass argument as print('ananta')
# the built in len(arg) is used to determine length of string
# id(name) is used to get address of name,the address is same for same data i.e. id("youtube") gives same address
# constant is defined by CAPITALIZE FORM as(PI=3.15)
# type(name) gives data types as <class 'str'>
#if a = " hello,world " then print(a.strip()) return by removing whitespaces from begging or end,print(a.replace("h","j") gives us as jellow,world,print(a.split()) split string into sub string,print(a.upper()),print(' '.join(a)) join the char in list
#LIST
# list is same as array in c/c++ but list can have different types of data i.e. name=['2',8] to add item from last name.append(arg),to remove item name.pop(),to insert particular item at particular index name.insert(index,value) also name.pop(index) ,to clear all name.clear(), to sort name.sort()
# some built in function min(name),max(name),sum(name){for number only},
#TUPLE
#tuple is immutable(value are not changeable) but reverse in list
#tuple is defined as tup=(arg1,arg2,...) access as tup[0]gives arg1
# two method index,count tup.count(arg1) gives 1
# it is used when we want list with values are not changed
#SET
#set is defined as set={23,56,89} set gives random as {56,89,23}
#DATA TYPES
#null,the variabe having assigning no value
#numric,it is of four types->int,float,complex,bool,converting normal number to complex as  complex(7,8) gives 7+8j
#sequence->list,tuple,set,string,range& range is defined as range(10) and converting range to list as list(range(10)) gives [1,2,3,.....9] for even list(range(2,10,2)) where 2->start,10->end,2->diff
#dictionary is defined as set d={"ananta":"mi","sailesh":"j2"} since keys are unique but  values may repeated,since no index so we use key for particular value as d["ananta"] 0r d.get("ananta") to get all keys/values -> d.keys()/d.values()
#OPERATORS
#arithmetic->+,-,*,%,/ to perform arithmetic operation
#assignment->=,+=,-=,*=,/=,%= to assign values to variable(0r itself also) it is also allow that a,b=3,4 gives a as 3 and b as 4
#relational-> >,>=,<,<=,==,!= to compares variables
#logical->or,and,not to combine relation
#unary->-,+,--,++ for eg n=7,n=-n gives -7
#BITWISE OPERATORS
#complement0r tilde(~) operators for eg ~12 gives -13 we have 2's complement is -ve of that number
#bitwise or,and,x-or(^) 10ds
#leftshift operator,rightshift operator
#NUMBER SYSTEM
#binary,to convert dec to bin we use as bin(decimal number) gives in binary format
#decimal->
#hexadecimal ,ip-address->to convert dec to hex we use as hex(decimal number) gives in binary format as"0x..."
#octal->to convert oct to bin we use as oct(decimal number) gives in binary format
#MATH FUNCTION
# import math(module) to find sqrt,
# floor round  to lowest int value use as print(math.floor(x)) where initially x is 3.45 gives us as 3 
# ceil round to highest int value
# import math as m allow us to use built in function such as math.sqrt(arg i.e.25) as m.sqrt(arg),pow(base_num,power_value),print(math.pi) gives values of pi lly,print(math.e)
# if we want specific built in math function in this case we do as from math import sqrt,pow or pow or sqrt only
#ARRAY
#from  array import *
#vals = array('i',[67,90,66])
#vals.reverse()
#for i in range(len(vals)):
    #print(vals[i])
from array import *
a=array('i',[67,90,56,46,23])
a.reverse()
newa =array(a.typecode,(b*b for b in a))
for i in range(len(newa)):
    print(newa[i])
from numpy import *
arr1 = array([4,6,7,8])
arr2 = arr1.copy()
for i in arr2:
    print(i)
#type code,u-> unicode_char,2 byte,i->int,2 bytes,f->float,4 bytes,'d'->double,8 bytes,signed means -VE 2 +VE values the varible can store but unsigned means +VE values only denotes as'I'
#PYCHARM
#eval(input("exp:")) is used to evaluate the exp in python such as 7-9+7 gives -9
#to take char in python we do as x=input("enter char:")[0] then print(x) will display single char
#if statement
#if-elif-else statement
#break -> to jump out of loop
#continue-> to skip satisfies condition values i.e. in for loop if i%2 == 0:then continue (in the indentation(or scope) level of continue)&print(i) in the scope of loop) skip even num in range
#pass is use to pass number in else condition which does n't satisfy if condition i.e. gives olp in else condition by skiping num satsfying if condtion
#pattern-> refer PROJECT IN PYCHARM,ALSO PYTHON_01_PATTERN
#OOP IN PYTHON
#object->instance
#class->design,attributes,methods
#encapsulation
#abstraction
#polymorphism



