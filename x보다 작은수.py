import random #랜덤 도입


def random_list(number): #정수 N개의 수열로 구성된 리스트를 만드는 함수이다
  result=[]

  for i in range(number): #반복문을 통해 result 리스트에 N개의 숫자를 입력한다.
    result.append(random.randint(0,100)) #문제에 수열의 범위가 나타나있지 않아,
                                         #0부터 100까지 산정하였다.

  return result

n=int(input("n값을 입력하시오.: "))
x=int(input("x값을 입력하시오 : "))
result=random_list(n)
print(result)

list=[] #X보다 작은 수가 입력될 리스트이다.
a=0
for a in range(n): #반복문과 조건문을 통해 X보다 작은 정수를 리스트에 넣어준다.
  if result[a] < x:
    list.append(result[a])
print(list)
    
  
  

