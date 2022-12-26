## Practice Exercises
Practice exercises on classes and OOP in general in python. 

1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. [[solution](./0-class.py)]
2. Create a Vehicle class without any variables and methods. [[solution](./1-vehicle.py)]
3. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

    Given Vehicle class is defined as

```python
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
```
4. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.