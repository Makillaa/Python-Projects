# This code implements how the python zip function works
x = 'abcd'
y = [1, 2, 3, 4, 5]

def smallest_object(*args): # Function to find the smallest number of elements in a list, accepts iterators
    return range(len(sorted(args, key=len)[0])) # Returns the object with the fewest elements. sorted sorts
    # in length, len takes the smallest object in length (at index 0) and returns the number of elements,
    # range generates a number - which returns len

genr = ( (x[i], y[i]) for i in smallest_object(x, y) ) # We make a generator, where we get pairs of elements from two
# of objects, limited by the length of the smallest object

for item in genr: # We go through these pairs, in the generator and display each of them
    print(item)