import re
import operator

# =============== Task 1 ============================

keys = ['a', 'b', 'c', 'd']
values = ['1', '2', '3', '4', '5', '6', '7']
values2 = ['11', '22', '33']

def createDict(keyList, valuelist):
    d = {}
    for i in range(len(keyList)): d[keyList[i]] = 'None'
    if len(valuelist) <= len(keyList):
        for i in range(len(valuelist)): d[keyList[i]] = valuelist[i]
    else:
        for i in range(len(keyList)): d[keyList[i]] = valuelist[i]
    print d

print "\n===    Task 1  ===\n"
createDict(keys, values)
createDict(keys, values2)

# =============== Task 2 ============================

str1 = 'Was it a car or a cat I saw'
str2 = 'Once upon a time in London...'

def palindr(string):
    s = string.lower().strip()
    pattern = re.compile(r'\s+')
    s = re.sub(pattern, '', s)
    if s == s[::-1]:
        print "String '%s' is palindrome" % string
    else:
        print "String '%s' is not palindrome" % string

print "\n===    Task 2  ===\n"
palindr(str1)
palindr(str2)

# =============== Task 3 ============================

a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print "\n===    Task 3  ===\n"
print list((set(a) & set(b)))

# =============== Task 4 ============================

f = open('access_log','r')

ip = []
hit = {}

for line in f:
    ip.append(re.match("(.*)(\s-\s-)",line).group(1))

for i in (list(set(ip))):
    hit[i] = int(ip.count(i))

hit = sorted(hit.items(),key = operator.itemgetter(1),reverse=True)

print "\n===    Task 4  ===\n"
print "Top 10 source ip by requests number:\n"
for i in range(0,10): print "{0} - {1}".format(*hit[i])

