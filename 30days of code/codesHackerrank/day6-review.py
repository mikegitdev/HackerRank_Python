testCases=int(input())


for i in range(testCases):
    tesString=input()
    evenIndexedChars = ''
    oddIndexedChars = ''

    for j in range(len(tesString)):
        if j % 2 == 0:
            evenIndexedChars += tesString[j]
        else:
            oddIndexedChars += tesString[j]
    print('{} {}'.format(evenIndexedChars, oddIndexedChars))
