def IsSubstring(s1, s2) :#SC O(1), TC O(1)
    
    if s1 in s2 :

        return True

    elif s2 in s1 :

        return True

    
    return False



def StringRotation(s1, s2) : #SC O(1), TC O(1)

    if len(s1) == len(s2) :

        s1 *= 2

        if IsSubstring(s1, s2) : #SC O(1), TC O(1)

            return True

    return False


print(StringRotation('abcd', 'bcda')) #True

print(StringRotation('abcd', 'bdca')) #False

print(StringRotation('erbottlewat', 'waterbottle')) #True


    
