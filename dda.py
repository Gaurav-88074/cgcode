x1 = 2
y1 = 3
x2 = 12
y2 = 8

slope = (y2-y1)/(x2-x1)
print("slope is:",slope)
while x1!=x2 and y1!=y2:
    print(x1,y1,x1+1,y1+slope)
    x1+=1
    y1+=slope

