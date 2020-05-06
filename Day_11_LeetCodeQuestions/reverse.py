"""Time Complexity: 
This would have a run time of O(n) for best and worst cases because the while loop continues based on the number of letters there are
in the string, which is n. All the other lines of the code take O(1) because they are simple if statements."""



def reverse(string):
  left = 0
  right = len(string) - 1

  opposite = []

  while len(opposite) != len(string):
    if not string[left].isalpha():
      opposite.append(string[left])
    elif not string[right].isalpha():
      right -= 1
      continue
    else:
      opposite.append(string[right])
      right -= 1
    left += 1

  return "".join(opposite)
string = "Mike-is-so-cool"
print(reverse(string))
# string_output = "Looc-os-si-ekim"