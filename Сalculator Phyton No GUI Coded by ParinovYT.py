pf = print #
f = float #

pf ('Сalculator Phyton No GUI Coded by ParinovYT')
c1 = int (input('Enter the number 1: '))
c2 = int (input('Enter the number 2: '))
c3 = int (input('Select the operation --- 1 + / 2 - / 3 : / 4 * ---'))

if c3 == 1: r = c1 + c2
if c3 == 2: r = c1 - c2
if c3 == 3: r = f(c1 / c2)
if c3 == 4: r = c1 * c2
print ('Result = ',r)
