def CheckPermutation(s1, s2) : # SC O(len(s2) + len(s1)), TC O(len(s2) + len(s1))

    s1 = ''.join(sorted(s1)) # SC O(len(s1)), TC O(len(s1))

    s2 = ''.join(sorted(s2)) # SC O(len(s2)), TC O(len(s2))

    if s1 == s2 :

        return True

    return False

print(CheckPermutation('semen', 'nemes'))

print(CheckPermutation('aab', 'aba'))

print(CheckPermutation('wewf', 'wef'))

print(CheckPermutation('frg', 'XxX'))

