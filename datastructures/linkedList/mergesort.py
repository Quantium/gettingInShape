def mergeLists(head1, head2):
    holder=[]
    index1=head1
    index2=head2
    while index1 != None or index2 != None:
        if index1 != None:
            holder.append(index1)
            index1=index1.next   
        if index2 != None:
            holder.append(index2)
            index2=index2.next
    
    holder=sorted(holder,key=lambda a : a.data)
    hl=len(holder)
    for i,node in enumerate(holder):
        if i < hl-1:
            node.next = holder[i+1]
        else:
            node.next = None
    return holder[0]

## VS

def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return None
  
    if head1 is None:
        return head2

    if head2 is None:
        return head1
    
    if head1.data < head2.data:
        smallerNode = head1
        smallerNode.next = mergeLists(head1.next, head2)
    else:
        smallerNode = head2
        smallerNode.next = mergeLists(head1, head2.next)
    
    return smallerNode