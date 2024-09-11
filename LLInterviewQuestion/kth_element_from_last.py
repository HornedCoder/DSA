from LinkedList import LinkedList

def kth_element_from_last(ll,k):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(k):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    
    return pointer1

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(kth_element_from_last(customLL,4 ))