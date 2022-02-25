def Pythagorean(a,b,c): #조건문에 따라 삼각형의 종류를 판별하는 Pythagorean 함수 정의
    if a+b <= c :       # 이 경우는 삼각형이 아니다
        print("NO")
    elif a**2+b**2 == c**2 :  #이 경우에 직각 삼각형이다
        print("직각삼각형")
    elif a**2+b**2 < c**2 :   #이 경우는 둔각 삼각형이다
        print("둔각삼각형")
    else :                    #그 외에는 예각 삼각형으로 처리했다.
        print("예각삼각형")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

Pythagorean(a,b,c)
