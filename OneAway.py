def OneAway(string1, string2) : #SC O(1), TC O(len(string1)^2) or O(len(string2)^2) wichever is bigger

    if len(string1) == len(string2) + 1 : #TC O(1)

        for i in string1 : #TC O(len(string1)^2)

            if string2 == string1.replace(i, '') : #TC O(len(string1))

                return True #TC O(1)

        return False #TC O(1)

    elif len(string2) == len(string1) + 1 : #TC O(1)

        for i in string2 : #TC O(len(string2)^2)

            if string1 == string2.replace(i, '') : #TC O(len(string2))

                return True #TC O(1)

        return False #TC O(1)

    elif len(string1) == len(string2) : #TC O(1)

        if string1 == string2 : #TC O(1)

            return False #TC O(1)

        for i in range(len(string1)) : #TC O(len(string1)^2)

            if string1[i] != string2[i] : #TC O(1)

                for j in range(i + 1, len(string1)) : #TC O(len(string1))

                    if string1[j] != string2[j] : #TC O(1)

                        return False #TC O(1)

                return True #TC O(1)

    else : #TC O(1)

        return False #TC O(1)


print(OneAway('pale', 'jkfdgnlfjgn'))
