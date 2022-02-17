import turtle


z=turtle.Turtle()
#Koch method will draw koch curve .
def koch(t,l):
 angle1=60
 angle=120
 if l>3 :
  koch(t,l/3)
  t.lt(angle1)
  koch(t,l/3)
  t.rt(angle)
  koch(t,l/3)
  t.lt(angle1)
  koch(t,l/3)
 else :
  t.fd(l)
#Taking input.
n=int(input("Enter a natural number")) 
#Collataz Conjecture for generating random number (More Fun!).      
while int(n)!=1:
 if(n%2==0):
  z.lt(60)
  z.color("green") #color
  n=n/2
  koch(z,n)
            
 else:
  z.lt(120)
  z.color("red") #color
  n=(3*n+1)/2
  koch(z,n)
#End
turtle.mainloop()
