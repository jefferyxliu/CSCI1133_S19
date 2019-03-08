# CSCI 1133, Lab Section 013, lab07 Jeffery Liu, Earthquakes

f = open('2.5_day.csv','r')

line1 = f.readline().split(',')

for i in range(len(line1)):
    print('{0:2}\t{1}'.format(i + 1, line1[i]))


earthquakes = []
for line in f:
    l = line.split(',')
    earthquakes.append([l[4],l[13].lstrip('\"') + ',' + l[14].rstrip('\"')])


for x in sorted(earthquakes, reverse = True):
    print('magnitude: {0:4}\t\tlocation: {1}'.format(x[0], x[1]))

f.close()
