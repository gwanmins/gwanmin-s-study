def find_Pal(str1):
    str1 = list(str1)
    str2 = str1[::-1]
    if str2 == str1:
        return str1
    else:
        pass


raw = str(input("문자열을 입력해주세요: "))
str_list = list(raw)
pal_list_temp = []
maxnum_temp = 0
maxnum = 0

for i in range(0, len(str_list)):
    for k in range(1, len(str_list) + 1):
        if find_Pal(str_list[i:i + k]) is None:
            continue
        elif find_Pal(str_list[i:i + k]) is not None:
            maxnum_temp += 1
            pal_list_temp.append(str_list[i:i + k])
            continue
    if maxnum_temp > maxnum:
        maxnum = maxnum_temp
        maxnum_temp = 0
        continue
    else:
        maxnum_temp = 0
        continue

print(max(pal_list_temp, key=len))
