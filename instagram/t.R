from math import ceil, floor

perimeter = 20
length = int(ceil(perimeter / 4))
breadth = int(floor(perimeter / 4))
area = length * breadth
print("length = " + str(length))
print("breadth = " + str(breadth))
print("area = " + str(area))