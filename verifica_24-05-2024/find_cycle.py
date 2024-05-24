class LinkedList:
    
    def __init__(self,node, next) -> None:
        
        self.node = node
        self.next = next
        
def has_cycle(head: Node) -> list[int]:
    pass



 	

ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head))  #Output True