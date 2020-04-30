def CheckPermutation(string1, string2) :#Space complexity O(len(string1)), time complexity O(len(string1)^2 + len(string1)*len(string2))

    if len(string1) == len(string2) : 

        for i in set(string1) :

            if string1.count(i) != string2.count(i) :

                return False

        return True

    return False


print(CheckPermutation('semen', 'nemes'))

print(CheckPermutation('aab', 'aba'))

print(CheckPermutation('wewf', 'wef'))

print(CheckPermutation('frg', 'XxX'))

# Que pasa si ordenamos string1 y string2, como lo solucionaria?
# busque metodo >>> sort <<<<




