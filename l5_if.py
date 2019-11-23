#5. If  Statements
#==================================
#Python Flow Control
#===========================
#Python if...else
#The if…elif…else statement is used in Python for decision making.

#Python if Statement Syntax
#if test expression:
#	statement(s)

#Python if...elif...else Statement
#Syntax of if...elif...else
#if test expression:
#	Body of if
#elif test expression:
#	Body of elif
#else: 
#	Body of else

x = 50
y=15

if x>y :
    # print('{} is greater than {}'.format(x,y))
    print('%s is greater than %s' % (x,y))
else:
    print('{} is smaller than {}'.format(x,y))
			

val =12
if val % 2 ==0:
    print('{} is even number'.format(val))
else:
    print('{} is odd number'.format(val))
