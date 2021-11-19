inputFile = open('./input.txt','r')
# readlines produced an array, where elements would have "\n" in them
# we use read, and split lines instead
inputData = inputFile.read().splitlines()
print("Input Data:", inputData)
inputFile.close()

def SplitData(inputData):
  inputData = inputData.replace(':','').replace('-',' ')
  splitData = inputData.split(' ')
  return splitData

accepted = []
for line in inputData:
  data_min, data_max, data_required, data_password = SplitData(line)
  data_min = int(data_min)
  data_max = int(data_max)
  
  required_count = data_password.count(data_required)
  if required_count >= data_min and required_count <= data_max:
    accepted.append(data_password)
  pass

print(accepted)
print('Accepted Count:', len(accepted))
