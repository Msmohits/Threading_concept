#  import threading library to use.
import threading
#  import time for time management
import time


# created a function for thread.
def emp():
    for i in range(4):
        id = "your id is 1 \n"
        name = "your name is Mohit\n"
        print(id, name)
        time.sleep(1)
    print("thread one completed\n")


# Created another function for thread.
def student():
    for i in range(4):
        print("That's thread 2 work\n ")

        time.sleep(1)
    print("thread 2 completed\n")


# created to threads .
threading.Thread(target=emp()).start()
threading.Thread(target=student()).start()
