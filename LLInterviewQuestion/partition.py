from LinkedList import LinkedList

def partition(ll,x):
    current = ll.head
    ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if x > current.value:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL,50)
print(customLL)