from collections import OrderedDict
from itertools import izip, repeat

#List formation
class node(object):
    def __init__(self):
        self.startnode = None
        self.endnode = None
        self.cost = None
        self.next_node = None

class linkedlist(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.newele = None
        self.temp = None
        self.temp1 = None

    def isEmpty(self):
        return (self.start == None )

    def insertFirst(self, startnode, endnode, cost):
        self.newele = node()
        self.newele.startnode = startnode
        self.newele.endnode = endnode
        self.newele.cost = cost
        self.newele.next_node = None
	empty = self.isEmpty()
        if(empty):
            self.start = self.newele
            self.end = self.newele            
        else:
            self.end.next_node = self.newele
            self.end = self.newele

    def printList(self):
        empty = self.isEmpty()
        if(empty):
            trial = 1
#            print "List is empty"
        else:
            self.temp = self.start
            while (self.temp != None):
                print self.temp.startnode
                print self.temp.endnode
                print self.temp.cost
                self.temp = self.temp.next_node

    def destinationsearch(self,startele):
        empty = self.isEmpty()
        dest = []
        if(empty):
            trial = 1
#            print "List is empty.Destination search"
        else:
            self.temp = self.start
            while (self.temp != None):
                if(self.temp.startnode == startele):
                    dest.append(self.temp.endnode)
                self.temp = self.temp.next_node
            return dest
    

    def gsearch(self,startele,endele):
        empty = self.isEmpty()
        if(empty):
            trial = 1
#            print "List is empty.g value search"
        else:
            self.temp = self.start
            while (self.temp != None):
                if((self.temp.startnode == startele) and (self.temp.endnode == endele)):
                    g = self.temp.cost
                self.temp = self.temp.next_node
            return g

#Queue formation
class queuenode(object):
    def __init__(self):
        self.nodenumber = None
        self.state = None
        self.g = None
        self.depth = None
        self.parent = None
        self.f = None

class queue(object):
    def __init__(self):
        self.nodes = []
        self.temp1 = None
        self.temp2 = None
        self.temp3 = None
        self.temp4 = None
        self.front = 0
        self.rear = -1
        self.itemcount = 0
        self.array = []
        self.array1 = []
        self.array2 = []
        self.array3 = []
        self.array4 = []

    def isEmptyQueue(self):
        return (self.itemcount == 0)
  
    def isFull(self):
        return (self.itemcount == self.MAX)
    
    def size(self):
        return self.itemcount

    def printqueue(self):
        emptyqueue = self.isEmptyQueue()
        if(emptyqueue):
            trial = 1
#            print "Queue is empty"
        else:
            self.temp2 = queuenode()
            i = self.front
            while (i <= self.rear):
                j = 0
#                while (j <= 5):
                print self.nodes[i][1]
#                    j = j + 1
                i = i + 1

    def sortarray(self,n):
        emptyqueue = self.isEmptyQueue()
        if(emptyqueue):
            trial = 1
#            print "Queue is empty"
        else:
            a = []
            i = self.front
            while (i <= self.rear):
                a.append(self.nodes[i])
                i = i + 1
            a.sort(key = lambda row: row[n])
            self.makequeueempty()
            j = 0
            l = len(a)
            while(j < l):
                qnode = a[j]
                self.insertqueue(qnode)
                j = j + 1

    def insertqueue(self,qnode):
        self.newnode = queuenode()
        self.newnode = list(qnode)
        self.rear = self.rear + 1
        self.nodes.insert(self.rear,self.newnode)
        self.itemcount = self.itemcount + 1            
 
    def makequeueempty(self):
        del self.nodes[:]
        self.front = 0
        self.rear = -1
        self.itemcount = 0 
    
    def assign(self,i):
        a = i
        return a   

    def insertbeg(self,qnode):
        self.newnode = queuenode()
        self.newnode = list(qnode)
        i = self.front
        while ( i < self.rear ):
            self.nodes[i+1] = self.nodes[i]
            i = i + 1
        self.rear = self.rear + 1
        self.nodes.insert(self.front,self.newnode)
        self.itemcount = self.itemcount + 1

    def removeatfirst(self):
        emptyqueue = self.isEmptyQueue()
        if(emptyqueue):
#            print "Queue is empty"
            return None
        else:
            self.temp3 = self.nodes[self.front]
            self.front = self.front + 1
            self.itemcount = self.itemcount - 1
            return self.temp3

    def searchparent(self,parent):
        i = 0
        ele = 0
        j = len(self.array3)
        while( i < j ):
            if(parent == self.array3[i][0]):
                ele = self.array3[i][4]
                self.array.append(ele)
                ele1 = self.array3[i][1]
                ele2 = self.array3[i][2]
                self.array1.append(ele1)
                self.array2.append(ele2)
            i = i + 1
        return ele

    def returnstate(self, parent, array):
        self.array3 = list(array)
#        emptyqueue = self.isEmptyQueue()
#        if(emptyqueue):
#            print "Queue is empty**"
#            return None
#        else:
        while ( parent != None ):
            parent = self.searchparent(parent) 
                              
    def printoutput(self):
        i = 0
        self.array1.reverse()
        self.array2.reverse()
        l = len(self.array1)
        while(i < l):
#            print "Final route"
#            print self.array1[i]
#            print self.array2[i]     
            i = i + 1
        return (self.array1, self.array2)

    def searchqueue(self, node):
        emptyqueue = self.isEmptyQueue()
        if(emptyqueue):
#            print "Queue is empty"
             trial = 1
        else:
            self.temp2 = queuenode()
            self.temp2 = list(node)
            i = self.front
#            print "search queue values check"
            while(i <= self.rear):
                if(self.nodes[i][1] == self.temp2[1]):
 #                   print "match found"
                    if(self.nodes[i][2] < self.temp2[2]):
                        return self.nodes[i]
                    else: 
                        return None
 #               else:
 #                   print "match not found"
                i = i + 1


    def deleteelement(self, node):
        self.temp2 = queuenode()
        self.temp = queuenode()
        self.temp2 = list(node)
        i = 0
        #search for that element
        while(i <= self.rear):
            if(self.nodes[i][1] == self.temp2[1]):
                print "element to be deleted"
                print self.nodes[i]
                self.temp = self.nodes[i]
                a = i
            i = i + 1
        #remove the element
        print "element removed is"
        print self.temp
        print "index"
        print a
        j = a
        while(j < self.rear):
            self.nodes[j]= self.nodes[j+1]
            j = j + 1
        self.rear = self.rear - 1


l = linkedlist()
f = open('input.txt', 'r')
algorithm = f.readline()
start_node = f.readline()
end_node = f.readline()
no_routes = f.readline()
algorithm = algorithm.strip()
start_node = start_node.strip()
end_node = end_node.strip()
no_routes = no_routes.strip()
i = int(no_routes)
routes_2 = i * 2
#print algorithm
while (i > 0):
    route = f.readline()
    start_1,end_1,cost = route.split(" ")
    cost = int(cost)
#    print start_1,end_1,cost
    l.insertFirst(start_1, end_1, cost)
    i = i - 1
#heuristics
no_h = f.readline()
no_h = no_h.strip() 
j = int(no_h)
no_h = int(no_h)
arr_h = []
while (j > 0):
    arr_h1 = []
    heuristics = f.readline()
    node_name,h_cost = heuristics.split(" ")
    h_cost = int(h_cost)
#    print node_name,h_cost
    arr_h1.append(node_name)
    arr_h1.append(h_cost)
    arr_h.append(arr_h1)
    j = j - 1

#print "The List"
#l.printList()      #list is formed


if(algorithm == "A*"):
############ A* implementation ############
#    print algorithm
    nodenumber = 1
    depth = 0
    ar = []
    openqueue_astar = queue()
    closedqueue_astar = queue()

#Form first node
    g = 0
    firstnode = [nodenumber,start_node,g,depth,None,0]
    nodenumber = nodenumber + 1
    depth = depth + 1
    openqueue_astar.insertqueue(firstnode)
    ar.append(firstnode)
#print "first node"
#q.printqueue()

#Form other nodes
    dest = []
    dest_index = 0

    j = openqueue_astar.isEmptyQueue()
    while (j != True):
        goalnode = openqueue_astar.removeatfirst()
        closedqueue_astar.insertqueue(goalnode)
 #   print "goalnode"
 #   print goalnode
        if(goalnode[1] == end_node):
   #     print "Success! End found"
   #     print end_node
            break
        else:
            dest = l.destinationsearch(goalnode[1])
#        g_1 = goalnode[2]
            dest_l = len(dest)
            dest_index = 0
            while(dest_index < dest_l):
                g_start = goalnode[1]
                g = l.gsearch(g_start,dest[dest_index])
  #          print "g value from previous nodes"
  #          print g
  #          print "current gal node"
  #          print goalnode
                g_1 = goalnode[2] + g
 #           print "f value g + g_1"
 #           print g_1
            # search h value
                h_i = 0
                ele = dest[dest_index]
            
                flag_h = 0
                while(h_i < no_h):
                    if(arr_h[h_i][0] == ele):
                        h = arr_h[h_i][1]
                        flag_h = 1
 #                   print "corresponding h value"
 #                   print h
                    h_i = h_i + 1
           
                if(flag_h == 0):
                    h = 0
                
                f = g_1 + h
                mnode = [nodenumber,dest[dest_index],g_1,depth,goalnode[0],f]
                nnode1 = closedqueue_astar.searchqueue(mnode)
                nnode2 = openqueue_astar.searchqueue(mnode)
                if((nnode1 == None) and (nnode2 == None)):
                    openqueue_astar.insertqueue(mnode)
                    ar.append(mnode)
                elif((nnode1 == None) and (nnode2 != None)):
                    if(mnode[2] < nnode2[2]):
                        openqueue_astar.deleteelement(nnode2)
                        openqueue_astar.insertqueue(mnode)
                        ar.append(mnode)
                elif((nnode1 != None) and (nnode2 == None)):
                    if(mnode[2] < nnode1[2]):
                        closedqueue_astar.deleteelement(nnode1)
                        openqueue_astar.insertqueue(mnode)
                        ar.append(mnode)
                openqueue_astar.sortarray(5)
#            print "sorted array"
#            q.printqueue()
#            print "queue empty or not"
#            print q.isEmptyQueue()
                nodenumber = nodenumber + 1
                dest_index = dest_index + 1
        depth = depth + 1    
        j = openqueue_astar.isEmptyQueue()
#    print "j value"
#    print j

#print "Final goal node:"
#print goalnode
#    print goalnode
    gn = goalnode[0]  
#print "array of nodes"
#print ar
    openqueue_astar.returnstate(gn,ar)
    out_state_astar = []
    out_cost_astar = []
    out_state_astar, out_cost_astar = openqueue_astar.printoutput() 

    astar_state = OrderedDict(izip(out_state_astar,repeat(None)))     
    out_state_astar = list(astar_state)

    astar_cost = OrderedDict(izip(out_cost_astar,repeat(None)))
    out_cost_astar = list(astar_cost) 

    out_file = open('output.txt', 'w')
#out_file.write("Hi")
    arr_len = len(out_state_astar)
    i =0
    while(i<arr_len):
        state_out_astar = out_state_astar[i]
        cost_out_astar = str(out_cost_astar[i])
        out_file.write(state_out_astar + " " + cost_out_astar + "\n")
        i = i + 1
    out_file.close()
#print out_state_astar
#print out_cost_astar


elif(algorithm == "UCS"):
################# UCS implementation ##################

#    print "UCS IMPLEMENTATION"
    openqueue = queue()
    closedqueue = queue()
    g = 0
    depth = 0
    nodenumber = 1
    ar1 = []

#First node formation
    firstnode = [nodenumber,start_node,g,depth,None,0]
    nodenumber = nodenumber + 1
    depth = depth + 1
    openqueue.insertqueue(firstnode)
    ar1.append(firstnode)
#print "open queue"
#openqueue.printqueue()  #First node formed

#Formation of other nodes
    dest = []
    j = openqueue.isEmptyQueue()
#    print j
    while (j != True):
        goalnode = openqueue.removeatfirst()
        closedqueue.insertqueue(goalnode)
    
        if(goalnode[1] == end_node):
#        print "Success! End found"
#        print end_node
            break
        else:
#        print "not found yet"
            dest = l.destinationsearch(goalnode[1])
            dest_l = len(dest)
            dest_index = 0
            while(dest_index < dest_l):
                g_start = goalnode[1]
                g = l.gsearch(g_start,dest[dest_index])
                g_1 = goalnode[2] + g
                mnode = [nodenumber,dest[dest_index],g_1,depth,goalnode[0],0]
                nnode1 = closedqueue.searchqueue(mnode)
                nnode2 = openqueue.searchqueue(mnode)
                if((nnode1 == None) and (nnode2 == None)):
                    openqueue.insertqueue(mnode)
                    ar1.append(mnode)
                elif((nnode1 == None) and (nnode2 != None)):
                    if(mnode[2] < nnode2[2]):
                        openqueue.deleteelement(nnode2)
                        openqueue.insertqueue(mnode)
                        ar1.append(mnode)
                elif((nnode1 != None) and (nnode2 == None)):
                    if(mnode[2] < nnode1[2]):
                        closedqueue.deleteelement(nnode1)
                        openqueue.insertqueue(mnode)
                        ar1.append(mnode)
                openqueue.sortarray(2)
                nodenumber = nodenumber + 1
                dest_index = dest_index + 1
 #   print "open queue"
 #   openqueue.printqueue()
        depth = depth + 1    
        j = openqueue.isEmptyQueue()

#print "Final goal node"
#print goalnode
    gn1 = goalnode[0]
#print "array of nodes"
#print ar1
    openqueue.returnstate(gn1,ar1)
    out_state_ucs = []
    out_cost_ucs = []
    out_state_ucs, out_cost_ucs = openqueue.printoutput()
   
    ucs_state = OrderedDict(izip(out_state_ucs,repeat(None)))     
    out_state_ucs = list(ucs_state)

    ucs_cost = OrderedDict(izip(out_cost_ucs,repeat(None)))
    out_cost_ucs = list(ucs_cost)
    

    out_file = open('output.txt', 'w')
#    out_file.write("Hi")
    arr_len = len(out_state_ucs)
    i =0
    while(i<arr_len):
        state_out_ucs = out_state_ucs[i]
        cost_out_ucs = str(out_cost_ucs[i])
        out_file.write(state_out_ucs + " " + cost_out_ucs + "\n")
        i = i + 1
    out_file.close()
#    print out_state_ucs
#    print out_cost_ucs

elif(algorithm == "BFS"):
############ BFS implementation ###############

    ar_bfs = []
    queuebfs = queue()
#print "BFS IMPLEMENTATION"

#First node formation
    g = 0
    depth = 0
    nodenumber = 1

    firstnode = [nodenumber,start_node,g,depth,None,0]
    nodenumber = nodenumber + 1
    g = g + 1
    depth = depth + 1
    queuebfs.insertqueue(firstnode)
    ar_bfs.append(firstnode)
#queuebfs.printqueue()

#Other nodes formation
    j = queuebfs.isEmptyQueue()
    dest = []
    while (j != True):
        goalnode = queuebfs.removeatfirst()
        if(goalnode[1] == end_node):
#        print "Success! End found"
#        print end_node
            break
 
        else:
            dest = l.destinationsearch(goalnode[1])
            dest_l = len(dest)
            dest_index = 0
            while(dest_index < dest_l):
#            print "array ele"
#            print ar_bfs[0][1]
                index_arr = 0
                len_arr = len(ar_bfs)
                flag = 0
                g = goalnode[2] + 1
                while(index_arr < len_arr):
                    if(dest[dest_index] == ar_bfs[index_arr][1]):
#                    print "match found"
#                    print dest[dest_index]
                        flag = 1
                    index_arr = index_arr + 1
            
                if(flag != 1):
                    mnode = [nodenumber,dest[dest_index],g,depth,goalnode[0],0]
                    queuebfs.insertqueue(mnode)
                    ar_bfs.append(mnode)
             
                nodenumber = nodenumber + 1
                dest_index = dest_index + 1
    
        depth = depth + 1
#    queuebfs.printqueue()
#    print queuebfs.isEmptyQueue()
        j = queuebfs.isEmptyQueue()
   
#print "Final goal node"
#print goalnode
    gn1 = goalnode[0]
#print "array of nodes"
#print ar_bfs
    queuebfs.returnstate(gn1,ar_bfs)
    out_state_bfs = []
    out_cost_bfs = []
    out_state_bfs, out_cost_bfs = queuebfs.printoutput() 

    out_file = open('output.txt', 'w')
#    out_file.write("Hi")
    arr_len = len(out_state_bfs)
    i =0
    while(i<arr_len):
        state_out_bfs = out_state_bfs[i]
        cost_out_bfs = str(out_cost_bfs[i])
        out_file.write(state_out_bfs + " " + cost_out_bfs + "\n")
        i = i + 1
    out_file.close()
#print out_state_bfs
#print out_cost_bfs


elif(algorithm == "DFS"):
############## DFS IMPLEMENTATION ################

    ar_dfs = []
    queuedfs = queue()
#print "DFS IMPLEMENTATION"

#First node formation
    g = 0
    depth = 0
    nodenumber = 1

    firstnode = [nodenumber,start_node,g,depth,None,0]
    nodenumber = nodenumber + 1
    g = g + 1
    depth = depth + 1
    queuedfs.insertbeg(firstnode)
    ar_dfs.append(firstnode)
#queuedfs.printqueue()
    success_flag = 0

    j = queuedfs.isEmptyQueue()
    while (j != True):
        goalnode = queuedfs.removeatfirst() 
        if(goalnode[1] == end_node):
#        print "Success! End found"
#        print end_node
            break
        else:
            dest = l.destinationsearch(goalnode[1])
#        print "dest:"
#        print dest
            dest_l1 = len(dest)
            dest_index1 = 0
            g = goalnode[2] + 1
            while(dest_index1 < dest_l1):
                if(dest[dest_index1] == end_node):
                    mnode = [nodenumber,dest[dest_index1],g,depth,goalnode[0],0]
                    queuedfs.insertbeg(mnode)
                    ar_dfs.append(mnode)
                    goalnode = mnode
#                print "inserted a special node"
                    success_flag = 1
                    break
                dest_index1 = dest_index1 + 1
            if(success_flag == 1):
#            print "Success end found"
                break
            dest_l = len(dest)
            dest_index = 0
            dest.reverse()
            while(dest_index < dest_l):
#            print "array ele"
#            print ar_dfs[0][1]
                index_arr = 0
                len_arr = len(ar_dfs)
                flag = 0
                while(index_arr < len_arr):
                    if(dest[dest_index] == ar_dfs[index_arr][1]):
#                    print "match found"
#                    print dest[dest_index]
                        flag = 1
                    else:
                        flag = 0
#                    print "match not found"
                    index_arr = index_arr + 1      
#            print "flag"
#            print flag   
                if(flag != 1):
                    g = goalnode[2] + 1
                    mnode = [nodenumber,dest[dest_index],g,depth,goalnode[0],0]
                    queuedfs.insertbeg(mnode)
#                print "queue during each insert"
#                queuedfs.printqueue()
#                print "end of local queue"
                    ar_dfs.append(mnode)

                nodenumber = nodenumber + 1
                dest_index = dest_index + 1
        depth = depth + 1
#    queuedfs.printqueue()
#    print queuedfs.isEmptyQueue()
        j = queuedfs.isEmptyQueue()
   
#print "Final goal node"
#print goalnode
    gn1 = goalnode[0]
#print "array of nodes"
#print ar_dfs
    queuedfs.returnstate(gn1,ar_dfs)
    out_state_dfs = []
    out_cost_dfs = []
    out_state_dfs, out_cost_dfs = queuedfs.printoutput() 
    out_file = open('output.txt', 'w')
#out_file.write("Hi")
    arr_len = len(out_state_dfs)
    i =0
    while(i<arr_len):
        state_out_dfs = out_state_dfs[i]
        cost_out_dfs = str(out_cost_dfs[i])
        out_file.write(state_out_dfs + " " + cost_out_dfs + "\n")
        i = i + 1
    out_file.close()
#print out_state_dfs
#print out_cost_dfs
