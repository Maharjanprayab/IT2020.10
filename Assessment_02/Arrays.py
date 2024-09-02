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
    test1 = My_array(10)#Creating an object as array named test1 with size 10
    length1 = len(test1)

    for i in range(length1):
        if i < len(test):
            test1[i] = test[i]
        else:
            test1[i] = random.randint(0, 99)

    print(f"Contents of test1 array are: {test1}")

if __name__ == "__main__":
    test, length = test_array()#Create and populate test array
    test1_array(test)#Create and populate test1 array based on test array
    del test #Explicitly dereferencing 'test' for demosnstration.