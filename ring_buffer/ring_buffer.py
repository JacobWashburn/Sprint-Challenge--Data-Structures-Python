from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        s = self.storage
        if len(self.storage) == self.capacity:
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

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
