def CheckPermutation(string1, string2) :#Space complexity O(1), time complexity O(len(set(string1))*len(string1))

    if len(string1) == len(string2) :

        for i in set(string1) :

            if string1.count(i) != string2.count(i) :

                return False

        return True

    return False


print(CheckPermutation('semen', 'nemes'))


