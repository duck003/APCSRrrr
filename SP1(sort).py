class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

name = ['Michael Rivera', 'Joshua Morgan', 'Jeff Thompson', 'Tony John', 'Nathan Price', 'Hugh Wilson', 'Nicole Linden', 'Susanne Blanton', 'Alta Madison', 'Richard Alexander']

age = [12, 77, 50, 87, 11, 85, 58, 2, 76, 46]

person = [Person(name[i], age[i]) for i in range(len(name))]

def name(a:Person):
    z = a.name.split()
    return z[1]

pprson = sorted(person, key=name)

print([p.name for p in pprson])
