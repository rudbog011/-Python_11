print('Введите ip-адрес:')
ip = input()
s = ip.split('.')
flag = 'YES'
if len(s) != 4:
    flag = 'NO'
for sn in s:
    if int(sn) < 0 or int(sn) > 255:
        flag = 'NO'
print(flag)
