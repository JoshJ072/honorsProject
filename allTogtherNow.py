def inputFromUser():
    # Getting inputs
    values = []
    while True:
        for i in inputIdx:
            val = input('Value for ' + template[i].strip() + ': ')
            values.append(val)
        ans = input('Would you like to input another test case (y/n)? ')
        if (ans == 'n'):
            return values

def inputFromCSV():
    # Getting inputs
    values = []
    csv = open(fileName + '.csv')
    for line in csv:
        parts = line.split(',')
        for part in parts:
            values.append(part.strip())
    csv.close()
    return values

chipName = input("Please enter the chip name without extension: ")
if (input("Would you like the files to be a different name (y/n)? ").strip() == 'y'):
    fileName = input("Please enter the file name without extension: ")
else:
    fileName = chipName

# The two lists to return
template = []
inputs = []

# Opening the file
file = open(chipName + '.template')

# Extracting the lines
numInputs = 0
idx = 0
inputIdx = []
for line in file:
    if line.strip() == '':
        continue
    template.append(line)
    if '()' in line:
        numInputs += 1
        inputIdx.append(idx)
    idx += 1

if input('Would you like to input values manually (y/n)? ') == 'y':
    inputs = inputFromUser()
else:
    inputs = inputFromCSV()
    
file.close()


# Prining to .tst file
tst = open(fileName + '.tst.', 'w')

# Printing the header
tst.write('load ' + chipName + '.asm,\n')
tst.write('output-file ' + fileName + '.out,\n')
tst.write('compare-to ' + fileName + '.cmp,\n')
outputFormat = input('Please enter the output-list line: ')
if 'output-list' in outputFormat:
    tst.write(outputFormat + '\n\n')
else:
    tst.write('output-list ' + outputFormat + ';\n\n')

idx = 0
while len(inputs) != 0 or idx != 0:
    if '()' in template[idx]:
        if inputs[0].strip() != 'none':
            tst.write(template[idx].replace('()', inputs[0]))
        inputs.pop(0)
    else:
        tst.write(template[idx])
    idx += 1
    if idx == len(template):
        idx = 0
        tst.write('\n\n')

tst.close()