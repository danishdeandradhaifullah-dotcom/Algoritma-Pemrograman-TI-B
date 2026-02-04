def greeting(name):
  print("Hello, " + name) 

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))