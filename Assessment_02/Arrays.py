import random

class My_array:

    def __init__(self, size):
        self.array = [random.random() for i in range(size)]
        self.logical_length = size
        self.physical_length = size * 2

    def __setitem__(self, index, value):
        if 0 <= index < self.logical_length:
            self.array[index] = value
        else:
            raise IndexError("Index is out of range.")

    def __getitem__(self, index):
        if 0 <= index < self.logical_length:
            return self.array[index]
        raise IndexError("Index is out of range.")

    def __len__(self):
        return self.logical_length
    
    def __str__(self) -> str:
        return str(self.array[:self.logical_length])
    


def test_array():
    test = My_array(5)#Creating an object as array named test with size 5
    length = len(test)
    for i in range(length):
        value = random.randint(0,99)
        test[i] = value
    print(f"Contents of test array are: {test}")
    return test, length

def test1_array(test):
    go = input("Press any key to continue")
    test1 = My_array(10)#Creating an object as array named test1 with size 10
    length1 = len(test1)

    for i in range(length1):
        if i < len(test):
            test1[i] = test[i]
        else:
            test1[i] = random.randint(0, 99)

    print(f"Contents of test1 array are: {test1}")
    return test1, length1

def selection_sort(arr):
    i_range = len(arr)
    print(f"test1 = {arr}")
    for i in range(i_range):
        min_index = i
        print(f"We assume test1[{i}] = {arr[i]} as minimun value and compare minimun value with every other value on the right-hand side of the value")
        for j in range(i+1, i_range):
            print(f"j = {j}")
            if arr[j] < arr[min_index]:
                min_index = j
            
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"test1 = {arr}")
    print(f"Array after the selection sort is {arr}")

def bubble_sort(arr):
    i_range = len(arr)
    for i in range(i_range):
        j_range = i_range - i -1
        for j in range(j_range):
	        if arr[j]>arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f"Array after the bubble sort is {arr}")

def sorting(agr):
    go = input("Press any key to continue")
    print(f"Choose a method of sorting.")
    print(f"    1 Bubble sort")
    print(f"    2 Selection sort")

    while True:
        choice = int(input(f"Enter a number [1 or 2]: "))
        if choice == 1:
            bubble_sort(agr)
            break
        elif choice == 2:
            selection_sort(agr)
            break
        else:
            print(f"Invalid value. Please enter 1 or 2.")


if __name__ == "__main__":
    test, length = test_array()#Create and populate test array
    test1, length1 = test1_array(test)#Create and populate test1 array based on test array
    sorting(test)
    del test #Explicitly dereferencing 'test' for demosnstration.