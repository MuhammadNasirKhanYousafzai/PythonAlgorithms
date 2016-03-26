import Node
def QuickSort(head,last):
     '''Merge sort
                    this function is used to merge linked list

     '''
    # print head.getData(),last.getData()
     if head==None or head==last:
        return
     povit=partition(head,last)
     QuickSort(head,povit)
     QuickSort(povit.getNext(),last)




def partition(head,last):
    povit=head.getData()
    sort=head
    head=head.getNext()
    less=[]
    greater=[]
    while head!=last.getNext():
      if povit<head.getData():
          greater.append(head.getData())
      else:
          less.append(head.getData())
      head=head.getNext()

    for i in less:
        sort.setData(i)
        sort=sort.getNext()
    sort.setData(povit)
    seletedpovit=sort
    sort=sort.getNext()
    for i in greater:
        sort.setData(i)
        sort=sort.getNext()

    return seletedpovit




