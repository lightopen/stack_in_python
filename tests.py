from stack import Stack

print(help(Stack))

s = Stack()

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(2)

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(4)

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(22)

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(55)

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(66)
print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

s.push(0)

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

v = s.pop()

print("=========================")
print(s.top)
print(s.count())
print(s.full())
print(s.empty())
for i in s:
    print("%s in s" % i)

print(v)



