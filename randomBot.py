import random

def botInput(array, mark):
    field = random.randint(0, 8)
    correct = False
    if(array[field] == " "):
        array[field] = mark
        correct = True
    return correct