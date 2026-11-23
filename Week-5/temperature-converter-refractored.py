def converter(faren):
    return (int(f) - 32) //1.8


f = input("Enter farenheight temperature you'd like to convert to celcius: ")
c = converter(f) 
print( f + " farenehight is " + str(c) + " celcius")
