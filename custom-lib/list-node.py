import collections

ListNode = collections.namedtuple('ListNode', ['val', 'next'])

ln = ListNode(val=1, next=ListNode(val=2, next=None))

print(ln)

class ListNodeContainer:
    def __init__(self, items):
        self._items = [ListNode(val=item, next=None) for item in items]

    def __len__(self):
        return len(self._items)

    def __getitem__(self, position):
        return self._items[position]

lnc = ListNodeContainer([1, 2, 3])
print(len(lnc))
print(lnc[0])
