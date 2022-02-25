# 네개의 좌표 중 두 좌표를 선택해서 반복:
# 두 좌표로부터 식 구함
# 식과 원래 좌표가 만나는 좌표 구함
# 해당 좌표가 두 좌표 사이에 있는지 구함
# 맞으면 해당 좌표, 아니면 두 좌표 중 가까운 좌표 선택

import math

def main():
    ax,ay=map(int,input("a 좌표 입력: ").split())
    c1x,c1y=map(int,input("c1 좌표 입력: ").split())
    c2x,c2y=map(int,input("c2 좌표 입력: ").split())
    c3x,c3y=map(int,input("c3 좌표 입력: ").split())
    c4x,c4y=map(int,input("c4 좌표 입력: ").split())

    distances = [
        get_distance(ax,ay,c1x,c1y,c2x,c2y),
        get_distance(ax,ay,c1x,c1y,c3x,c3y),
        get_distance(ax,ay,c1x,c1y,c4x,c4y),
        get_distance(ax,ay,c2x,c2y,c3x,c3y),
        get_distance(ax,ay,c2x,c2y,c4x,c4y),
        get_distance(ax,ay,c3x,c3y,c4x,c4y),
    ]
    print("min distance:", min(distances))

def get_line(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1) # 기울기
    inter = y1 - slope*x1 # 절편
    return slope, inter

# 점 (x,y)와, (x1,y1), (x2,y2)를 지나는 직선사이의 거리
# 최단거리 교점이 (x1,y1), (x2,y2) 사이에 있다면 해당 교점과의 거리를,
# 아니면 (x1,y1)와 (x2,y2) 중 (x,y)와의 거리 중 짧은 것을 반환함
def get_distance(x,y,x1,y1,x2,y2):
    px, py = get_crossing_point(x, y, x1, y1, x2, y2)
    if is_point_between(px,py,x1,y1,x2,y2):
        return round(math.sqrt((px-x)**2+(py-y)**2),2)
    else:
        return round(min(math.sqrt((x1-x)**2+(y1-y)**2),
                   math.sqrt((x2-x)**2+(y2-y)**2)),2)

# 점 (x,y)와, (x1,y1),(x2,y2)사이를 지나는 직선의 최단거리 교점의 좌표
def get_crossing_point(x,y,x1,y1,x2,y2):
    if (x1==x2):
        return x1, y
    elif (y1==y2):
        return x, y1
    slope1, inter1 = get_line(x1,y1,x2,y2)
    m1 = slope1
    b1 = inter1
    m2 = -(1/slope1)
    b2 = (1/slope1)*x+y
    px = (b2-b1)/(m1-m2)
    py = m1*(b2-b1)/(m1-m2)+b1
    return px,py

def is_point_between(x,y,x1,y1,x2,y2):
    return x1 <= x <= x2 and y1 <= y <= y2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
