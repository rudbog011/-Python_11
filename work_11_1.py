print('Введите количество строк n:')
n = int(input())
print('Введите', n, 'строк:')
s = []
for i in range(n):
    s.append(input())
print('Введите строку поиска:')
poisk = input()
for i in range(len(s)):
    if poisk.lower() in s[i].lower():
        print(s[i])
