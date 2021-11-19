from termcolor import colored

inputFile = open("./input.txt")
inputData = inputFile.read().split('\n')
print(inputData)
inputFile.close()

def findChars(right=3, down=1):
  char = "#"
  charCount = 0
  increment = right
  i = 0
  
  for x in range(down,len(inputData),down):
    line = inputData[x]
    
    if not line or line == "\n" or line == None:
      continue
    
    line = line.strip()
    
    while right > len(line)-1:
      right -= len(line)

    if line[right] == char:
      charCount += 1

    # print('Right:', right)
    line = line[:right] + colored(line[right],'yellow' ,attrs=['bold']) + line[right+1:]
    # print(line)
    right += increment
    
    i += 1
    pass
  print('Chars:', charCount)
  return charCount

print(findChars(1) * findChars(3) * findChars(5) * findChars(7) * findChars(1,2))