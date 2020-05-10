def OneAway(string1, string2) : 

    #Insertion or remotion of character

    if len(string1) != len(string2) :

        if len(string1) < len(string2) :

            Bigger = string2

            Smaller = string1

        else :

            Bigger = string1

            Smaller = string2


        if len(Bigger) - len(Smaller) != 1 :

            return False

        
        else :

            if Smaller in Bigger :

                return True


            else :

                for i in range(len(Bigger)) :

                    RemFrBig = Bigger[0 : i] + Bigger[i + 1 : ]

                    if Smaller in RemFrBig :

                        return True

                
                return False


    #Replacement of character

    else :

        if string1 == string2 :

            return False


        count = 0

        for i in range(len(string1)) :

            if string1[i] != string2[i] :

                count += 1

            if count > 1 :

                return False

        
        return True



print(OneAway('pale', 'jkfdgnlfjgn')) #False

print(OneAway('pale', 'ple')) #True

print(OneAway('pales', 'pale')) #True

print(OneAway('pale', 'bale')) #True

print(OneAway('pale', 'bake')) #False

print(OneAway('aaaa', 'aaa')) #True




