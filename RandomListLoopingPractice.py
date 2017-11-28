n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in numbers:
    result = result + i
  return result

def total2(numbers):
    result = 0
    for i in range(len(numbers)):
        result = result + numbers[i]
    return result
   
    
print(total(n))
print(total2(n))

# Join strings together
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in words:
    result = result + i
  return result


print(join_strings(n))

# Concatenate two lists into one list
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
  return x + y

print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]



# Loop through list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers:
      results.append(i)
  return results

print(flatten(n))