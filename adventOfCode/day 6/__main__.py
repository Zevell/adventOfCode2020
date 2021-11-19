f = open('input.txt', 'r')
data = f.read().split('\n\n')
f.close()

# def char_range(c1, c2):
#     """Generates the characters from `c1` to `c2`, inclusive."""
#     for c in range(ord(c1), ord(c2)+1):
#         yield chr(c)

def anyoneAnswered():
  yesCount = 0 
  for answers in data:
    if not answers:
      continue
    
    answers = answers.replace('\n','')
    
    uniqueAnswers = ''.join(dict.fromkeys([char for char in answers])) # This will return only unique characters, we join it so it is one string so "len" can be used. We create the dictionary from a list of characters rather than the string itself to allow dict to properly filter out duplicates.
    # print("answers:", uniqueAnswers)
    yesCount += len(uniqueAnswers)
  return yesCount
  
def everyoneAnswered():
  yesCount = 0
  charList = []
  for answers in data: # for each "section" or "group" of answers, created by splitting at empty lines
    if not answers:
      print("Group of answers invalid")
      continue
    
    lineCount = answers.count('\n') + 1 # +1 as the last new line is cut off with the way we split the answers
    # print(lineCount)
    answers = answers.replace('\n','').replace('\\n','').lower()
    answerCharList = [] # create an answer specific list of characters to make it more readable when printing the final char list.
    
    uniqueAnswers = dict.fromkeys([char for char in answers]) # This will return only unique characters (not repeated) as we only want to count the occurence of a specific character once per group of answers. We create the dictionary from a list of characters rather than the string itself to allow dict to properly filter out duplicates.
    
    for char in uniqueAnswers:
      if answers.count(char) == lineCount:
        yesCount += 1
        answerCharList.append(char)
    
    charList.append(answerCharList)
    # print("answers:", answers)
    
  print(charList)
  return yesCount

print("Everyone answered total:", everyoneAnswered())
print("Anyone answered total:", anyoneAnswered())
