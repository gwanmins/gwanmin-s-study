def add_slot(a, b, c):
    num_sum=a+b+c
    if num_sum==0:
        return 0
    else:
        pass

nums= list(map(int, input("숫자를 입력해주세요: ").split(",")))
result_temp=[]

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        for k in range (i+2,len(nums)):
            if add_slot(nums[i],nums[j],nums[k])==0:
                result_temp.append([nums[i],nums[j],nums[k]])
            else:
                pass

print(result_temp)
