debug = True

with open('input.txt') as data:
  data = data.readlines()
  
print('All Data:',data,'\n\n\n')

linesRead = []
acc = 0
i = 0
while i < len(data):
  line = data[i]
  if not line: continue # if the line is empty, skip.
  if i in linesRead: 
    print('Loop detected. Results:')
    print('acc:',acc,'| line #:',i,'| line data:',line,'| prev line:',linesRead[-1])
    break
  linesRead.append(i)
  if debug: print('current:',line)
  
  split = line.split(' ')
  type = split[0].strip()
  action = split[1][:1].strip()
  value = split[1][1:].strip()
  
  if type == 'acc': # change the value of acc by the specified action and value
    if action == '+': acc += int(value)
    elif action == '-': acc -= int(value)
  elif type == 'jmp': # change the current line by the specified action and value
    if action == '+': i += int(value)
    elif action == '-': i -= int(value)
    continue
  
  i += 1
  if debug: print('type:',type,'| action:',action,'| value:',value), print('line:',i), print('acc:',acc)
  