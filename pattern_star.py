#left-lower triangle
for i in range(1,6):
    print(i*"*")
print()
#right-upper triangle
for i in range(1,6):
    print(i*" ",(6-i)*"*")

#left-upper triangle
for i in range(5,0,-1):
    print(i*"*")
#right-lower triangle
for i in range(1,6):
    print((5-i)*" ",i*"*")
'''
============== RESTART: F:\PYTHON\Assignsments\pattern_star.py ==============
*
**
***
****
*****

  *****
   ****
    ***
     **
      *
*****
****
***
**
*
     *
    **
   ***
  ****
 *****
'''


