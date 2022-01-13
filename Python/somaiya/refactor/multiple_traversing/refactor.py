# In this case: we should be using dictionaries ratehr than a list of arrays as we can iterate over both key and value in one for loop. 
# OR we can also use zip function ...

names  = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
 
heros = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

dheros = {
    'Peter Parker': 'Spiderman', 
    'Clark Kent': 'Superman', 
    'Wade Wilson': 'Deadpool', 
    'Bruce Wayne': 'Batman', 
}

universes = ['Marvel', 'DC', 'Marvel', 'DC']

print("");
for name, hero in dheros.items():
    print(name, "is actually", hero);
print("");


for name, hero in zip(names, heros):
    print(f'{name} is actually {hero}');
print("");

for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is actually {hero} from {universe}');
print("");

pack_a = zip(names, heros, universes);
for x in pack_a: 
    print(x)

