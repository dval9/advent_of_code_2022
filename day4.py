

file = open(r"./input4")
contains = 0

for line in file:    
    assigns = line.rstrip()

    assigns = assigns.split(',')
    a = assigns[0].split('-')
    b = assigns[1].split('-')

    if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]):
        contains += 1        
    elif int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1]):
        contains += 1
        
print(contains)
file.close()

file = open(r"./input4")
overlaps = 0

for line in file:    
    assigns = line.rstrip()

    assigns = assigns.split(',')
    a = assigns[0].split('-')
    b = assigns[1].split('-')

    if int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1]):
        overlaps += 1        
    elif int(a[1]) >= int(b[0]) and int(a[1]) <= int(b[1]):
        overlaps += 1
    elif int(b[0]) >= int(a[0]) and int(b[0]) <= int(a[1]):
        overlaps += 1
    elif int(b[1]) >= int(a[0]) and int(b[1]) <= int(a[1]):
        overlaps += 1
        
print(overlaps)
file.close()