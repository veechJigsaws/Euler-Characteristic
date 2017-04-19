import numpy as np
#jig=open("jig.svg","w")

svg_file='''<?xml version="1.0" encoding="UTF-8" standalone="no"?> <!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg   xmlns:dc="http://purl.org/dc/elements/1.1/"   xmlns:cc="http://creativecommons.org/ns#"   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"   height="297mm"   viewBox="0 0 210 297"   version="1.1"   id="svg18"   inkscape:version="0.92.1 r15371"   sodipodi:docname="jigsawcut.svg">
  <defs     id="defs12" />  <sodipodi:namedview     id="base"     pagecolor="#ffffff"     bordercolor="#666666"     borderopacity="1.0"
     inkscape:pageopacity="0.0"     inkscape:pageshadow="2"     inkscape:zoom="1.4"     inkscape:cx="400"     inkscape:cy="560"     inkscape:document-units="mm"
     inkscape:current-layer="layer1"     showgrid="false"     showguides="false"     inkscape:window-width="1920"     inkscape:window-height="1001"     inkscape:window-x="-9"
     inkscape:window-y="-9"     inkscape:window-maximized="1" />  <metadata     id="metadata15">    <rdf:RDF>      <cc:Work         rdf:about="">        <dc:format>image/svg+xml</dc:format>
        <dc:type           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />        <dc:title></dc:title>      </cc:Work>    </rdf:RDF>
  </metadata>  <g     inkscape:label="Layer 1"     inkscape:groupmode="layer"     id="layer1">    <path
       style="fill:none;stroke:#000000;stroke-width:0.26458332px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"     
  d="%s"  id="path20"       inkscape:connector-curvature="0"       sodipodi:nodetypes="cssssc" />  </g></svg>'''

# This function takes two inputs, which are determined by the variance defined 
# in the random_jig function, and returns a random number within the variance
def rando(start,end):
    return np.random.uniform(start,end)
    
# This is a function that takes two inputs, a point (can be list or tuple) and
# an angle theta, which is also calculated in random_jig
def rotate(x,y):
    return([x[0]*np.cos(y)-x[1]*np.sin(y),x[0]*np.sin(y)+x[1]*np.cos(y)])

# This is a function that takes two inputs, a list of points, and a tuple 
# describing the x and y displacements to offset the jig by
def translate(a,b):
    newlist=[]    
    for i in a:
        newlist.append((i[0]+b[0],i[1]+b[1]))
    return newlist
    
# This function takes 5 inputs, the start position, end position, and the 
# variance, which determines the amount of randomness in the jigsaw
def random_jig(xstart,ystart,xend,yend,variance):
    import numpy as np    
    list1=[]
    list1.append('M'+str(xstart)+','+str(ystart))
    pi=np.pi
    L=np.sqrt((xstart-xend)**2+(ystart-yend)**2)
    v1,v2=-variance,variance
    xvar=xend-xstart
    yvar=yend-ystart
    if xvar==0:
        theta=pi/2
    else:
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
    return(svg)
    
def stringize(svg):    
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
    return(thesvg+' ')

def idc(list1):                                             #list format:
    sidelist=np.zeros(100)                                  #(xcoordinate,ycoordinate,number of square side 0 is glued to,side1,side2,side3)
    finalstring=''                                          #North: 0
    count=-1                                                #East:  1
    for i in list1:                                         #South: 2
        count+=1                                            #West:  3
        if sidelist[count*4]==0:                            
            n=random_jig(i[0],i[1],i[0]+100,i[1],1)           
            if i[2]=='':
                a=0
                finalstring+=stringize(n)
                for j in list1:
                    if (j[0],j[1])==(i[0],i[1]-100):                       
                        sidelist[count*4],sidelist[a*4+2]=1,1
                    a+=1
            elif sidelist[4*i[2]+2]==0:
                displacement=(list1[i[2]][0]-i[0],list1[i[2]][1]-i[1]+100)
                finalstring+=stringize(translate(n,displacement))
                finalstring+=stringize(n)
                sidelist[count*4],sidelist[4*i[2]+2]=1,1                      
        if sidelist[count*4+1]==0:            
            e=random_jig(i[0]+100,i[1],i[0]+100,i[1]+100,1)            
            if i[3]=='':
                a=0
                finalstring+=stringize(e)
                for j in list1:
                    if (j[0],j[1])==(i[0]+100,i[1]):                       
                        sidelist[count*4+1],sidelist[a*4+3]=1,1
                    a+=1                
            elif sidelist[4*i[3]+3]==0:
                displacement=(list1[i[3]][0]-i[0]-100,list1[i[3]][1]-i[1])
                finalstring+=stringize(translate(e,displacement))
                sidelist[count*4+1],sidelist[4*i[3]+3]=1,1   
                finalstring+=stringize(e)
        '''if sidelist[count*4+2]==0:          
            s=random_jig(i[0],i[1]+100,i[0]+100,i[1]+100,1)            
            if i[4]=='':
                continue            
            elif sidelist[4*i[4]]==0:
                displacement=(list1[i[4]][0]-i[0],list1[i[4]][1]-i[1]+100)
                finalstring+=stringize(translate(s,displacement))
                sidelist[count*4+1],sidelist[4*i[4]-2]=1,1
                finalstring+=stringize(s)
        if sidelist[count*4+3]==0:            
            w=random_jig(i[0],i[1],i[0],i[1]+100,1)            
            if i[5]=='':
                continue             
            elif sidelist[4*i[5]+1]==0:
                displacement=(list1[i[5]][0]-i[0]+100,list1[i[5]][1]-i[1])
                finalstring+=stringize(translate(w,displacement))
                sidelist[count*4+1],sidelist[4*i[5]-2]=1,1
                finalstring+=stringize(w)'''


    return finalstring
    #return sidelist 
test2=[(0,0,12,'','',3),(100,0,13,'','',''),(200,0,14,'','',''),(300,0,15,0,'','')\
    ,(0,100,'','','',7),(100,100,'','','',''),(200,100,'','','',''),(300,100,'',4,'','')\
    ,(0,200, '','','',11),(100,200,'','','',''),(200,200,'','','',''),(300,200,'',8,'',''),\
    (0,300,'','',0,15),(100,300,'','',1,''),(200,300,'','',2,''),(300,300,'',12,3,'')]
    
test3=[(0,0,2,1,'',1),(0,100,'',0,'',0,),(0,200,'',2,0,2)]
print(idc(test3))
#svg_file=svg_file %idc(test3)
#jig.write(svg_file)
