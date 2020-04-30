def IsUnique(string) : #Space complexity O(1), time complexity O(len(string))

    for i in range(1, len(string)) :

        if string[i] != string[0] :

            return False

    return True 

print(IsUnique('ssssa'))