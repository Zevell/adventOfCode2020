debug = False

with open('input.txt') as data:
  data = data.read().splitlines()
  
print('All Data:',data,'\n\n\n')

def createBagDict():
  bagDict = {}
  for line in data: # Loop through each line, creating a parent:children entry in 'bagDict'
    if not line: # If empty line; skip
      continue
    
    # Split twice because we need each child bag to also be seperated into elements.
    split = line.replace(' bags','').replace('.','').replace(' bag','').split(' contain')
    split = ', '.join(split).split(', ')
    
    for i,e in enumerate(split): # If child is not 'no other'; remove all leading and trailing whitespace from all children bags.
      if 'no other' in e:
        split.pop(i)
      else:
        split[i] = e.strip()
    
    parent = split[0]
    children = split[1:]
    
    if debug:
      print('Parent:',parent,'\nChildren:',children)
    
    bagDict[parent] = children
  return bagDict

bagDict = createBagDict()
if debug:
  print(bagDict)

# Recursive function, loop through all children of provided bag name if bag exists in dictionary. Add to the childrenCount the amount of children the bag contains.
i = 0
def countCarriedBags(bagName, multiplier=1):
  global childrenCount
  global bagDict
  global i
  bags = bagDict[bagName]
  i += 1
  
  if bags and debug: print('bags:',bags)
  if debug: print('multiplier:', multiplier), print('current iteration:',i)
  for x in range(0,multiplier):
    for bag in bags:
      if debug: print(bag[2:],'|', bag[:2]) # bag name | bag count
      childrenCount += int(bag[:2])
      if bag[2:] in bagDict.keys(): # If a key exists, it has children. Iterate through it.
        countCarriedBags(bag[2:],int(bag[:2]))

childrenCount = 0
countCarriedBags('shiny gold')
print('Children count:', childrenCount)




















# def countCarriedBags(bag):
#   global matchedChildren
#   global childrenCount
#   childrenofChild = 0
#   if not bag or type(bag) != str: # if the parameter provided for 'bag' is not a string; raise a type error.
#     raise TypeError('Requires a bag name as a string')
  
#   for child in bagDict[bag]:
#     if not child:
#         continue
      
#     print('bag:', bagDict[bag])
#     # print('child:', child)
#     for x in range(int(child[:2])):
#       if child[2:] in bagDict: # one of the children from "bag" exists in the bag dict, fetch the children (if they exist) of this child.
#         for childofChild in bagDict[child[2:]]: # for every child in the current iterated child
#           print('childBag:', bagDict[child[2:]])
#           # print('childofChild:', childofChild)
#           if childrenofChild == 0: # You can't multiply by zero, so first add.
#             childrenofChild = int(child[:2])
#           else:
#             childrenofChild *= int(child[:2]) # multiply the current value by the value of how many parents the child came from; as one bag can hold many children, and those many can hold many, etc.
#           print(childrenofChild)
#         print(childrenCount)
#         if childrenCount == 0:
#           childrenCount += childrenofChild
#         else:
#           childrenCount *= childrenofChild
#         countCarriedBags(child[2:])
      
        
#       # if child[2:] in matchedChildren:
#       #   matchedChildren[child[2:]].append(child)
#       # else:
#       #   matchedChildren[child[2:]] = [child]