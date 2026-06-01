a = 20
b = 20
c = 20.5
d = "hello"
e = [1, 2, 3]
f = {"key": "value"}

print(f"int a: {id(a)} => {hex(id(a))}")
print(f"int b: {id(b)} => {hex(id(b))}")
print(f"float c: {id(c)} => {hex(id(c))}")
print(f"string d: {id(d)} => {hex(id(d))}")
print(f"list e: {id(e)} => {hex(id(e))}")
print(f"dict f: {id(f)} => {hex(id(f))}")