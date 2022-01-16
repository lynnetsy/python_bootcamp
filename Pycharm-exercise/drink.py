import numpy as np

machine_resources = \
    {
        'Water': 300,
        'Milk': 200,
        'Coffee': 100,
        'Money Available': 10,

    }
drinks = {
    'Espresso':
        {'Water': 50,
         'Milk': 0,
         'Coffee': 18,
         'Value': 7,
         },
    'Latte':
        {'water': 200,
         'milk': 150,
         'Coffee': 24,
         'Value': 7,
         },
    'Cappuccino':
        {'water': 250,
         'milk': 100,
         'Coffee': 24,
         'Value': 7,
         }
}

drinks_index = ['Water', 'Milk', 'Coffee', 'Value']
machine_index = ['Water', 'Milk', 'Coffee', 'Money Available']

# espresso = drinks['Espresso'][index[0]]

# print(espresso)
result = []
a = np.array(list(machine_resources.values()))
b = np.array(list(drinks['Espresso'].values()))

result = np.subtract(a, b)
print(a)
print(b)
print(result)

def update_resources(result):
    new_stats = {}
    i = 0
    for element in machine_index:
        new_stats[element] = result[i]
        i += 1
        new_stats.append(new_stats[element] = result[i])

update_resources(result)


