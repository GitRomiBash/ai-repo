    # Create a variable and set it as a list



## index:  0     1    2    3    4    5    6
my_list = ["a", "b", "c", "d", "e", "f", "g"]
print(my_list)

    # Methods for accessing parts of a list



my_list = ["a", "b", "c", "d", "e", "f", "g"]
print(my_list[0]) # Accesses the first element ("a")
print(my_list[2]) # Accesses the thrid element ("c")

#slicing a list: (can slice a list to access a subset of elements.)
my_list = ["a", "b", "c", "d", "e", "f", "g"]
print(my_list[1:4]) #Access elements from index 1 to 3

#negative indexing: (can use negative indexing to access elements from the end of the list.) Ex:
my_list = [10, 20, 30, 40, 50]
print(my_list[-1]) #Access the last element (50)

#Looping thru a list, u can iterate over all elements in a list using a loop.
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)


    # Return the value of a list at a given index

my_list = [10, 20, 30, 40, 50]
index = 2
value_at_index = my_list[index]
print(value_at_index)
##Or
my_list = [10, 20, 30, 40, 50]
print(my_list[2])




#Moms:
#def valueofindex(index):
   # print("Return the value of a list at a given index\n")
    #print("The value in index ", index, "  is:", my_list[index],"\n")
    #return my_list[index]

#myValue = valueofindex(3)
#print(myValue)

#valueofindex(5)








    # Return the index of the first object with a matching value

my_list = [10, 20, 30, 40, 30]
value_to_find = 30
index = my_list.index(value_to_find)
print(index)

##In this example, my_list is a list of numbers, and we want to find the index of the first occurrence of the value 30. The index() method will return the index of the first element with the specified value. In this case, it will return 2 because 30 is first found at index 2 in the list.









#Moms:
#def indexofvalue(value):
    # set a counter to find out what is the position/index of the value provided by user
    #counter = 0
    
    #itterate for each item in mylist
    #for item in my_list:
        #if item == value:
           # print("Value provided by user is in list with  index of ", counter)
        
        #counter += 1
#indexofvalue("z")










    # Return a list slice [index_start:index_end]
xlist = ["pinetree", "oaktree", "palmtree", "smalltree", "bigtree", "stubbytree", "thintree"]

print(xlist[1:4])

##This will return a new list containing elements from start_index up to (but not including) end_index in the original list.





    # Print the data type of user_name
#?
#Dummy example:
user_name = "John"
print(type(user_name))


    # Methods for modifying a list


#1st append
my_list = [1, 2, 3]
my_list.append(7)
print(my_list)
##Adds an element to the end of the list.

#2cd extend   
my_list = [1, 2, 3]
my_list.extend([4,5,6])
print(my_list)
##Extends the list by appending elements from another iterable.


#3rd insert : Inserts an element at a specified position.
my_list = [1, 2, 3]
my_list.insert(1,5) ##Insert 5 at index 1
print(my_list)

#4th remove : Removes the first occurrence of a specified value.
my_list = [1, 2, 3, 2]
my_list.remove(2) ##Removes the first occurence of 2
print(my_list)




#5th pop : Removes and returns the element at a specified index.
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
# Removes and returns the element at index 1

#6th Delete: Deletes an element at a specified index.
my_list = [1, 2, 3]
del my_list[1]  # Deletes the element at index 1
print(my_list)


#7th Clear : Removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()  # Removes all elements from the list
print(my_list)







    # Add an element onto the end of a list
##Append

    # Change a specified element within a list at the given index
my_list =  [10, 20, 30, 40, 50]
index_to_change = 2
new_value = 35

my_list[index_to_change] = new_value
print(my_list)






    # Remove a specified object from a list

my_list = [1, 2, 3, 4, 5, 6, 7]
my_list.remove(6)
print(my_list)


##Or

my_list = [1, 2, 3, 4, 5, 6, 7]
object_to_remove = 6

my_list.remove(object_to_remove)
print(my_list)




    # Remove the object at the index specified

my_list = [1, 2, 3, 4, 5, 6, 7]
del my_list[5]
print(my_list)



    # Functions for accessing information about a list







my_list = [10, 20, 30, 40, 50]
variable_length = len(my_list) ##length of a list
print(variable_length)
##or 
print(len(my_list)) #Without assinging a variable.


##index function method returns the index of the first occurrence of a specified value in th list. 
my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))

##Or with a variable.
my_list = [10, 20, 30, 40, 50]
index = my_list.index(30)
print(index)  # Output: 2

##count
my_list = [10, 20, 30, 20, 40, 50, 20]
count = my_list.count(20)
print(count)  # Output: 3
 

## in operator: you can also use the in operator to check if an element is present in the list.

my_list = [10, 20, 30, 20, 40, 50, 20]
if 30 in my_list:
    print("ye 30 in list")
   










    # Define a list named scores
scores = [92, 87, 68, 75, 96]




    # Return the max (or highest value) item in a list

scores = [92, 87, 68, 75, 96]
variable = max(scores)
print(variable)



    # Return the min (or lowest) item in a list

scores = [92, 87, 68, 75, 96]
variable = min(scores)
print(variable)



    # Return the sum of the items in a list

scores = [92, 87, 68, 75, 96]
variable = sum(scores)
print(variable)



    # Return the length of the list

scores = [92, 87, 68, 75, 96]
variable = len(scores)
print(variable)



    # Use sum and len to calculate average


scores = [92, 87, 68, 75, 96]
average = sum(scores) / len(scores)
print(average)



    # Create a tuple, a sequence of immutable Python objects that cannot be changed

tup = (1, 2, 3)



# Information functions also work on tuples, provided they contain valid data
# types
