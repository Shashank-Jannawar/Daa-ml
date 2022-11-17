import heapq


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq

        self.huff = ""
        self.left = left
        self.right = right

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def printNode(root, curr):
    curr += root.huff
    if(root.left):
        printNode(root.left, curr)
    if(root.right):
        printNode(root.right, curr)

    if(not root.left and not root.right):
        print(root.char, curr)


chars = ['a', 'b', 'c', 'd', 'e']
freqs = [1, 2, 3, 4, 5]

arr = []
for i in range(len(chars)):
    heapq.heappush(arr, Node(chars[i], freqs[i]))

while len(arr) > 1:
    left = heapq.heappop(arr)
    right = heapq.heappop(arr)

    left.huff = '0'
    right.huff = '1'
    heapq.heappush(arr, Node(left.char+right.char,
                             left.freq+right.freq, left, right))

printNode(arr[0], "")
