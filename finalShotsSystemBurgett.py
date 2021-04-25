"""
Name            : finalShotsSystemBurgett.py
Author          : Chadwick Burgett
Created         : 04/24/2021
Course          : CIS 152 Data structures
Version         : 1.0
Copyright       : This is my own original work based on
                specifications issued by our instructor
                and ideas I researched on several different
                internet sites.
Description     : This program creates a vaccine shot system, at an administration
level. It uses a stack for the shots and a priority queue for the people. It uses Tkinter
for GUI from finalGuiBurgett.py.
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access to
my program.
"""
import random as rand
from tkinter import *


class LLFUllException(Exception):  # This is an exception class
    pass


class LLEmptyException(Exception):  # This is an exception class
    pass


class ShotsStack:
    # This is the class that handles the shots in a stack format.
    def __init__(self):
        """
        This is the constructor for the ShotStack. It sets the number of shots,
        where the top is, max size, a list of shots and keeps track of the number of shots given
        """
        self.stock_of_shots = 0
        self.top = -1
        self.max_size = 1000000
        self.shots = ["" for x in range(self.max_size)]
        self.shot_number = 0

    def is_empty(self):
        """
        This checks if the ShotsStack is empty.
        :return: A bool of whether the stack is empty.
        """
        if self.top < 0:
            return True
        else:
            return False

    def is_full(self):
        """
        This checks if the ShotsStack is full
        :return: A bool of whether the stack is full
        """
        return self.top == self.max_size - 1
        # This return statement will return a bool of true if top == maxSize -1, or in other words is full, and false otherwise.

    def push(self, num):
        """
        This function pushes a number of shots onto the stack.
        :param num: This is the number to increase the stack
        :return: The number of shots on the stack.
        """
        for a in range(0, num):
            # This for loop adds the shot number to the stack and increases size.
            self.shot_number += 1
            self.shots[self.top] = self.shot_number  # This adds the shots to the stack
        self.top = self.top + 1  # This iterates top
        self.stock_of_shots += num
        return self.stock_of_shots

    def pop(self, num):
        """
        This function decreases the stack by the number passed in.
        :param num: This is the number to decrease the stack by.
        :return: The new number of shots left in the stack
        """
        if self.stock_of_shots > num:
            self.stock_of_shots -= num
            return self.stock_of_shots
        else:
            temp = num - self.stock_of_shots
            self.stock_of_shots = 0
            return temp

    def peek(self):
        """
        This is not actually used in my program but it would allow the user to see the top shot.
        :return:
        """
        if not self.is_empty():  # This makes it so it only continues if the stack is not empty.
            self.top = self.top - 1  # This makes it so the top points at the last item inserted.
            return self.shots[self.top]  # This was written to iterate inside this line but it needed to iterate after this line.
            # self.top = self.top + 1
        else:
            print("The stack is Empty")

    def size(self):
        """
        This returns the size of the stack
        :return: The size of the stack
        """
        # return self.top + 1  # This returns the size of the current stack.
        return self.stock_of_shots

    def print_stack_up(self):
        """
        This returns the stack.
        :return: The stack is returned
        """
        stack_str = ""
        if not self.is_empty():
            for x in self.shots:
                stack_str = x + "\n" + stack_str
        else:
            print("The stack is Empty")
        return stack_str


class Node:
    # This is the Node class and the constructor for it
    def __init__(self, jn, p):
        self.job_num = jn  # This is the number associated with a person in our system.
        self.priority = p  # This is the priority level, A-D, in our system
        self.next_val = None  # This sets the next_val for each node


