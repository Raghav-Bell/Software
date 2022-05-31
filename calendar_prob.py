from datetime import date
def oddTable(n):   #Maping odd days
 d= dict()
 d[0] ="Sunday"
 d[1] ="Monday"
 d[2] ="Tuesday"
 d[3] ="Wednesday"
 d[4] ="Thursday"
 d[5] ="Friday"
 d[6] ="Saturday"
 return d[n]

def isLeap(y):                #Checking if year is leap
 if y%4==0 and y%100!=0:
  return True
 elif y%400==0:
   return True
 return False

def sol(delta ,y):
 count=0
 for _ in range(y):
  if isLeap(_): #counting leap years
   count+=1
 return oddTable((366*count+365*(y-count-1)+delta)%7)  #Calculating odd days & checking oddtable

y,m,d = map(int,input().split()) # input as year ,month , day
delta=date(y,m,d)-date(y,1,1) #difference b/w 1st jan of the year and given date
print(sol(int(delta.days),y))
