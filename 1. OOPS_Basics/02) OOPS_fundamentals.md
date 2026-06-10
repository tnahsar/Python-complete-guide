# Fundamental concepts of object-oriented programming (OOP):
- OOP fundamentals focus on encapsulation, inheritance, polymorphism, and abstraction, with classes and objects being central to its structure.

## Class
- A class is like a blueprint or template for creating objects. It defines a set of attributes (variables) and behavior (methods) that the objects created from that class will have.
- In Python, classes are defined using the class keyword.

Example:
```
class Dog:
    # Attributes (variables)
    species = "Canine"

    # Method (function defined within the class)
    def bark(self):
        return "Woof!"
```
- Class: Dog is the class that defines what characteristics and behaviors all "Dog" objects will have.
- Inside the class, species is an attribute, and bark() is a method.


## Object
- An object is an instance of a class. When you create an object, you're creating a real-world instance of that class with specific data.
- An object is created by calling the class as if it were a function.
- When a class is defined, no memory is allocated until an object of that class is created.

Example:
```
# Creating an object (instance) of the Dog class
my_dog = Dog()

# Accessing object attributes and methods
print(my_dog.species)  # Outputs: Canine
print(my_dog.bark())    # Outputs: Woof!
```
## Attributes
- Attributes are **variables** that hold data related to an object. 
- There are two types of attributes:
  - **Instance attrbiute:**
    - An **instance** attribute is a variable that belongs to a specific object (instance) of a class.
    - Each object has its own separate copy of these attributes.
    - They are usually defined inside the constructor `__init__()`.
    - Changes to one object’s instance attribute don’t affect other objects.

    Example:
    ```
    class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance attribute
        self.breed = breed    # Instance attribute

    # Create two Dog objects
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Charlie", "Poodle")

    # Each object has its own data
    print(dog1.name)  # Output: Buddy
    print(dog2.name)  # Output: Charlie

    # Changing dog1’s name won’t affect dog2
    dog1.name = "Max"
    print(dog1.name)  # Output: Max
    print(dog2.name)  # Output: Charlie
    ```
    Hee `name` and `breed` are instance attributes. Each dog has its own `name` and `breed`.
    
  - **Class attrbiute:**
    - A **class** attribute is shared by all objects (instances) of the class.
    - It is defined outside of the constructor (directly inside the class).
    - All instances share the same copy of the class attribute.
    - If you change the value of class attribute, it will affects all objects.

    Example:
    ```
    class Dog:
    species = "Canine"  # Class attribute (shared by all dogs)
    
    def __init__(self, name, breed):
        self.name = name   # Instance attribute
        self.breed = breed # Instance attribute

    # Create two objects
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Charlie", "Poodle")

    # Access class attribute
    print(dog1.species)  # Output: Canine
    print(dog2.species)  # Output: Canine

    # Change the class attribute at the class level
    Dog.species = "Dog Animal"

    print(dog1.species)  # Output: Dog Animal
    print(dog2.species)  # Output: Dog Animal
    ```
    Here `species` is a class attribute — shared among all dogs. Changing it on the class (`Dog.species`) updates it for all instances.

  Example Showing Both Together:
  ```
  class Car:
  wheels = 4  # Class attribute

  def __init__(self, brand, color):
    self.brand = brand   # Instance attribute
    self.color = color   # Instance attribute

  # Create two Car objects
  car1 = Car("Toyota", "Red")
  car2 = Car("Honda", "Blue")

  print(car1.wheels, car1.brand, car1.color)  # 4 Toyota Red
  print(car2.wheels, car2.brand, car2.color)  # 4 Honda Blue

  # Change instance attribute
  car1.color = "Black"
  print(car1.color)  # Black
  print(car2.color)  # Blue (unchanged)

  # Change class attribute
  Car.wheels = 6
  print(car1.wheels)  # 6
  print(car2.wheels)  # 6
  ```
  `brand` and `color` → instance attributes  & `wheels` → class attribute

