import random
import time

#Properties
#1. Difficulty

#Methods
#1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
#length will be difficulty.
#2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
#will be in the size of difficulty.
#3. is_list_equal - A function to compare two lists if they are equal. The function will return
#True / False.
#4. play - Will call the functions above and play the game. Will return True / False if the user
#lost or won.

def generate_sequence(difficulty):
    Random_List = [random.randint(0, 10) for i in range(difficulty)]
    return Random_List



def get_list_from_user(difficulty):
    # creating an empty list
    Input_List = []

    # number of elements as input
    Number_Elements = difficulty

    # iterating till the range
    for i in range(Number_Elements):
        print("please enter number:", i + 1)
        try:
            ele = int(input())
            Input_List.append(ele)  # adding the element

        except ValueError:
            print("I am afraid %s is not a number" % i)
            break

    print(Input_List)
    return Input_List


def is_list_equal(Random_List,Input_List):
    if (Random_List == Input_List):
        return "Equal"
    else:
        return "Non equal"

def play():
    Random_List = generate_sequence(5)
    print(Random_List)
    timeout = time.time() + 3  # 3 seconds from now
    while True:
        if time.time() > timeout:
            break
    Input_List = get_list_from_user(5)
    IS_Equal=is_list_equal(Random_List,Input_List)
    print(IS_Equal)



play()

#generate_sequence(5)
#get_list_from_user(5)
#l1=[1,2,3]
#l2=[1,2,3]
#IS_Equal = is_list_equal(l1,l2)
#print(IS_Equal)