inventory = {
    'gold': 500,
    # Assigned a new list to 'pouch' key
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# 2. Sort the list under the 'backpack' key
inventory['backpack'].sort()

# 3. Remove 'dagger' from the 'backpack' list
inventory['backpack'].remove('dagger')

# 4. Add 50 to the number stored under 'gold'
inventory['gold'] = inventory['gold'] + 50