## Function
- A function is a block of reusable code that is designed to perform a specific task.
- It can be defined inside or outside of a class
- It can take inputs (called parameters or arguments) and return an output.
- Functions are not tied to any particular object or class. It's a standalone entity.

Example:
```
 def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```
 In this example, `greet()` is a function. It's defined independently and isn't tied to any object.

 ## Method
- A method, on the other hand, is a function that is bound to an object or a class. This means it is associated with an object and can be called on that object.
- A method can only be defined inside a class. So, it works on data related to the object or class.
- A method is called on an object, usually using dot notation `(object.method())`, and it can also take the  object itself (via self) as the first argument in the case of instance methods.

Example:
```
 class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
```
Here, `bark()` is a method because it's defined inside a class (Dog), and you call it on an instance or object of the class i.e. 'my_dog'.

### Built-in method:
- Lists, tuples, strings, sets, dictionaries, and many other data types in Python are actually objects, and they come with their own built-in methods.

#### Example: list Methods
- A `list` is an object of class `list`, and it has several built-in methods, such as:

| Method      | Description                          | Example              |
|--------------|--------------------------------------|----------------------|
| append(x)    | Adds an item `x` to the end of the list | `my_list.append(10)` |
| remove(x)    | Removes the first occurrence of `x`     | `my_list.remove(5)`  |
| sort()       | Sorts the list in place                 | `my_list.sort()`     |
| reverse()    | Reverses the list                      | `my_list.reverse()`  |
| pop()        | Removes and returns the last element    | `my_list.pop()`      |
| count(x)     | Returns how many times `x` appears      | `my_list.count(3)`   |
| index(x)     | Returns the index of the first `x`      | `my_list.index(2)`   |

So when you write: `my_list.sort()` you’re calling the `sort()` built-in method that belongs to the list object.

#### Example: tuple Methods
- Tuples are immutable (cannot be changed), so they have fewer methods:

| Method   | Description              | Example                        |
|-----------|--------------------------|----------------------------------|
| count(x)  | Counts occurrences of `x` | `(1, 2, 2, 3).count(2) → 2`     |
| index(x)  | Returns index of `x`      | `(1, 2, 3).index(3) → 2`        |

#### Example: str (string) Methods
- Strings also have many useful methods:

| Method          | Description                 | Example                             |
|-----------------|-----------------------------|-------------------------------------|
| upper()         | Converts to uppercase        | `"hello".upper() → "HELLO"`         |
| lower()         | Converts to lowercase        | `"HELLO".lower() → "hello"`         |
| replace(a, b)   | Replaces `a` with `b`        | `"hi world".replace("hi", "hello")` |
| split()         | Splits into a list           | `"a,b,c".split(",") → ['a', 'b', 'c']` |
| strip()         | Removes whitespace           | `" hi ".strip() → "hi"`             |

## Constructor
- A constructor is a special method that gets called when you create a new object of a class. The main purpose of a constructor is to **initialize an object’s attributes** i.e. it allows you to set the initial state (values) of an object.
- In Python, the constructor is defined using the special method `__init__()`. This method is automatically called when you create a new object or instance of a class.  
**Note:** It’s not called explicitly — Python does that for you when you create an instance of the class.
- It always takes at least `self` as the first parameter: `self` refers to the instance of the class being created. Any other parameters are used to initialize attributes.

Example of a Constructor in Action:
```
class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name      # Initialize the name of the dog
        self.breed = breed    # Initialize the breed of the dog
    
    def bark(self):
        print(f"{self.name} says woof!")

# Create an instance of the Dog class (calls the constructor automatically)
my_dog = Dog("Buddy", "Golden Retriever")

# Access the attributes and methods of the object
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()        # Output: Buddy says woof!
```

#### **Why self is Important:**
- `self` is like a placeholder for the object you’re working with.  
**Note:** You don’t pass self when creating an object; Python handles that internally. You only provide values for the parameters like name and breed.

  When You Create an Object:
  ```
  my_dog = Dog("Buddy", "Golden Retriever")
  ```
  Python internally calls:
  ```
  Dog.__init__(my_dog, "Buddy", "Golden Retriever")
  ```