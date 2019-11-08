import random

#Trying to improve results implementing queue

#Determine queue node, queue, and dequeue

class QueueNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None

    def enqueue(self, value):
        newNode = QueueNode(value)
        self.size += 1
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def dequeue(self):
        if not self.head:
            return None
        self.size -= 1
        if not self.size:
            current_head = self.head
            self.head = None
            return current_head.value
        current_head = self.head
        self.head = self.head.next
        self.head.prev = None
        return current_head.value

class Graph:
    def __init__(self, data):
        self.graph = data
        self.size = len(data)
        self.savedPaths = {}

    def getExits(self, room, exclude=-1):
        return [self.graph[room][i] for i in self.graph[room] if self.graph[room][i] != exclude]

#Bredth first search
#Explore the vertex
  #While +1 unscheduled vertices adjacent to current vertex
  #i. schedule adjacent vertex to be explored [queue]
#Mark vertex as explored

    def bfs(self, start, finish):
        queue = Queue()
        queue.enqueue([start])
        visited = set()
        bestPath = None
        bestLength = 0
        while queue.size:
            current = queue.dequeue()
            currentRoom = current[-1]
            visited.add(currentRoom)
            if currentRoom == finish:
                if not bestLength or len(current) < bestLength:
                    bestPath = current
                    bestLength = len(bestPath)
            else:
                for dir in self.graph[currentRoom]:
                    dest = self.graph[currentRoom][dir]
                    if dest not in visited:
                        queue.enqueue(current + [dest])

        if bestLength:
            bestPath.pop(0)
            return bestPath
        return None

