# def bubblesort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
                
# my_list = [1,7,18,21,4,5,20,22,10]

# print(my_list)

# bubblesort(my_list)

# print(my_list)

class Node():
    
    def __init__ (self, value, nextnode = None):
        self.value = value
        self.next_node = nextnode

    def get_next (self):
        return self.next_node

    def set_next (self, nextnode):
        self.next_node = nextnode

    def get_value (self):
        return self.value

    def set_data (self, value):
        self.value = value


class Linked_listnode():

    def __init__(self, rightnode = None):
        self.head = rightnode
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, value):
        new_node = Node (value, self.head)
        self.head = new_node
        self.size += 1
        
    def insert(self,prev_node, value):
        if prev_node is None:
            print("The given previous node must not be empty!")
            return
        new_node = Node(value)       
        new_node.nextnode = prev_node.nextnode 
        prev_node.nextnode = new_node

    def remove (self, value):
        node = self.head
        previews_node = None

        while node:
            if node.get_value() == value:
                if previews_node:
                    previews_node.set_next(node.get_next())
                else:
                    self.head = node.get_next()
                self.size -= 1
                return True	
            else:
                previews_node = node
                node = node.get_next()
        return False  

    def find (self, value):
        node = self.head
        while node:
            if node.get_value() == value:
                return value
            else:
                node = node.get_next()
        return None

my_list = Linked_listnode()
my_list.add("Shoulder")
my_list.add("mover")
my_list.add("Ku")
my_list.add("lydia")
my_list.add(10)
my_list.add(12)


# get the size of input 
print(f"There are total {str(my_list.get_size())} node") 

# remove the size 10 
my_list.remove(10)

# display the size again and reduces one                       
print(f"One node have been removeand There are {str(my_list.get_size())} node left") 

my_list.insert(my_list.head.next_node, "Nathan")
# checking if the the vulue exist then return the value, if not then return " NONE"
print(f"The value you try to get is {my_list.find('Shoulder')}")
# display the output

print(f"The value you try to get is {my_list.find(12)}")
