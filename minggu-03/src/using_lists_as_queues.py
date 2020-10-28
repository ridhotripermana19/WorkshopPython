from collections import deque

queue = deque(["Eric", "John", "Michael"])
print('Add Terry on list')
queue.append("Terry")
print('Add Graham on list')
queue.append("Graham")
print(queue)
print('Remove item on the list which is', queue.popleft())
print('Remove item on the list which is', queue.popleft())
print(queue)