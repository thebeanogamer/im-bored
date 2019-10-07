for i in range(1,100):
    out = ""
    if i%3 == 0:
        out += "Fizz"
    if i%5 == 0:
        out += "Buzz"
    if out:
        print(out)
    else:
        print(i)
