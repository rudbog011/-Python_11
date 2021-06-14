print('Введите строку, содержащую натуральные числа, отделенные символом пробела:')
s = input()
n = s.split()
cnt = 0
print(n)
for i in range(len(n)):
        for k in range(i + 1, len(n)):
                if n[i] == n[k]:
                        cnt += 1
print(cnt)
