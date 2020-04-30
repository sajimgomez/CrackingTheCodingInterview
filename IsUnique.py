def IsUnique(string) : #SC O(len(string)), TC O(len(string))

    if len(string) == len(set(string)) : #SC O(len(string)), TC O(len(string))

        return True #SC O(1), TC O(1)

    return False #SC O(1), TC O(1)


print(IsUnique('eaio'))

print(IsUnique('aaattv'))

print(IsUnique('qwwwdr'))

print(IsUnique('qwertyuiop'))

