def PalindromePermutation(string) : #Space complexity O(1), time complexity O(len(StrSet)^2*len(string))

    string = string.replace(' ', '')

    string = string.lower()

    StrSet = set(string)

    if len(string) % 2 == 0 :

        for i in StrSet : #TC O(len(StrSet)*len(string))

            if string.count(i) % 2 != 0 : #TC O(len(string))

                return False

        return True

    else :

        for i in StrSet : #TC O(len(StrSet)*(len(StrSet)*len(string))) --> O(len(StrSet)^2*len(string))

            if string.count(i) % 2 != 0 : #TC O(len(string)+len(StrSet)*len(string)) --> O(len(StrSet)*len(string))

                StrSet.discard(i)

                for j in StrSet : #TC O((len(StrSet) - 1)*(len(string))) --> O(len(StrSet)*len(string))

                    if string.count(j) % 2 != 0 : #TC O(len(string))

                        return False

        
                return True


print(PalindromePermutation('Tact Coa'))