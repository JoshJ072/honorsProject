class Formating:
    name = ''
    firstGap = 0
    writeSpace = 0
    secondGap = 0
    leftAlign = False
    
    def __init__(self, name, first, write, second):
        self.name = name
        self.firstGap = first
        self.writeSpace = write
        self.secondGap = second


def getUserInput():
    values = []
    while True:
        for obj in objects:
            val = input('Value for ' + obj.name + ': ')
            values.append(val)
        ans = input('Would you like to input another test case (y/n)? ')
        if (ans == 'n'):
            return values

def importFromCSV():
    values = []
    csv = open(fileName + '.csv')
    for line in csv:
        parts = line.split(',')
        for part in parts:
            values.append(part.strip())
    csv.close()
    return values


# Get output-list
output_list = input('Please put the output-list line with no semicolon: ')

# Parse output-list
objects = []

while (len(output_list) > 2):
    name = output_list[:output_list.index('%')]
    
    #   cut off up to next value
    output_list = output_list[output_list.index('%')+1:]
    
    val = output_list[0]
    output_list = output_list[1:]
    
    firstGap = int(output_list[:output_list.index('.')])
    output_list = output_list[output_list.index('.')+1:]
    
    
    writeSpace = int(output_list[:output_list.index('.')])
    output_list = output_list[output_list.index('.')+1:]
    
    
    try:
        secondGap = int(output_list[:output_list.index(' ')])
        output_list = output_list[output_list.index(' ')+1:]
    except:
        secondGap = int(output_list)
    
    obj = Formating(name, firstGap, writeSpace, secondGap)
    if val == 'S':
        obj.leftAlign = True
    objects.append(obj)

# print name to file
fileName = input('What is the file name (no extension)? ')
cmp = open(fileName + '.cmp', 'w')

cmp.write('|')
for obj in objects:
    if (len(obj.name) > (obj.firstGap + obj.writeSpace + obj.secondGap)):
        cmp.write(obj.name[:obj.firstGap + obj.writeSpace + obj.secondGap].center(obj.firstGap + obj.writeSpace + obj.secondGap))
    else:
        cmp.write(obj.name.center(obj.firstGap + obj.writeSpace + obj.secondGap))
    cmp.write('|')
cmp.write('\n')

# get Vals
if (input('Would you like to input values from a csv (y/n)? ') == 'y'):
    values = importFromCSV()
else:
    values = getUserInput()


# Print vals
while len(values) != 0:
    cmp.write('|')
    for obj in objects:
        if values[0] == '*' or values[0] == 'none':
            cmp.write('*' * (obj.firstGap + obj.writeSpace + obj.secondGap))
            values.pop(0)
        else:
            cmp.write(' ' * obj.firstGap)
            if (obj.leftAlign):
                cmp.write(str(values.pop(0)).ljust(obj.writeSpace))
            else:
                cmp.write(str(values.pop(0)).rjust(obj.writeSpace))
            cmp.write(' ' * obj.secondGap)
        cmp.write('|')
    cmp.write('\n')


cmp.close()