# Our games' inventory needs some additional features to help keep track of the items inside of it.
#
# Implement the count_potions function. It should take a list of our players' inventory (strings) as input and return
# the number of times Healing potion shows up in the list as an integer.
#
# For example
#
# count = count_potions(['Short sword', 'Bread', 'Healing potion', 'Healing potion'])
# print(count)
# prints "2"
def count_potions(inventory):
    return sum(1 for x in inventory if x == "Healing potion")


# LIST INDEXING
# While iterating over each item in a list is O(n), not every lookup strategy based on lists falls into the same category.
#
# Array indexing accesses an element in an array using its index number.
#
# ASSIGNMENT
# Our players need the option to find the last item in their inventory.
#
# Implement the last_item function. It should take a list of our player's inventory (strings) and return the last element in the list.
def last_item(inventory):
    return inventory[-1] if len(inventory) != 0 else None


"""
ASSIGNMENT
Some of our players have older computers, and they've noticed that our game is crashing because it requires too much memory. 
We've narrowed down the issue to the attack_action() function. Let's debug the function call stack and visualize 
which functions are being called from within.

Modify attack_action to call functions shoot_arrow and calc_new_health using call()
We have to make sure our shoot_arrow function is calculating the damage it will deal.

Modify shoot_arrow to call calc_damage using call()
Now that we know how much damage our arrow will do, we need to apply that damage to the target.

Modify calc_damage to call apply_damage using call()""

"""


def attack_action():
    call(shoot_arrow)
    call(calc_new_health)


def shoot_arrow():
    call(calc_damage)


def calc_damage():
    call(apply_damage)

    # don't touch below this line


def calc_new_health():
    pass


def apply_damage():
    pass


"""
STACK IMPL
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


stack = Stack()


def call(func):
    stack.push(func.__name__)
    print("Pushing " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")
    func()
    stack.pop()
    print("Popping " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")


call(attack_action)


def is_balanced(input_str):
    size = 0
    stack = Stack()
    for char in input_str:
        if stack.peek() == '(' and char == ')':
            stack.pop()
            size -= 1
        else:
            stack.push(char)
            size += 1
    return size == 0


class PotionStack(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        if self.peek() == item:
            return
        super().push(item)


"""
QUEUE IMPL
"""


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


"""
LL IMPL
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
