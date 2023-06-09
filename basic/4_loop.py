# while Loop:
def ex1():
    count = 0
    sum = 0
    while True:
        numInp = input('Enter a number: ')
        if (numInp == 'done'):
            break
        try:
            num = float(numInp)
        except:
            print('Invalid input')
            continue
        count += 1
        sum += num
    average = sum / count
    print(count, sum, average)


# for Loop:
def ex2():
    nums = [12, 15, 5, 46, 87, -29, -31, 45, 3]
    max = None
    min = None

    for num in nums:
        if ((max is None) or (min is None)):
            max = num
            min = num
        else:
            if (max < num):
                max = num
            if (min > num):
                min = num
    print(max, min)


ex1()
ex2()
