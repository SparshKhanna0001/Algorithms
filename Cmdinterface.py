import sys

from SearchAlgorithms import BinarySearch as bi
from SearchAlgorithms import LinearSearch as li
from SearchAlgorithms import JumpSearch as js

from SortingAlgorithms import BubbleSort as bs
from SortingAlgorithms import SelectionSort as ss

opening_msg = "Hey There! You are currently using the algorithm facility."
commands_msg0 = "You can access the following algorithms with help of commands displayed alongside the name of algorithm."
cammands_msg1 = "Definitions - to know about of the definitions of certain algorithms - d"
commands_msg2 = "Linear Search Algorithm - li"
commands_msg3 = "Binarty Search Algorithm - bi"
commands_msg4 = "Jump Search Algorithm - js"
commands_msg5 = "Bubble Sort Algorithm - bs"
commands_msg6 = "Selection Sort Algorithm - ss"
commands_msg7 = "To quit - q"
asteriks = "*"*50
end_line_character = "\n"


def input_processing(input: str) -> list or bool:
    try:    
        array = input.split(", ")
        array = list(map(lambda x: int(x), array))
        return array
    except:
        return False

array = "4, 5, 6, 7, 4, 4"
array = input_processing(array)
print(type(array))
# while True:

#     operation: str = input("Please enter the command you want to access.")
    
#     if operation.lower() == "d":
#         command_definition = "You can access the following definitions with the help of the following commands:-"
#         print(f"""{command_definition} \n{asteriks} \n{commands_msg2} \n{commands_msg3} \n{commands_msg4} \n{commands_msg5} \n""")
#         operation_definition = input(">>>")
        
#         if operation_definition.lower() == "bs":
#             print(SearchAlgorithms.BinarySearch.define())
#         elif operation_definition.lower() == "li":
#             print(SearchAlgorithms.LinearSearch.define())
#         elif operation_definition.lower() == "js":
#             print(SearchAlgorithms.JumpSearch.define())
#         elif operation_definition.lower() == "bs":
#             print(SortingAlgorithms.JumpSearch.define())
#         else:
#             print("I don't understand that...\nPlease try a valid command.")
    
#     elif operation.lower() == "bs":
#         array = input

# """The basic problem i m currently facing now is that when array is received as input,  """
