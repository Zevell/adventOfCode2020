debug = True

with open('testing.txt') as data:
  data = data.readlines()
  
print('All Data:',data,'\n\n\n')

def splitInstruction(instructionLine):
  if type(instructionLine) != str:
    raise TypeError('Expected a line as a string.')
  
  class splitInstruction:
    split = instructionLine.split(' ')
    type = split[0].strip()
    action = split[1][:1].strip()
    value = split[1][1:].strip()
  return splitInstruction

linesRead = {}
acc = 0
i = 0
while i < len(data):
  line = data[i]
  if not line: continue # if the line is empty, skip.
  if i in linesRead and linesRead[i][0] >= 2: 
    print('Loop detected. Results:')
    print('acc:',acc,'| line #:',i+1,'| line data:',line,'| prev line:',linesRead[-1])
    continue
  if i not in linesRead: linesRead[i] = 1
  else: linesRead[i] += 1
  if debug: print('current:',line), print('encounters:',linesRead[i])
  
  split = splitInstruction(line)
  
  if type == 'acc': # if the instruction type is to alter the accumulator
    if split.action == '+': acc += int(split.value)
    elif split.action == '-': acc -= int(split.value)
  elif type == 'jmp': # if the instruction type is to jump to a different line
    # alter the current line by the instruction's value
    if split.action == '+':
      i += int(split.value)
    elif split.action == '-':
      i -= int(split.value)
    continue
  
  i += 1
  if debug: print('type:',split.type,'| action:',split.action,'| value:',split.value), print('line:',i+1), print('acc:',acc)
  