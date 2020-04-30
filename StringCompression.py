def StringCompression(string) : #SC O(1), TC O(len(string))

    string += ' '

    CurrChar = string[0]

    CompString = ''

    Count = 0

    for i in range(len(string)) :

        if string[i] == CurrChar :

            Count += 1

        else :

            CompString += CurrChar + str(Count)

            CurrChar = string[i]

            Count = 1


    if len(string) - 1 > len(CompString) :


        return CompString

    else :

        return string[:len(string) - 1]


print(StringCompression('aabcccccaaa'))

