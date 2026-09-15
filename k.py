p = []
m = []
q = []

for i in range(2, 5):
    if i == 2:
        for j in range (1, 6):
           p.append(f"2 x {j} = {2 * j}")
    elif i == 3:
        for j in range(1, 6):
            m.append(f"3 x {j} = {3 * j}")
    else:
        for j in range (1, 6): 
            q.append(f"4 x {j} = {4 * j}")
        
print(p)
print(m)
print(q)

# for j in range(1, 3):
#     str_li.append(f"2 x {j} = {2 * j}")
#     for j in range(1, 5):
#         n.append(f"3 x {j} = {3 * j}")
        
# print(str_li)
# print(n)
