# # Todo: 1
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# # Todo: 2
# questions = ['name', 'quest', 'favorite color']
# answer = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answer):
#     print('What is {0}? It is {1}.'.format(q, a))

# # Todo: 3
# for i in reversed(range(1, 10, 2)):
#     print(i)

# # Todo: 4
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# Todo: 5
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)