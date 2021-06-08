class PhoneBook(object):
    def __init__(self):
        pass

    def size(self):
        pass

    def insert(self, name, phone_number):
        pass

    def find(self, name):
        pass

class ListPhoneBook(PhoneBook):
    def __init__(self):
        super().__init__()
        self.list_pb = []

    def size(self):
        return len(self.list_pb)

    def insert(self, name, phone_number):
        self.list_pb.append({"name": name, "phone_number": phone_number})

    def find(self, name):
        phone = -1
        for contact in self.list_pb:
            if contact["name"] == name:
                phone = contact["phone_number"]
        return phone


class BinarySearchTreePhoneBook(PhoneBook):

    class Node:

        def __init__(self, name, phone_number):
            self.name = name
            self.phone_number = phone_number
            self.left = None
            self.right = None

    def __init__(self):
        super().__init__()
        self.root = None
        self.tree_size = 0

    def size(self):
        return self.tree_size

    def insert(self, name, phone_number):
        self.tree_size += 1
        if not self.root:
            self.root=self.Node(name, phone_number)
            return
        current_node = self.root
        while True:
            if name < current_node.name:
                if not current_node.left:
                    current_node.left = self.Node(name, phone_number)
                    return
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = self.Node(name, phone_number)
                    return
                else:
                    current_node = current_node.right

    def find(self, name):
        if not self.root: return -1
        current_node = self.root
        while current_node and current_node.name != name:
            if name < current_node.name:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node.phone_number if current_node else -1
