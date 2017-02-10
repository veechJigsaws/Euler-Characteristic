###############################################################################
# This function takes an input of a list describing which sides are glued
# together, and another list describing the location of each square, and which 
# square it is (number of square, xcenter coordinate, ycenter coordinate). This
# function will then return a graph of the identification diagram, its number 
# vertices, edges, faces and it's genus. 
############################################################################### 
def euler_characteristic(a,b):
    #import libraries, set initial lists, change x and y limits of the graph  
    import matplotlib.pyplot as plt 
    colorlist=['blue','red','yellow','black','green','orange','purple']
    cardinal={'N':[[-.5,.5],[.5,.5]],'E':[[.5,-.5],[.5,.5]],'S':[[-.5,-.5],[.5,-.5]],'W':[[-.5,-.5],[-.5,.5]]}
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)  
###############################################################################
    v=vertices(diagram(a,b))
    e=edges(a)
    f=faces(b)
    X=v-e+f
    genus=1-X/2
    print('Number of Vertices=',v)
    print('Number of Edges=',e)
    print('Number of Faces=',f)
    print('Genus ',genus,' Surface')
###############################################################################
# For all values in list and location, assign 4 points of square, give 
# each edge a color, and plot the square. Repeat loop for all values
###############################################################################
def diagram(list1,location):   
    acenter='' 
    bcenter=''
    count=0    
    verticelist=[]    
    for i in list1:
        a,b=i[0][0],i[1][0]
        for j in location:
            if str(a)==str(j[0]):
                acenter=[j[1],j[2]]
            if str(b)==str(j[0]):
                bcenter=[j[1],j[2]]    
        valuea=cardinal[i[0][1]]
        valueb=cardinal[i[1][1]]
        xa=[acenter[0]+valuea[0][0],acenter[0]+valuea[1][0]]
        ya=[acenter[1]+valuea[0][1],acenter[1]+valuea[1][1]]
        xb=[bcenter[0]+valueb[0][0],bcenter[0]+valueb[1][0]]
        yb=[bcenter[1]+valueb[0][1],bcenter[1]+valueb[1][1]]
        plt.plot(xa,ya,color=colorlist[count])
        plt.plot(xb,yb,color=colorlist[count])
        for i in range(2):        
            verticelist.append((xa[i],ya[i]))
            verticelist.append((xb[i],yb[i]))
        count+=1
    return(verticelist)
###############################################################################
# Takes input of verticelist, which is returned in diagram function
###############################################################################
def vertices(verticelist):
    vertices=[]
    library={}
    count=0
    for i in range(0,len(verticelist),2):
        if verticelist[i] not in vertices:
            if verticelist[i+1] not in vertices:              
                vertices.append(verticelist[i])
                vertices.append(verticelist[i+1])
                library[verticelist[i]]=count
                library[verticelist[i+1]]=count
                count+=1
            else:
                vertices.append(verticelist[i])
                library[verticelist[i]]=library[verticelist[i+1]]
        else:            
            vertices.append(verticelist[i+1])
            library[verticelist[i+1]]=library[verticelist[i]]
    for i in range(0,len(verticelist),2):
        for j in library:
            if verticelist[i]==j:
                library[j]=library[verticelist[i+1]]
            if verticelist[i+1]==j:
                library[j]=library[verticelist[i]]
    for i in range(0,len(verticelist),2):
        for j in library:
            if verticelist[i]==j:
                library[j]=library[verticelist[i+1]]                
    v=0    
    a=[]
    for i in library:
        if library[i] not in a:
            a.append(library[i])            
            v+=1
    return(v)
###############################################################################
# Takes input of identification diagram list, returns number of edges
###############################################################################    
def edges(list):
    e=len(list)
    return(e)
###############################################################################
# Takes input of identification diagram location, returns number of faces
###############################################################################       
def faces(location):
    f=len(location)
    return(f)
list1=[('0E','1W'),('0N','0S'),('1N','1S'),('0W','1E')]
location1=[(0,0,0),(1,1,0)]
list2=[('0W','1E'),('0N','1S'),('0S','1N'),('0E','1W')]
location3=[(0,0,0),(1,1,0),(2,1,1)]
list3=[('0W','1E'),('0N','0S'),('1S','2N'),('2W','2E'),('0E','1W'),('1N','2S')]
euler_characteristic(list1,location1)