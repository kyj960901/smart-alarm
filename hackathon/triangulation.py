import math

#cos to sin
def cos_to_sin(a):
    return (1-a**2)**0.5

#코사인제2법칙을 이용하여 코사인값
def cos2_law(a, b, c):
    return (b**2+c**2-a**2)/(2*b*c)

#두점의 x축에대한 기울기를 사인으로 반환
def gradient_sin(p1, p2):
    return (p2[1]-p1[1])/distance_2points(p1, p2)

#두점의 x축에대한 기울기를 코사인으로 반환
def gradient_cos(p1, p2):
    return (p2[0]-p1[0])/distance_2points(p1, p2)

#두점의 거리
def distance_2points(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5


#평균점구하기
def avg_point(sin, cos, d):
    return [d*cos, d*sin]

def avg_arr(arr):
    x=0
    y=0
    for a in arr:
        x+=a[0]
        y+=a[1]
    return [x, y]


def triangulation(points, distances):
    arr = []
    l = len(points)
    for i in range(l):
        angle_cos = cos2_law(distances[i], distances[(i+1)%l], distance_2points(points[i], points[(i+1)%l]))
        d = angle_cos * distances[i]
        arr.append(avg_point(gradient_sin(points[i], points[(i+1)%l]), gradient_cos(points[i], points[(i+1)%l]), d))
    return avg_arr(arr)


points = [(4, 0), (2, 7), (1, 0), (8, 6)]
distances = (4, 3, 3, 1)

print(triangulation(points, distances))