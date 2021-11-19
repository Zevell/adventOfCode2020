import re

f = open('./input.txt', 'r')
data = f.read().split('\n\n')
# print(data)
f.close()

personArray = []
i = 0
for info in data:
  # print('Original:',info)
  splitInfo = info.split('\n')
  splitInfo = ' '.join(splitInfo).split(' ')
  splitInfo = ':'.join(splitInfo).split(':')
  splitInfo = list(filter(lambda x: (x != None),splitInfo))
  
  # print('Split:', splitInfo)
  personArray.append(splitInfo)
  
  i += 1
  pass

def byr(intValue):
  if intValue >= 1920 and intValue <= 2002:
    return True
  else:
    return False

def iyr(intValue):
  if intValue >= 2010 and intValue <= 2020:
    return True
  else: 
    return False
  
def eyr(intValue):
  if intValue >= 2020 and intValue <= 2030:
    return True
  else:
    return False
  
def hgt(value):
  cm = None
  inches = None
  if 'cm' in value:
    cm = value.split('cm')
  elif 'in' in value:
    inches = value.split('in')
  if inches:
    if int(inches[0]) >= 59 and int(inches[0]) <= 76:
      return True
  elif cm: 
    if int(cm[0]) >= 150 and int(cm[0]) <= 193:
      return True
  return False

def hcl(value):
  if not '#' in value:
    return False
  if re.search("[\da-f]{6}",value.lower()):
    return True
  else:
    return False

def ecl(value):
  valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  for color in valid:
    if value == color:
      return True
  return False

def valid(person):
  correct = 0
  print(person)
  for field in person:
    # print(field)
    value = None
    intValue = None
    try:
      value = person[person.index(field)+1]
      intValue = int(person[person.index(field)+1])
    except Exception as e:
      # print(e)
      pass
    
      
    if field == 'byr':
      if byr(intValue) == True:
        print('byr correct')
        correct += 1
    elif field == 'iyr':
      if iyr(intValue) == True:
        print('iyr correct')
        correct += 1
    elif field == 'eyr':
      if eyr(intValue) == True:
        print('eyr correct')
        correct += 1
    elif field == 'hgt':
      if hgt(value) == True: 
        print('hgt correct')
        correct += 1
    elif field == 'hcl':
      if hcl(value) == True:
        print('hcl correct')
        correct += 1
    elif field == 'ecl':
      if ecl(value) == True: 
        print('ecl correct')
        correct += 1
    elif field == 'pid':
      # print('pid length:',len(value))
      # print('pid:', str(value).strip())
      if len(str(value).strip()) == 9:
        print('pid correct')
        correct += 1
      
  if correct == 7:
    return True
  else:
    return False

requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
correct = 0
for person in personArray:
  has = 0
  for field in requiredFields:
    if field in person:
      has += 1
    elif field == "cid":
      has += 1
    pass
  if has == 8:
    if valid(person): # send the entire person list to verify whether all fields are correct.
      correct += 1
  pass

# print(infoDict)
print('\n\nPerson1:', personArray[0])
print('correct:', correct)