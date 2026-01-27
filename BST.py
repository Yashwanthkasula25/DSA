class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
##
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def postorder_traversal(self):
        elementt = []


        elementt.append(self.data)
        if self.left:
            elementt += self.left.in_order_traversal()
        if self.right:
            elementt += self.right.in_order_traversal()

        return elementt

    def preorder_traversal(self):
        element = []
        if self.left:
            element += self.left.in_order_traversal()
        if self.right:
            element += self.right.in_order_traversal()

        element.append(self.data)



        return element

    def totalsum(self):
        return sum(self.in_order_traversal())

    def findmin(self):
        return min(self.in_order_traversal())


    def findmax(self):
        return max(self.in_order_traversal())


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("sum is",numbers_tree.totalsum())
    print(numbers_tree.findmin())
    print(numbers_tree.findmax())
    print("In order traversal gives this sorted list:", numbers_tree.preorder_traversal())
    print("In order traversal gives this sorted list:", numbers_tree.postorder_traversal())