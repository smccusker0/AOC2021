import sys

if len(sys.argv) != 2 or sys.argv[1].lower() != 'test' and sys.argv[1].lower() != 'prod':
    print("Usage: 'python day1.py test' to run Test data\n'python day1.py prod' to run Production data\n")
    sys.exit

if sys.argv[1].lower() == 'test':
    dataFile = open('test.txt')
elif sys.argv[1].lower() == 'prod':
    dataFile = open('prod.txt')

depthList = []
for datum in dataFile.readlines():
    depthList.append(int(datum))

dataFile.close()

increaseTally = 0

#part 1
for x, y in zip(depthList, depthList[1:]):
    if y > x:
        increaseTally += 1

print("Part 1: ")
print(increaseTally)

increaseTally = 0
sumList = []
#part 2
for x, y, z in zip(depthList, depthList[1:], depthList[2:]):
    sumList.append(int(x) + int(y) + int(z))

for x, y in zip(sumList, sumList[1:]):
    if y > x:
        increaseTally += 1

print("Part 2:")
print(increaseTally)