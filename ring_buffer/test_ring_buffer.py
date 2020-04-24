import unittest
from ring_buffer import RingBuffer, ArrayRingBuffer


class RingBufferTests(unittest.TestCase):
    def setUp(self):
        self.buffer = RingBuffer(5)
        self.buffer_2 = RingBuffer(5)

    def test_ring_buffer(self):
        self.assertEqual(self.buffer.storage.length, 0)

        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.assertEqual(self.buffer.storage.length, 4)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd'])

        self.buffer.append('e')
        self.assertEqual(self.buffer.storage.length, 5)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd', 'e'])

        self.buffer.append('f')
        self.assertEqual(self.buffer.storage.length, 5)
        self.assertEqual(self.buffer.get(), ['f', 'b', 'c', 'd', 'e'])

        self.buffer.append('g')
        self.buffer.append('h')
        self.buffer.append('i')
        self.assertEqual(self.buffer.storage.length, 5)
        self.assertEqual(self.buffer.get(), ['f', 'g', 'h', 'i', 'e'])

        self.buffer.append('j')
        self.buffer.append('k')
        self.assertEqual(self.buffer.get(), ['k', 'g', 'h', 'i', 'j'])

        for i in range(50):
            self.buffer_2.append(i)
        self.assertEqual(self.buffer_2.get(), [45, 46, 47, 48, 49])


class ArrayRingBufferTests(unittest.TestCase):
    def setUp(self):
        self.buffer = ArrayRingBuffer(5)
        self.buffer_2 = ArrayRingBuffer(5)

    def test__array_ring_buffer(self):
        self.assertEqual(len(self.buffer.storage), 5)

        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.assertEqual(5, len(self.buffer.storage))
        self.assertEqual(['a', 'b', 'c', 'd'], self.buffer.get())

        self.buffer.append('e')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], self.buffer.get())

        self.buffer.append('f')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(['f', 'b', 'c', 'd', 'e'], self.buffer.get())

        self.buffer.append('g')
        self.buffer.append('h')
        self.buffer.append('i')
        self.assertEqual(5, len(self.buffer.storage))
        self.assertEqual(['f', 'g', 'h', 'i', 'e'], self.buffer.get())

        for i in range(50):
            self.buffer_2.append(i)
        self.assertEqual([45, 46, 47, 48, 49], self.buffer_2.get())


if __name__ == '__main__':
    unittest.main()
