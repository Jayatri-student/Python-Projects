# list is mutable, ordered, allows duplicate elements
fruits=["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
fruits[2] = "kiwi"
print(fruits)

# tuple is immutable, ordered, allows duplicate elements
contact=("XYZ",20,"female")
name,age,gender=contact
print(name)
print(age)

# set is mutable, unordered, does not allow duplicate elements
fruits={"apple", "banana", "cherry"}
fruits.add("dragonfruit")
fruits.discard("banana")
print(fruits)

# dictionary is mutable, unordered, does not allow duplicate keys
student={"name":"XYZ",
         "age":20,
         "dept":"CSE"}
print(student)
print(student["name"])
print(student.get("age"))
student["city"]="Bangalore"
student.pop("age")
print(student)

for key,value in student.items():
    print(key,":",value)
print(student.keys())
print(student.values())

#indexing
marks=[10,20,30,40,50]
print(marks[0]) # first element
print(marks[-1]) # last element
print(marks[2]) # third element

# slicing
print(marks[1:4]) # elements from index 1 to 3
print(marks[:3]) # first three elements
print(marks[2:]) # elements from index 2 to end
print(marks[::2]) # every second element
print(marks[::-1]) # reverse the list

# functions without parameters and without return type
def greet():
    print("WELCOME")
greet()

# functions with parameters and without return type
def greeting(message):
    print(message)
greeting("Hello")

#functions with parameters and with return type
def calc(a, b):
    return a + b, a * b
total, product = calc(10, 20)
print("Total:", total)
print("Product:", product)

#default parameters
def greet(name="Guest"):
    print("Hello", name)
greet("XYZ")
greet() # uses default parameter

#keyword arguments
def introduce(name, age,city):
    print(name,age,city)
introduce(name="XYZ", age=20, city="Bangalore") #with order
introduce(city="Bangalore", name="XYZ", age=20) #without order



