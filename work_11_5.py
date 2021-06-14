print('Введите строку:')
s = input()
n = s.split()
v = []
cnt = 0
for i in range(len(n)):
        for k in range(len(n)):
                if n[i] == n[k]:
                        cnt += 1
        if cnt == 1:
                v.append(n[i])
        cnt = 0

print(*v)
