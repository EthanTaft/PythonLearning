"""Remove multiple keys and their values from a python dictionary at once
"""
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'
}

# Remove one item at a time
del zoo_animals['Unicorn']

# Or remove multiple items at once with the pop() method for dictionaries
ls = ["Sloth", "Bengal Tiger"]
for k in ls:
  zoo_animals.pop(k)

# Reassign a key's value in a dictionary
zoo_animals["Rockhopper Penguin"] = "Cold"
print zoo_animals
