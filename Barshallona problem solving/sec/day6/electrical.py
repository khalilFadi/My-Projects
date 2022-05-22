import math 
n = int(input())
cities = []
for i in range(n):
    city = list(map(int, input().split()))
    cities.append(city)
num_towers = int(input())

towers = []
for i in range(num_towers):
    tower = list(map(int, input().split()))
    towers.append(tower)


#input ends 
max_distance = 0
for C in cities:
    least_tower = 10e8
    for T in towers:
        if math.sqrt( (C[0] - T[0])**2 + (C[1] - T[1])**2 ) < least_tower:
            least_tower = math.sqrt( (C[0] - T[0])**2 + (C[1] - T[1])**2 )
    if least_tower > max_distance:
        max_distance = least_tower
print(max_distance)