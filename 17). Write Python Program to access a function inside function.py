#17). Write Python Program to access a function inside function

def demo():
    print("This is demo Function")
def test():
    print("This is test function")
    demo()

test()
