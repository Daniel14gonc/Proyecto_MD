from collections import Counter
from itertools import groupby

data = None
with open('otro.txt', 'r') as file:
    contents = file.read()
    contents = contents.replace('\n', ',')
    data = contents.split(',')

# Count the occurrences of each item
counts = Counter(data)

# Group the items by count
groups = groupby(sorted(counts.items(), key=lambda x: x[1], reverse=True), key=lambda x: x[1])

# Print the groups
for count, items in groups:
    item_list = [item[0] for item in items]
    print(f"{count}: {item_list}")