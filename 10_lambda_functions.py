def hello():
    print("hello!")

# Default parameter should alwasy go at the end
def add(x, y=8):
    return x+y
print(add(5,7)) 

print((lambda x,y: x + y)(5,7))