from LinkedList import LinkedList

def Sum(l1,l2):
    pointer1 = l1.head
    pointer2 = l2.head
    l3 = LinkedList()
    carry = 0

    while pointer1 and pointer2:
        result = carry
        if pointer1:
            result += pointer1.value
            pointer1 = pointer1.next
        if pointer2:
            result += pointer2.value
            pointer2 = pointer2.next
        
        l3.add(int(result%10))
        carry = result/10

    return l3

customLL1 = LinkedList()
customLL2 = LinkedList()
customLL1.generate(3,0,9)
customLL2.generate(3,0,9)
print(customLL1)
print(customLL2)
print(Sum(customLL1,customLL2))
