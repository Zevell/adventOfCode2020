inputFile = open('./input.txt','r')
# readlines produced an array, where elements would have "\n" in them
# we use read, and split lines instead
inputData = inputFile.read().splitlines()
print("Input Data Lines:", len(inputData))
inputFile.close()

def SplitData(inputData):
  inputData = inputData.replace(':','').replace('-',' ')
  splitData = inputData.split(' ')
  return splitData

accepted = []
for line in inputData:
  # print("split data:", SplitData(line))
  first, second, required, password = SplitData(line)
  first = int(first)-1 # minus one so it is more inline with arrays
  second = int(second)-1 # minus one so it is more inline with arrays
  # Encountered an error I thought was related to the string having less length than the character position it is looking at, was not related.
  # if len(password) < good or len(password) < bad:
  #   continue
  if password[first] == required and password[second] != required:
    accepted.append(password)
  elif password[second] == required and password[first] != required:
    accepted.append(password)
pass

# print(accepted)
print("Accepted Count", len(accepted))