x1 = 5
y1 = 8
x2 = 9
y2 = 11

dy = y2-y1
dx = x2-x1

d= 2*dy - dx

a=2*dy
b = -2*dx

i = 0
while x1!=x2 and y1!=y2:
    dir = None
    if d>0:
        dir = "NE"
        x1+=1
        y1+=1
    else:
        dir = "E"
        x1+=1
    
    print(dir,i,d,x1,y1)
    if d>0:
        d = d+a+b
    else:
        d = d+a
    
    