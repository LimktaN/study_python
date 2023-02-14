a = "이시영"
b = "김정형"
c = "이상민"
d = "김종민"
e = "탁재훈"

f = ["이시영", "김정형", "이상민", "김종민", "탁재훈"]
print(a, b, c, d, e)
print(f[2])

g = ["int", 1, 2, ["haha", "hoho"]]
print(g[3][1])
print(g[1]+g[2])
print(g[0:2])

g[0] = "str"
print(g)

g[1:3] = [5, 6]
print(g)

g.append("추가")
print(g)

h = [7, 112, 2, 2323, 31]
print(h)

h.sort()
print(h)

h.reverse()
print(h)

h.insert(2, 12345)
print(h)

h.remove(112) # 인덱스가 아닌 값
print(h)

print(h.pop())
print(h.count(12345))

print(h.extend([1727, 12362]))
print(h)