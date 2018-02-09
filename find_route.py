'''
Created on Jan 23, 2018

@author: Abhishek Modi
'''

import sys

                    
def fringe_sort(fringe):
#     Insertion sorting algo over here
#     print "Fringe before sort:",fringe

    for j in range(1,len(fringe)):
        key = fringe[j][2]
        key_list = fringe[j]
        i = j-1
        while(i >= 0 and fringe[i][2]>key):
            fringe[i+1] = fringe[i]
            i = i-1
        fringe[i+1] = key_list
     
#     print "Fringe After sort:",fringe
    return fringe
    

def path_finder(file,origin_city, destination_city):
    flag = 1
    fringe = []
    closed = []
    closed_nodes = []
    fringe.append(["",origin_city,int(0)])
    end = "END OF INPUT"
    while(flag):
        fopen = open(file,"r")
        if(fringe == []):
#             print "Failure!!!"
            return []
        
        ##    pops the first value from fringe
        temp = fringe.pop(0)
        
        ## Goal test
        if temp[1] == destination_city:
#             print "found"
            flag = 0
            
        if temp[1] not in closed:
            closed.append(temp[1])
            closed_nodes.append(temp)
            count = 0
            
            ##    Finds all the adjacent locations and appends it to the fringe
            for i in fopen:
                if end in i:
                    break
                if temp[1] in i:
                    count = count + 1
                    i = i.split()
                    if temp[1] == i[0]:
                        i[2] = int(i[2]) + int(temp[2])
                        fringe.append(i)
                    elif temp[1] == i[1]:
                        temp1 = i[0]
                        i[0] = i[1]
                        i[1] = temp1
                        i[2] = int(i[2]) + int(temp[2])
                        fringe.append(i)
            if count == 0 and fringe == []:
#                 print "No Route"
                return []
            
            ##    Sorts the fringe
            fringe = fringe_sort(fringe)
                        
        fopen.close()    

    return closed_nodes
                
def backtracking(closed_nodes,destination_city):
   
    if closed_nodes == []: 
        print "Distance: Infinite"
        print "Route:\nNone"
        return
    
    closed_nodes = closed_nodes[::-1]
    route = []
#     print closed_nodes
#     flag = 1
#     while(flag):
    if closed_nodes[0][1] != destination_city:
        return
    temp = closed_nodes[0]
    route.append(temp)
    for node in closed_nodes:
        if temp[0] in node[1]:
            temp = node
            route.append(temp)
#     print 'Route: \n', route
    
    print "\nDistance:", route[0][2],"km"
    print "\nRoute:"
    prev_value = 0
    route = route[::-1]
    for node in range(1,len(route)):
        print route[node][0], "to", route[node][1],",", route[node][2] - prev_value,"km"
        prev_value = route[node][2]
    


##    Stores Filename in the object
f = sys.argv[1]

try:
    fopen = open(f,"r")
    flag = 1
except:
    print "Invalid File Name"
    flag = 0

if flag == 1:
    origin_city = sys.argv[2]
    destination_city = sys.argv[3]
    print f, origin_city, destination_city
    closed_nodes = path_finder(f, origin_city, destination_city) 
    backtracking(closed_nodes,destination_city)
     