class PriorityQueue:
    # This is the class for the Priority Queue
    def __init__(self):
        # This is the constructor for the class, it implements the class.
        self.head_val = None
        self.max_size = sys.maxsize
        self._size = 0
        self.person = 100

    def is_empty(self):
        # This checks if the priority queue is empty
        return self.head_val is None

    def is_full(self):
        # This checks if the priority queue is full
        return self._size == self.max_size

    def enqueue(self, job, pri):
        """
        This function adds a new node into the priority queue
        :param job: This is the five digit job number to be added
        :param pri: This is the priority level to be added to node
        :return: None
        """
        if self.is_full() is False:  # This checks that the PriorityQueue is not full.
            if self.is_empty() is True:  # This checks if the PriorityQueue is empty.
                self.head_val = Node(job, pri)  # If the PriorityQueue is empty then the head_val is set to Node
                self._size += 1  # This iterates size
            else:
                # This checks if the head_val has a higher priority than the new one.
                if self.head_val.priority > pri:
                    new_node = Node(job, pri)  # This sets the new node to a temp node.
                    new_node.next_val = self.head_val  # This sets the next val for the new node to head_val
                    self.head_val = new_node  # This sets the temp node to head_val
                    self._size += 1  # This iterates size
                else:
                    temp = self.head_val  # This sets the head_val to temp so I can iterate through the queue
                    # This while loop iterates through the PriorityQueue.
                    while temp.next_val:
                        # This checks if the new priority level is smaller or equal too the current priority level
                        if pri <= temp.next_val.priority:
                            break
                        temp = temp.next_val  # This sets the next val
                    new_node = Node(job, pri)  # This sets the new node to a temp node.
                    new_node.next_val = temp.next_val  # This sets the new nodes next to the prior node
                    temp.next_val = new_node  # This sets the prior next to the new node
                    self._size += 1  # This iterates size

        else:  # If the LinkedList is full it gives an error
            raise LLFUllException("The PriorityQueue is Full.")

    def dequeue(self):
        """
        This function removes the first item in the PriorityQueue
        :return: none
        """
        if not self.is_empty():  # This checks if the PriorityQueue is not empty and raises an error if it is.
            # Since the enqueue already adds items in the correct order I only have to remove the first item.
            temp = str(self.head_val.job_num) + str(self.head_val.priority)  # This sets the current person to a string.
            self.head_val = self.head_val.next_val  # This assigns head_val to the next item in line
            self._size -= 1  # This subtracts 1 from the size.
            return temp  # This is the personal number and priority level for the person deleted from the system.
        else:  # If the queue is empty it raises an exception
            raise LLEmptyException("The PriorityQueue is Empty")

    def size(self):
        """
        This returns the size of the queue
        :return: The size of the queue
        """
        return self._size

    def peek(self):
        """
        This function returns the first item in a string
        :return: String of first item
        """
        if not self.is_empty():  # This checks if the PriorityQueue is not empty and raises an error if it is.
            return self.head_val.job_num + ": " + str(self.head_val.priority)
        else:  # If the queue is empty it raises an exception
            raise LLEmptyException("The PriorityQueue is Empty")

    def list_print(self):
        """
        This function prints out the linked list
        :return: none
        """
        print_val = self.head_val  # This sets a variable to the head value
        while print_val:  # This while loop runs through the entire linked list
            print(str(print_val.job_num) + " : " + print_val.priority)  # This prints the can object for the current pointer
            print_val = print_val.next_val  # This sets the variable to the next value

    def insert_persons(self, num):
        """
        THis function adds people into a priority queue
        :param num: This is the number of people to input
        """
        count = 0
        while count < num:
            person = self.person
            self.person += 1
            security_level = chr(rand.randint(ord('A'), ord('D')))  # This sets a random priority level between A-D.
            self.enqueue(person, security_level)
            count += 1


def user_input(choice, num, p, s):
    """
    This function starts the users input section. It is how the user interacts with the system.
    :param choice: This is the users choice of shot or person.
    :param num: This is the number to change the system
    :param p: THis is the person or priority queue that is passed in.
    :param s: This is the shot that is passed in.
    :return: This returns a message about the shots or people inserted.
    """
    person = p
    shots = s
    if choice == 1:  # This runs if the user set choice to shot
        shots.push(num)  # This pushes the number of shots into the system
        if person.size() != 0:  # If people in the system is not 0, the set_sized function is called.
            message = set_sizes(shots, person)
        else:  # If people is 0 then the message is set here.
            message = 'There are ' + str(shots.stock_of_shots) + ' shots left in the system.'
        return message

    elif choice == 2:  # This runs if the user set choice to person
        person.insert_persons(num)  # This pushes the number of people into the system
        if shots.stock_of_shots != 0:  # If shots in the system is not 0, the set_sized function is called.
            message = set_sizes(shots, person)
        else:  # If shots is 0 then the message is set here.
            message = 'There are ' + str(person.size()) + ' people left in the system.'
        return message


def set_sizes(s, p):
    """
    This function is called to set the message for the user and set the correct shot or person size.
    :param s: THis is the shot being passed in
    :param p: This is the person being passed in
    :return: This returns the correct message about who got shots and how many if any of either are left.
    """
    if s.stock_of_shots > p.size():  # If there are more shots than people in the system this runs
        temp = p.size()  # This sets the size of person to temp
        s.pop(p.size())  # This pops the shots by the number of people.
        person_details = ''
        for a in range(0, p.size()):
            # This for loop sets the people that received shots and dequeue them.
            if a == 0:
                person_details = person_details + p.dequeue() + ", "
            elif a % 8 == 0:  # This sets every 8 people to a new line.
                person_details = person_details + p.dequeue() + ",\n "
            else:
                person_details = person_details + p.dequeue() + ", "
        message = str(temp) + ' shots were given to the following people.\n' + str(person_details) + '\nThere are ' + str(s.stock_of_shots) + ' shots left in the system.'
    else:
        temp = s.stock_of_shots
        people_left = s.pop(p.size())
        person_details = ''
        for a in range(0, temp):
            if a == 0:
                person_details = person_details + p.dequeue() + ", "
            elif a % 8 == 0:
                person_details = person_details + p.dequeue() + ",\n "
            else:
                person_details = person_details + p.dequeue() + ", "
        message = str(temp) + ' shots were given to the following people.\n' + str(person_details) + '\nThere are ' + str(people_left) + ' people left in the system.'
    return message


if __name__ == '__main__':
    person1 = PriorityQueue()
    shot1 = ShotsStack()
    c = 1
    n = 10
    print(user_input(c, n, person1, shot1))
