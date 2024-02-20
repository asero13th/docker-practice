def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'FizzBuzz'
    else:
        return i

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(fizzbuzz(n))