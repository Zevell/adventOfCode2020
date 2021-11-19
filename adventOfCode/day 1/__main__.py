dataFile = open('./data.txt','r')
data = dataFile.readlines()

found = False
for num1 in data:
  if found == True:
    break
  num1 = int(num1)
  for num2 in data:
    num2 = int(num2)
    for num3 in data:
      num3 = int(num3)
      if num1 + num2 + num3 == 2020:
        print("Correct Numbers:\nNum1: {}\nNum2: {}\nNum3: {}\nTotal: {}\nMultiplied: {}".format(num1, num2, num3, num1+num2+num3,num1*num2*num3))
        found = True
        break
      pass
    pass
  pass


dataFile.close()