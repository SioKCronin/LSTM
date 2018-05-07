import numpy as np

n = 10
string_size = 50

fh = open("data_{}.csv".format(string_size), 'w')
fh.write("sequence,target\n")
for i in range(n):
    value = np.random.randint(2, size=string_size)
    for x in value:
        fh.write(str(x))
    if int(value[-1]) == 1:
        fh.write(",1.0")
    else:
        fh.write(",0")
    fh.write('\n')

fh = open("data_variable.csv", 'w')
fh.write("sequence,target\n")
for i in range(n):
    value = np.random.randint(2, size=np.random.randint(1, string_size))
    for x in value:
        fh.write(str(x))
    if int(value[-1]) == 1:
        fh.write(",1.0")
    else:
        fh.write(",0")
    fh.write('\n')
