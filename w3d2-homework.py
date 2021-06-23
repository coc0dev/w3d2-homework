#--------------------------------------
# Exercise 1
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

# lambda + filter to remove spaces
remove = lambda r: r.strip()
print(list(filter(remove, places)))

#---------------------------------------
# Exercise 2
# HINT! sorted(key=)
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
sort = sorted(authors, key = lambda a: a.split()[-1].lower())
print(sort)


#---------------------------------------
# Exercise 3
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

temp = lambda t:(t[0], t[1]*(9/5)+32)
print(list(map(temp, places)))

#----------------------------------------
# Exercise 4
def fib(num):
  if num <= 1:
    return num
  else:
      return (fib(num-1) + fib(num-2))
  
n = int(input("Enter a number: "))
if n <=0:
  print("Only positive numbers please.")
else: 
  print(f"Fibonacci up to sequence of {n}")
  for i in range(n):
    print(fib(i))