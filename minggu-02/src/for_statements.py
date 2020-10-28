# words = ['cat', 'windows', 'defenestrate']
# for w in words:
#     print(w, len(w));

users = {'Triwibowo': 'active', 'Ridho': 'active', 'Permana': 'inactive'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    
print(active_users)
