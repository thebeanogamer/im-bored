for i in range(1,100):
    fizzing = i % 3
    buzzing = i % 5
    if (fizzing & buzzing):
        print("Fizzbuzz")
    elif (fizzing):
        print("Fizz")
    elif (buzzing):
        print("Buzz")
    else:
        print(i)
