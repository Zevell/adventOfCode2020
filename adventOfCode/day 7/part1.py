from string import digits

f = open('input.txt', 'r')
data = f.readlines()
f.close()

bags = []

def stripDigits(list):
  remove_digits = str.maketrans('','', digits)
  sSplit = ','.join(list).translate(remove_digits).strip().split(', ') # use translate to remove all digits, strip, then split with a space because join adds a after the seperator.
  return sSplit

def getBags(data):
  for rule in data:
    if rule == None or rule == "" or rule == "\n":
      print("Rule empty")
      continue
    contains = rule.replace('.','').strip().split(',') # remove the trailing dotpoint and trim, then split by "," as it is used to separate bag info in "data".
    
    for e in contains:
      if "bags" in e or "bag" in e or "contain" in e:
        contains[contains.index(e)] = contains[contains.index(e)].replace('bags','').replace('bag','').replace('contain',':').replace('  ',' ').strip() # the element at the index of "e" will be replaced with the same value but with some words replaced.

    bag = []
    for b in contains:
      # print("index of b:", contains.index(b))
      if contains.index(b) == 0: # if the index of "b" in "contains" is 0 (first element) then alter it before adding it to "bag" list.
        bSplit = b.split(' : ')
        bag.append(bSplit[0])
        bag.append(bSplit[1])
      else:
        bag.append(b)
    
    bags.append(bag)
  
  directHolders = []
  for bGroup in bags:
    for bag in bGroup[1:]:
      if "shiny gold" in bag: # it can contain a shiny gold bag directly, so add it to the list that can hold the shiny gold bags directly.
        # print('found holder', bGroup[0])
        directHolders.append(bGroup[0])
  
  # print(directHolders)
  # print(contains)
  # print('\n\n\n')
  # print(bags)
  # print(bags[0])
  # print(bags[1])
  return bags, directHolders


bags, directHolders = getBags(data)
indirectHolders = []
for bagGroup in bags:
  bagGroup = stripDigits(bagGroup)
  
  for bag in bagGroup:
    for dh in directHolders:
      if dh in bag:
        # print(bagGroup)
        indirectHolders.append(bagGroup)
        
   
def findIndirectHandlers(bags):
  for bagGroup in bags:
    bagGroup = stripDigits(bagGroup)
    # print('bagGroup',bagGroup)
    for bag in bagGroup[1:]:
      for ih in indirectHolders:
        # print(ih[0])
        if ih[0] in bag: # current iterated number's element, and the first element of that ([0]) as that is the name of the bag.
          indirectHolders.append(bagGroup)

for x in range(0,4): # run it multiple times to make sure that all bags exist because running it only once does not give all bags as some bags aren't "defined" yet.
  findIndirectHandlers(bags)
# print(indirectHolders)
indirectHolderNames = dict.fromkeys([ih for ih in [item[0] for item in indirectHolders]]) # return a unique list of item names
directHolderNames = dict.fromkeys([dh for dh in [item[0] for item in directHolders]]) # return a unique list of item names

print(indirectHolderNames)
print(len(indirectHolderNames))