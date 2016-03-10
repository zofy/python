from genericpath import exists
from sys import argv

script, from_file, to_file = argv

print('Copying from file %s to %s.' % (from_file, to_file))

r = open(from_file)
#w = open(to_file, 'w+')
data = r.read()
print("Size of data is %.2f bytes." % len(data))
print("Do you want to carry on? [Y,N]")
answer = raw_input()

if answer == 'Y':
    print("What file do you wish to write into?")
    #file = raw_input()
    w = open(raw_input(), 'w')
    w.write(data)
print("DONE!")
#for line in r:
#    w.write(line)

r.close()
try:
    w
except: NameError
else:
    w.close()