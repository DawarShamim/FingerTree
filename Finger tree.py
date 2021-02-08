class Finger:
    def __init__(self):
        self.head=[]
        self.tail=[]
        self.tail_buffer=[]
        self.head_buffer=[]
        self.body=[]
        #to keep track of total elements
        self.counter=0

    #this function have constant time complexity.
    def InsertatHead(self,*args):
        self.counter+=1
        #checking whether head's limit fulfilled or not
        self.__Checkhead()
        #elements will be added after checking
        self.head=[*args]+self.head
    def __Checkhead(self):
        #special case: if tail is empty transfer element of head to tail.
        if self.tail==[]:
            self.tail=self.head
            # initialize the head to empty
            self.head=[]
        # if length of head fulfills the limit then
        elif len(self.head)>=3:
            # if head_buffer  also reaches it's limit then
            if len(self.head_buffer)>=3:
                # push elements in buffer to body/level3
                self.body.insert(0,list(self.head_buffer))
                # empty the head buffer/level 2
                self.head_buffer=[]
                # push elements in head to buffer
                self.head_buffer.insert(0,list(self.head))
                # empty the head branch/level1
                self.head=[]
            else:
                # push elements in head/level 1 to buffer/level 2
                self.head_buffer.insert(0,list(self.head))
                # empty the head branch/level 1
                self.head=[]


    #this function have constant time complexity
    def InsertatTail(self,*args):
        self.counter+=1
        # checking whether tail's limit fulfilled or not
        self.__Checktail()
        # elements will be added after checking
        self.tail.append(*args)
    def __Checktail(self):
        # special case: if head is empty transfer element of tail to head.
        if self.head==[]:
            self.head=self.tail
            # initialize the tail to empty
            self.tail=[]
        # if length of tail/level 1 fulfills the limit then
        elif len(self.tail)>=3:
            # if tail_buffer/level 2 also reaches it's limit then
            if len(self.tail_buffer)>=3:
                # push elements in buffer/level2  to body/level 3.
                self.body.append(list(self.tail_buffer))
                # empty the tail buffer/level2
                self.tail_buffer=[]
                # push elements in tail/level 1 to buffer/level2
                self.tail_buffer.append(list(self.tail))
                # empty the tail branch/level 1
                self.tail = []
            else:
                # push elements in tail/level1 to buffer/level 2
                self.tail_buffer.append(list(self.tail))
                # empty the tail branch/level 1
                self.tail = []

    # this function have constant time complexity
    def Remove_Head(self):
        # checking number of elements.
        if self.counter == 0:
            # if no elements are in the tree raise exception.
            raise "Tree is empty"
        # checking if head/level1 have any element.
        elif len(self.head) != 0:
            self.counter -= 1
            # popping first element from head/level1.
            x = self.head.pop(0)
            return x
        # checking if head buffer/level2 have any element.
        elif len(self.head_buffer) != 0:
            # transferring first element from buffer/level2 to head/level1.
            self.head = self.head_buffer.pop(0)
            # popping first element from head/level1.
            x = self.head.pop(0)
            self.counter -= 1
            return x
        # checking if body/level3 have any element.
        elif len(self.body) != 0:
            # transferring first element from body/level3 to buffer/level2.
            self.head_buffer = self.body.pop(0)
            # transferring first element from buffer/level2 to head/level1.
            self.head = self.head_buffer.pop(0)
            # popping first element from head/level1.
            self.counter -= 1
            x = self.head.pop(0)
            return x
        # checking if tail buffer/level2 have any element.
        elif len(self.tail_buffer) != 0:
            # transferring first element from tail buffer/level2 to head buffer/level2.
            self.head = self.tail_buffer.pop(0)
            self.counter -= 1
            # popping first element from head/level1.
            x = self.head.pop(0)
            return x
        # checking if tail/level1 have any element.
        elif len(self.tail) != 0:
            self.counter -= 1
            # popping first element from tail/level1.
            x = self.tail.pop(0)
            return x

    # this function have cosntant time complexity
    def Remove_Tail(self):
        # checking number of elements.
        if self.counter == 0:
            # if no elements are in the tree raise exception.
            raise "Tree is empty"
        # checking if tail/level1 have any element.
        elif len(self.tail) != 0:
            self.counter -= 1
            # popping last element from tail/level1.
            x = self.tail.pop()
            return x
        # checking if tail buffer/level2 have any element.
        elif len(self.tail_buffer) != 0:
            # transferring last element from tail buffer/level2 to tail/level1.
            self.tail = self.tail_buffer.pop()
            # popping last element from tail/level1.
            x = self.tail.pop()
            self.counter -= 1
            return x
        # checking if body/level3 have any element.
        elif len(self.body) != 0:
            # transferring last element from body/level3 to buffer/level2.
            self.tail_buffer = self.body.pop()
            # transferring last element from buffer/level2 to tail/level1.
            self.tail = self.tail_buffer.pop()
            self.counter -= 1
            # popping last element from tail/level1.
            x = self.tail.pop()
            return x
        # checking if head buffer/level 2 have any element.
        elif len(self.head_buffer) != 0:
            # transferring last element from head buffer/level2 to tail buffer/level2.
            self.tail = self.head_buffer.pop()
            self.counter -= 1
            # popping last element from tail/level1.
            x = self.tail.pop()
            return x
        # checking if head/level1 have any element.
        elif len(self.head) != 0:
            self.counter -= 1
            # popping last element from head/level1.
            x = self.head.pop()
            return x

    # to get total number of elements.
    def Number_of_elements(self):
        return self.counter

    # number of elements in level 1
    def nodes_in_head(self):
        return len(self.head)

        # number of elements in level 2
    def nodes_in_head_buffer(self):
        return len(self.head_buffer)

        # number of elements in level 3
    def nodes_in_body(self):
        return len(self.body)

        # number of elements in level 2
    def nodes_in_tail_buffer(self):
        return len(self.tail_buffer)

        # number of elements in level 1
    def nodes_in_tail(self):
        return len(self.tail)

    # to get index of given value.
    def position(self,value):
        # pos calls private function which returns data like this("level1",index)
        pos=self.__position_in_head(value)
        # if data returned have two elements it means second element is index
        if len(pos)==2:
            return "index is",pos[1]
        else:
            # in case given value is not in tree returned data is ("not found")
            return pos
    def __position_in_head(self,value):
        # indexing_counter is used to get the index.
        indexing_counter=0
        # checking if head/level 1 contains any element
        if self.head!=[]:
            # flag to check whether execution should be continued or stopped.
            flag=False
            # using for loop.maximum range would be 3.
            for i in range(len(self.head)):
                # incrementing counter as we check each item.
                indexing_counter+=1
                if self.head[i]==value:
                    # if value is found flag is raised.
                    flag=True
                    return("h", (indexing_counter))
            if flag==False:
                # if value is not found call going to head_buffer/level 2.
                return self.__position_head_buffer(value, self.nodes_in_head())
        else:
            return self.__position_head_buffer(value,self.nodes_in_head())                        #if head/level1 contains no element then goto head_buffer/evel 2
    def __position_head_buffer(self,value,indexing_counter):
        if self.head_buffer!=[]:                                                                  #checking if head_buffer/level 2 contains any element
            flag=False                                                                            #flag to check whether execution should be continued or stopped.
            for i in range(len(self.head_buffer)):                                                #using for loop.maximum range would be 3.
                if self.head_buffer[i][0]==value:                                                 # checking 3 elements at a time to decrease the complexity
                    flag = True                                                                   #if value is found flag is raised.
                    return("h1",(indexing_counter+(i*3)+1))
                elif self.head_buffer[i][1]==value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("h1",(indexing_counter+(i*3)+2))
                elif self.head_buffer[i][2]==value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("h1",(indexing_counter+(i*3)+3))
            if flag == False:
                indexing_counter+=(self.nodes_in_head_buffer()*3)                                 #incrementing index by number of elements in level 2 before forwarding it
                return self.__position_body(value, indexing_counter)                              # if value is not found then going to body/level 3.
        else:
            return self.__position_body(value,indexing_counter)                                   # if value is not found call going to body/level 3.
    def __position_body(self,value,indexing_counter):
        if self.body!=[]:                                                                         #checking if head_buffer/level 2 contains any element
            flag = False                                                                          #flag to check whether execution should be continued or stopped.
            for i in range(len(self.body)):                                                       #checking 9 elements at a time.
                if self.body[i][0][0]==value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+1))
                elif self.body[i][0][1]==value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+2))
                elif self.body[i][0][2]==value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+3))
                elif self.body[i][1][0] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+4))
                elif self.body[i][1][1] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+5))
                elif self.body[i][1][2] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+6))
                elif self.body[i][2][0] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+7))
                elif self.body[i][2][1] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+8))
                elif self.body[i][2][2] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("b",(indexing_counter+(i*9)+9))
            if flag == False:
                indexing_counter += (int(self.nodes_in_body()) * 9)                               #incrementing index by number of elements in body\level 3
                return self.__position_tail_buffer(value, indexing_counter)                       #checking in tail_buffer/level 2
        else:
            return self.__position_tail_buffer(value, indexing_counter)                           #checking in tail_buffer/level 2
    def __position_tail_buffer(self, value, indexing_counter):
        if self.tail_buffer != []:                                                                #checking if tail_buffer/level 2 contains any element
            flag = False                                                                          #flag to check whether execution should be continued or stopped.
            for i in range(len(self.tail_buffer)):                                                #using for loop.maximum range would be 3.
                if self.tail_buffer[i][0] == value:                                               # checking 3 elements at a time to decrease the complexity
                    flag = True                                                                   #if value is found flag is raised.
                    return("t1",(indexing_counter + (i * 3) + 1))
                elif self.tail_buffer[i][1] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("t1", (indexing_counter + (i * 3) + 2))
                elif self.tail_buffer[i][2] == value:
                    flag = True                                                                   #if value is found flag is raised.
                    return("t1", (indexing_counter + (i * 3) + 3))
            if flag == False:
                indexing_counter += (int(self.nodes_in_tail_buffer()) * 3)                        #incrementing index by number of elements in level 2 before forwarding it
                return self.__position_in_tail(value, indexing_counter)                           # if value is not found then going to tail/level 1.
        else:
            return self.__position_in_tail(value, indexing_counter)                               # if value is not found call going to tail/level 1.
    def __position_in_tail(self,value,indexing_counter):
        if self.tail!=[]:
            flag=False
            for i in range(len(self.tail)):
                indexing_counter+=1
                if self.tail[i]==value:
                    flag=True
                    return ("t",(indexing_counter))
            if flag==False:
                return("not Found")
        else:
            return("not Found")
    def concatenate(self,node,value):
        temp_place=self.__position_in_head(value)                                                           #using position to check after which elemnt should the new node be added
        temp_place=temp_place[0]
        if temp_place=="n":                                                                                 #if the given value is not found in tree.
            raise "this element doesn't exist"                                                              #exception is raised
        else:
            # if value is found then it's position is returned
            place=temp_place
            # now checking whether the position is in level 2.t1 means level2
            if place == "t1":
                try:
                    #if node is compatible at level 2
                    if len(node) == 3:
                        # then concatenate
                        return self.__concatenate_tail_buffer(node)
                    else:
                        # else raise exception
                        raise "node is not compatible at level 2 \n your node should be like this:[1,2,3]"
                except:
                    raise "node is not compatible at level 2 \n your node should be like this:[1,2,3]"
            # b means level 3
            elif place == "b":
                try:
                    # if given node is compatible
                    if len(node[0]) == 3 and len(node[0]) == 3 and len(node[1]) == 3 and len(node[2]) == 3:
                        return self.__concatenate_body(node)
                    else:
                        # else raise exception
                        raise "given node is not compatible at level 3\n your node should be like this:[1,2,3]"
                except:
                    raise "given node is not compatible at level 3\n your node should be like this:[1,2,3]"
            # h1 means level 2
            elif place == "h1":
                try:
                    # checking compatiblity
                    if len(node) == 3 :
                        return self.__concatenate_head_buffer(node)
                    else:
                        raise "node is not compatible at level 2\n your node should be like this:[[1,2,3],[4,5,6],[7,8,9]]"
                except:
                    raise "given node is not compatible at level 2\n your node should be like this:[[1,2,3],[4,5,6],[7,8,9]]"
            elif place == "h":
                try:
                    # checking compatiblity
                    if node is int or float:
                        return self.__concatenate_head(node)
                    else:
                        raise "node is not compatible at level 1\n your node should be like this:2"
                except:
                    raise "given node is not compatible at level 1\n your node should be like this:2"
            elif place == "t":
                try:
                    # checking conpatiblity
                    if node is int or float:
                        # concatenating at tail and inserting at tail are same.
                        return self.InsertatTail(node)
                    else:
                        raise "node is not compatible at level 1\n your node should be like this:2"
                except:
                    raise "given node is not compatible at level 1\n your node should be like this:2"

    # concatenate at head/level 1
    def __concatenate_head(self,node):
        # incrementing number of element
        self.counter += 1
        # checking head if it is ready to add an element
        self.__Checkhead()
        self.head.append(node)

    # concatenate at head_buffer/level 2
    def __concatenate_head_buffer(self,node):
        # checking head if it is ready to add an element
        if len(self.head_buffer) >= 3:
            self.body.insert(0, list(self.head_buffer))
            self.head_buffer = []
            self.head_buffer.append(node)
            # incrementing number of element.
            self.counter += 3
        else:
            # incrementing number of element.
            self.head_buffer.append(node)
            # concatenating  in body/level 3
            self.counter += 3
    def __concatenate_body(self,node):
        self.body.append(node)
        self.counter += 9

    # concatenating at tail_buffer/level 2
    def __concatenate_tail_buffer(self,node):
        # checking whether tail_buffer is already filled or not
        if len(self.tail_buffer) >= 3:
            self.body.append(list(self.tail_buffer))
            self.tail_buffer = []
            self.tail_buffer.append(node)
            self.counter += 3
        else:
            self.tail_buffer.append(node)
            self.counter += 3

    # this function have time complexity of  O(log n):
    def split(self,value):
        # creating new object of finger tree
        abc=Finger()
        # to get the position of point from where tree should be splitted
        splitting=self.__position_in_head(value)
        # whether the element even exist
        if splitting=="not Found":
            # raise exception
            raise "splitting point not found"
        # if tree should be splitted from head/level 1
        elif splitting[0] == "h":
            for i in self.head:
                abc.InsertatTail(i)
        # if tree should be splitted from head_buffer/level 2
        elif splitting[0] == "h1":
            # using single loop to reduce time complexity
            for i in range(len(self.head_buffer)):
                abc.InsertatTail(self.head_buffer[i][0])
                abc.InsertatTail(self.head_buffer[i][1])
                abc.InsertatTail(self.head_buffer[i][2])
        # if tree should be splitted from body/level 3
        elif splitting[0] == "b":
            # using single loop to reduce time complexity
            for i in range(len(self.body)):
                # therefore using explicit indexing
                abc.InsertatTail(self.body[i][0][0])
                abc.InsertatTail(self.body[i][0][1])
                abc.InsertatTail(self.body[i][0][2])
                abc.InsertatTail(self.body[i][1][0])
                abc.InsertatTail(self.body[i][1][1])
                abc.InsertatTail(self.body[i][1][2])
                abc.InsertatTail(self.body[i][2][0])
                abc.InsertatTail(self.body[i][2][1])
                abc.InsertatTail(self.body[i][2][2])

        # if tree should be splitted from tail_buffer/level 2
        elif splitting[0]=="t1":
            # using single loop
            for i in range(len(self.tail_buffer)):
                abc.InsertatTail(self.tail_buffer[i][0])
                abc.InsertatTail(self.tail_buffer[i][1])
                abc.InsertatTail(self.tail_buffer[i][2])
        # if tree should be splitted from tail/level 1
        elif splitting[0]=="t":
            for i in self.tail:
                abc.InsertatTail(self.head_buffer[i][0])
        return abc

    # to get all the data from the tree
    def All_Data(self):
        print("Head",self.head)
        print("Head_Buffer",self.head_buffer)
        print("Body",self.body)
        print("Tail_Buffer",self.tail_buffer)
        print("Tail",self.tail)

# driver code:
obj=Finger()
for i in range(22):
    obj.InsertatHead(i)
for i in range(3):
    obj.InsertatTail(i)
print("\nAFTER\n")
for i in range(3):
    obj.InsertatTail(i)
# print(obj.Remove_Head())
# print(obj.Remove_Tail())
# obj.all_data()
# obj.all_data()
obj.All_Data()
# print("\nSPLITTING\n")
# obj1=obj.split(2)
print("\nAFTER\n")
index=obj.position(18)
print(index)
obj.concatenate([111,88,99],18)
obj.All_Data()
obj.concatenate([111,88,99],0)
obj.concatenate([111,88,99],0)
obj.All_Data()
# (obj1.all_data())
# print(obj.Number_of_elements())
print((obj.position(21)))
# print(obj.nodes_in_head())
# print(obj.nodes_in_head_buffer())
# print(obj.nodes_in_body())
# print(obj.nodes_in_tail_buffer())
# print(obj.nodes_in_tail())
