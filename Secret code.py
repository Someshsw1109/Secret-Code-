# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

message = input("Enter message : ")
words = message.split(" ")
codingOrDecoding = input("1 for Coding or 0 for Decoding\n")
codingOrDecoding = True if (codingOrDecoding=="1") else False
print(codingOrDecoding)
if(codingOrDecoding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      newMessage = r1+ word[1:] + word[0] + r2
      nwords.append(newMessage)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      newMessage = word[3:-3]
      stnew = newMessage[-1] + newMessage[:-1]
      nwords.append(newMessage)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  
  
