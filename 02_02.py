d = "hello world"
print(type(d))

dd = """hello
world

haha
"""
print(dd)

e = "hello \"World\""
print(e)

f = "hello "
g = "world"
h = 10
print(f+g)
print(f*h) # h 만큼 반복하여 출력


i = "Life is too short, You need Python"
print(i[0])
print(i[8])
print(i[0:8]) # 이상:미만:간격

j = "I eat %d apples." % 9
k = "I eat " + str(3) + " apples."
print(j)
print(k)

number = 10
day = "three"

l = "I ate %d apples. so I was sick for %s days." % (number, day)
print(l)

name2 = "진완"
m = "haha. {name} {level} hi".format(level="주임", name="진완")
n = f"haha. {name2} hi."
print(m)
print(n)