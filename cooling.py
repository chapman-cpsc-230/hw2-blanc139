input = raw_input("Enter the temperature of your tea in degrees Celsius: ")
T = float(input)

input2 = raw_input("Enter the temperature of the air in degrees Celcius: ")
T_a = float(input2)

input3 = raw_input("Enter the number of minutes that have passed: ")
min = float(input3)

print "Temperature of the air: %d degrees Celcius." % (T_a)
print "Number of minutes: %d minutes. " % (min)
print "Minute Temperature"

k = 0.055
i = 0
while i <= min:
    T = T - k * (T - T_a)
    i += 1
    print "%3.0d       %0.1f" % (i, T)
