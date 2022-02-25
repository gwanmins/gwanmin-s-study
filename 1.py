raw=map(str, input("펠린드롬을 입력해주세요: ").split())
str_list=list(raw)
str_join="".join(str_list)
str_case=list(str_join.lower())
rev_str=str_case[::-1]

if str_case==rev_str:
    print ("응 맞아~")
else:
    print ("응 아니야~")