from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        s = self.storage
        if len(s) == self.capacity:
            if self.current.next is None:
                s.remove_from_head()
                new_current = s.add_to_head(item)
                self.current = new_current
            else:
                new_current = self.current.replace_next_node(item, self.current.next.next)
                self.current = new_current
        else:
            new_current = s.add_to_tail(item)
            self.current = new_current

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while True:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            if node.next is not None:
                node = node.next
            else:
                break

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def __len__(self):
        return self.capacity

    def append(self, item):
        s = self.storage
        c = self.current
        if c:
            if not s[c] and len(s[c:]) == 1:
                s[c] = item
                self.current = 0
            else:
                s[c] = item
                if c < len(self) - 1:
                    self.current += 1
                else:
                    self.current = 0
        else:
            s[c] = item
            self.current += 1

    def get(self):
        return [v for v in self.storage if v]
