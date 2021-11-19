f = open('input.txt', 'r')
data = f.readlines()
f.close()

seatIDs = []
for line in data:
  rowString = line[0:7] # first seven characters used for finding the row
  columnString = line[7:len(line)] # last 3 characters used for finding the seat/column
  
  binaryRow = int(rowString.replace("F","0").replace("B","1"),2) # convert rowString to binary and get the 2-point integer representation
  binaryColumn = int(columnString.replace("L","0").replace("R","1"),2) # convert columnString to binary and get the 2-point integer representation
  # print(binaryRow)
  # print(binaryColumn)
  # print("Seat ID:", binaryRow * 8 + binaryColumn)
  seatIDs.append(binaryRow * 8 + binaryColumn)
  
allSeats = list(range(min(seatIDs),max(seatIDs))) # a list of all numbers from the lowest seat id to the highest
for id in allSeats: # loop through all seats and find the missing seat from seatIDs
  if id not in seatIDs:
    print("My Seat ID:", id)
print("Highest Seat ID:", max(seatIDs))