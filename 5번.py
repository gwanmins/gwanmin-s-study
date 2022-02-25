import random


def random_list(number):  #N개의 정수를 포함하는 리스트 함수 정의
  result=[]

  for i in range(number):
    result.append(random.randint(0,100))

  return result

n, x=map(int, input("N과 X를 입력하시오 :").split()) #map함수와 split을 이용해 n과 x값 받기
result=random_list(n) #random_list 함수를 통해 정수 n개의 수열 확보
print(result)

if x==1 :  #조건문을 통해 x가 1이면 오름차순 0이면 내림차순으로 정렬한다.
    result.sort()
    print(result)
elif x==0 :
    result.sort(reverse=True)
    print(result)
    
  

