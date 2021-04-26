class Formating:
    name = ''
    firstGap = 0
    writeSpace = 0
    secondGap = 0
    
    def __init__(self, name, first, write, second):
        self.name = name
        self.firstGap = first
        self.writeSpace = write
        self.secondGap = second


# Get output-list
output_list = 'a%B3.1.3 b%B3.1.3 out%B3.1.3' # input('Please put the output-list line with no semicolon: ')

# Parse output-list
objects = []

while (len(output_list) > 2):
    name = output_list[:output_list.index('%')]
    
    #   cut off up to next value
    output_list = output_list[output_list.index('%')+2:]
    
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
    objects.append(obj)

# print name to file
fileName = 'example.cmp' # input('What is the file name? ')
cmp = open(fileName, 'w')

cmp.write('|')
for obj in objects:
    cmp.write(obj.name.center(obj.firstGap + obj.writeSpace + obj.secondGap))
    cmp.write('|')
cmp.write('\n')

# get Vals
values = []
while True:
    for obj in objects:
        val = input('Value for ' + obj.name + ': ')
        values.append(val)
    ans = input('Would you like to input another test case (y/n)? ')
    if (ans == 'n'):
        break

# Print vals
while len(values) != 0:
    cmp.write('|')
    for obj in objects:
        if values[0] == '*' or values[0] == 'none':
            cmp.write('*' * (obj.firstGap + obj.writeSpace + obj.secondGap))
            values.pop(0)
        else:
            cmp.write(' ' * obj.firstGap)
            cmp.write(str(values.pop(0)).rjust(obj.writeSpace))
            cmp.write(' ' * obj.secondGap)
        cmp.write('|')
    cmp.write('\n')


cmp.close()