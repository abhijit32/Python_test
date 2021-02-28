import random
import math
import time

def divide(num1,num2):
    if num2 == 0:
        raise ValueError
    return num1/num2


def binarySearch(input_list,number_to_find):
    
    processed_list = input_list
    processed_list.sort()

    #Find the middle number 
    while 1:

        #When the list is trimmed down to just one element 
        if len(processed_list) == 1:
            if number_to_find == processed_list[0]:
                print(f"Number {number_to_find} found")
                break
            else:
                print(f"Number {number_to_find} does not exist in the list")
                break

        #Continue the logic with trimed down list
        else:
            middle_index = math.ceil(len(processed_list)/2)
            middle_number = processed_list[middle_index]
            
            if middle_number == number_to_find:
                print(f"Number {number_to_find} found")
                break

            elif number_to_find > middle_number:
                processed_list = processed_list[middle_index+1: ]
                

            elif number_to_find < middle_number:
                processed_list = processed_list [0:middle_index]

def createBinaryTree():
    pass


MY_RANGE = 40
mY_list = random.sample(range(1,100),MY_RANGE)
mY_list.sort()
print(mY_list)
number = int(input("Searh for the number : "))


start_binarySearch = time.time()
binarySearch(mY_list, number)
end_binarySearch = time.time()

print(f"time taken for binary search {end_binarySearch - start_binarySearch}")

