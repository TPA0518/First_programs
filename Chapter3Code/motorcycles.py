motorcycles = []
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles)
motorcycles.append('Honda')
print(motorcycles)

motorcycles.insert(1, 'Toyota')
print(motorcycles)
motorcycles.insert(3, 'BMW')
print(motorcycles)

del motorcycles[2]
print(motorcycles)
del motorcycles[3]
print(motorcycles)

popMotorcycles = motorcycles.pop()
print(motorcycles)
print(popMotorcycles)

motorcycles.append('Honda')
popMotorcycles = motorcycles.pop()
print("The last motorcycle I owned was a " + popMotorcycles + ".")
firstOwnedMotorcycle = motorcycles.pop(0)
print("The first motorcycle I owned was a " + firstOwnedMotorcycle + ".")

expensiveMotorcycle = 'BMW'
motorcycles.remove(expensiveMotorcycle)
print(motorcycles)
print("A " + expensiveMotorcycle.title() + " is too expensive for me.")

