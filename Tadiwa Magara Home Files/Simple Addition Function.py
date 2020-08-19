
'''
create a function for adding two variables. It will be needed to calculate p=y+z
'''
def calculateP( y , z ) :
        return int( y ) + int( z )

'''
create a function for multiplying two variables. It will be needed to calculate p=y+z
'''
def calculateResult( x, p ) :
        return int( x ) * int( p )

#Now this is the beginning of main program
x = input('x: ')
y = input('y: ')
z = input('z: ')

#Now Calculate <strong>p</strong>
p = calculateP ( y , z )

#Now calculate <strong>result</strong>
result = calculateResult( x , p )

#Print the result
print(result)
