from sys import stdin

colorValue = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9
}
colorMulity = {
    "black" : 1,
    "brown" : 10,
    "red" : 100,
    "orange" : 1000,
    "yellow" : 10000,
    "green" : 100000,
    "blue" : 1000000,
    "violet" : 10000000,
    "grey" : 100000000,
    "white" : 1000000000
}

color = ""
result = 0
colorList = [stdin.readline().strip() for _ in range(3)]
# print(colorList)

for colorIdx in range(3):
    if colorIdx == 0:
        color += str(colorValue[colorList[colorIdx]])
    elif colorIdx == 1:
        color += str(colorValue[colorList[colorIdx]])
    else:
        result = int(color) * colorMulity[colorList[colorIdx]]

print(result)