def URLify(string) :   #Space complexity O(1), time complexity O(len(string.strip()))

    NewString = ''

    for i in string.strip() :

        if i == ' ' :

            NewString += '%20'

        else :

            NewString += i

    
    return NewString


print(URLify('Mr John Smith    '))




