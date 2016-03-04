input = raw_input("Enter a value for b: ")
b = float(input)

while b == 1:
    print "b cannot equal 1."
    input = raw_input("Enter a different value for b: ")
    b = float(input)

input2 = raw_input("Enter a value for n: ")
n = int(input2)

i = 0
sump = 0
while i <= n:
    sump += b**i
    i += 1
print "%d is your first result." % sump


part2 = ((b**(n+1))-1)/(b-1)
print "%d is your second result." % part2
