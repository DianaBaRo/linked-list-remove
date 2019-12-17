#remove
def remove (self, data):
    #if list is empty
    if self.head is None:
        return;

    self.size = self.size - 1;

    currentNode = self.head;
    previousNode = None;

    while currentNode.data != data:
        previousNode = currentNode;
        currentNode = currentNode.nextNode;

    if previousNode is None:
        self.head = currentNode.nextNode;
    else:
        previousNode.nextNode = currentNode.nextNode;
    
