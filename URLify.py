def URLify(string) :   #Space complexity O(1), time complexity O(len(string.strip()))

    NewString = ''

    for i in string.strip() :

        if i == ' ' :

            NewString += '%20'

        else :

            NewString += i

    
    return NewString


print(URLify('Mr John Smith    ')) # Mr%20John%20Smith

print(URLify('M Jo ith  ')) # M%20Jo%20ith




