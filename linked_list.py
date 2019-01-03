class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count
    
    def insert(self, data):
        # Insert at beginning
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None
    
    def deleteAt(self, i):
        if i > self.count-1:
            return
        # head
        if i == 0:
            self.head = self.head.get_next()
        else:
            temp_index = 0
            node = self.head
            while (temp_index < i - 1):
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def print_list(self):
        temp_node = self.head
        while (temp_node != None):
            print("Node: ", temp_node.get_data())
            temp_node = temp_node.get_next()


# Create a LinkedList and insert some nodes
List = LinkedList()
List.insert(38)
List.insert(49)
List.insert(13)
List.insert(15)
List.print_list()

# Exercise the list
print("Item count: ", List.get_count())
print("Finding item: ", List.find(13))
print("Finding item: ", List.find(78))

# Delete an item
List.deleteAt(3)
print("Item count: ", List.get_count())
print("Finding item: ", List.find(38))
List.print_list()