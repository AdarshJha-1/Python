# import math
from math import sqrt

print("Hello, World!")

a = 10
b = 10
c = a + b
print(c)


slang = "UwW"
print(slang)

print(type(slang))
print(type(a))

print(id(a))

A = [1, 2, 3]
B = A;
B.append(69);
print(B)
print(A)

nums = [1,2,3]

print(nums)
nums.append(4)
print(nums)
nums.pop()

print(nums)
print(nums[0])
print(nums[-1])


point = (10, 2, -1);
print(point)
print(point[2])
print(type(point))
print(id(point))

s = {1, 2, 3}
print(s)
s.add(3);
print(s)


m = {
    "name": "Adarsh Jha",
    "age": 21
}

print(m)
print(type(m))
print(id(m))
print(m["name"])


square = lambda x: x*x

print(square(5))

nums = []
print(nums)

for i in range(10):
    nums.append(i*i)
print(nums)

nums = []
print(nums)
nums = [i*i for i in range(10)]

print(nums)

# with open("./data.txt") as f:
#     print(f.read())

class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(self.name)

u = User("Zoro")
u.hello()

# print(math.sqrt(16))
print(sqrt(16))