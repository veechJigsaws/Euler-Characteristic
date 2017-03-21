import numpy as np

# This function takes two inputs, which are determined by the variance defined 
# in the random_jig function, and returns a random number within the variance
def rando(start,end):
    return np.random.uniform(start,end)
    
# This is a function that takes two inputs, a point (can be list or tuple) and
# an angle theta, which is also calculated in random_jig
def rotate(x,y):
    return([x[0]*np.cos(y)-x[1]*np.sin(y),x[0]*np.sin(y)+x[1]*np.cos(y)])

# This function takes 5 inputs, the start position, end position, and the 
# variance, which determines the amount of randomness in the jigsaw
def random_jig(xstart,ystart,xend,yend,variance):
    import numpy as np    
    list1=[]
    list1.append('M'+str(xstart)+','+str(ystart))
    pi=np.pi
    thesvg=''
    L=np.sqrt((xstart-xend)**2+(ystart-yend)**2)
    v1,v2=-variance,variance
    xvar=xend-xstart
    yvar=yend-ystart    
    theta=np.arctan(yvar/xvar)  
    svg=np.zeros((18,2)) 
    pointlist=[(L/4+L/16*rando(v1,v2),0),(3*L/8+L/16*rando(v1,v2),L/8+L/16*rando(v1,v2)),(5*L/16+L/32*rando(v1,v2),2*L/8+L/32*rando(v1,v2)),(8*L/16+3*L/64*rando(v1,v2),5*L/16+L/64*rando(v1,v2)),(11*L/16+3*L/64,4*L/16+L/64*rando(v1,v2)),(10*L/16+L/64*rando(v1,v2),L/8+L/32*rando(v1,v2)),(12*L/16+L/32*rando(v1,v2),0),(L,0)]    
    slopelist=[0,pi/2,9*pi/16+pi/16*rando(v1,v2),0+pi/16*rando(v1,v2),-9*pi/16+pi/16*rando(v1,v2),-pi/2,0,0]
    for i in range(len(pointlist)):
        phi=slopelist[i]        
        if i==0:
            svg[i+1]=pointlist[i]
            svg[i+2]=[pointlist[i][0]/2,pointlist[i][1]/2]
            svg[i+3]=pointlist[i]
            continue
        else:
            svg[2*i+2]=[pointlist[i][0]-L/16*np.cos(phi),pointlist[i][1]-L/16*np.sin(phi)]
            svg[2*i+3]=pointlist[i]
    count=0    
    for i in svg:
        svg[count]=rotate(i,theta)       
        svg[count]=[svg[count][0]+xstart,svg[count][1]+ystart]
        count+=1
    
    thesvg=''
    count=0    
    for i in svg:
        if count==0:
            thesvg+='M'+str(i[0])+','+str(i[1])
            count+=1
            continue
        if count==1:
            thesvg+=' C'+str(i[0])+','+str(i[1])+' '
            count+=1
            continue
        if count!=0 and count!=2 and count%2==0:
            thesvg+='S'+str(i[0])+','+str(i[1])+' '
            count+=1
            continue
        else:
            thesvg+=str(i[0])+','+str(i[1])+' '
            count+=1
            continue

    return(thesvg)

print(random_jig(0,0,100,100,1))