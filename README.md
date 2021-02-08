# Finger Trees

Finger trees are a versatile family of fully persistent collections.  This library includes everything you need to make your own, as well a few ready-to-use collection types:

- **double-list** is a sequential collection that provides constant-time access to both the left and right ends.

- **counted-double-list** provides all the features of double-list plus constant-time `count` and log-n `nth`.


# Finger Tree Quickstart
First we need to create an object:
## object creation:
```
obj=FingerTree
```
now we can add elements in it using:
## insertion:
```
obj.InsertatHead(1)
```
we can add any data types
for example:
```
obj.InsertatHead("abc")
```  
```
obj.InsertatHead(["abc",1])
``` 
```
obj.InsertatHead((1,2,3))
``` 

we can also insert at tail using:

    obj.InsertatTail(1)

## Splitting:

this data structure allow us to split the existing tree to from another tree (subset) from any node 
this can be done using

    obj1=obj.split(value)
    
## position:
to find the position of an arbitrary value:
    
    print((obj.position(21)))

this function will return the postion of value in sequence.

## Concatenation:
to concate you should know the place of value after which you are concatenating.   
this is done using:

    obj.concatenate([111,88,99],11)

## Removing :
to remove element from the head of given sequence:

    obj.Remove_Head()

to remove the last element of the given sequence:
    
    obj.Remove_Tail()

## Total elements in sequence:
numbers of elements can be obtained using

    obj.Numbers_of_elements()

## Elements of sequence:
all elements of sequence can be view using
    
    obj.All_Data()

[1]: http://www.soi.city.ac.uk/~ross/papers/FingerTree.html