def goodString(string: str): # convert string into number, base is 0
  count = 0; passCount = 0
  arr = []

  for i in range(len(string)):
    if passCount > 0:
      passCount -= 1
      continue

    else:
      if string[i] == 'a':
        count += 1
      else:
        arr.append(count-1)
        passCount = count-1
        count = 0

  return arr

print(goodString("aabbabab"))
