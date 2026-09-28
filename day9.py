#LINK = https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6<=n<=20:
        print('Weird')  
    else:
        print('Not Weird')

#LINK = https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
    n = int(input())
    for i in range(n):
        print(i**2)

#LINK = https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))

