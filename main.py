def readint(prompt, min, max):
        val=int(input(prompt))
        assert val<=max and val>=min
        return val
try:
    v = readint("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)
except ValueError:
    print("Error: wrong input")
except AssertionError:
    print("Error: the value is not within permitted range (-10..10)")
