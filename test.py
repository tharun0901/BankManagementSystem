def list(head):
    prev=None
    curr=head
    # while curr:
    #     nxt=curr.next
    #     curr.next=prev
    #     prev=curr
    #     curr=nxt
    # return prev
    print(reversed(head))
n=int(input("Enter the number:"))
list(n)