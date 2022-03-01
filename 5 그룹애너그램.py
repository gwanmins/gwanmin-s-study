raw_list = list(map(str, input("단어를 입력해주세요: ").split()))
set_list = []
ana_counter = 1
dicts = {}

for i in range(0, len(raw_list)):
    set_list.append(set(raw_list[i]))

keys = range(len(set_list))

for j in range(0, len(set_list)):
    if set_list.count(set_list[j]) > 1:
        for k in keys:
            dicts[j] = set_list[j]
    else:
        pass

for l in range(0, len(dicts)):
    if dicts[l] == dicts[l + 1]:

