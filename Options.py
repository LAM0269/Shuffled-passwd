from itertools import permutations

class options_call ():
    def indirect(self,option,input_list):
        method = getattr(self,'option_'+str(option))
        return method(input_list)

    def option_0 (self,input_list) :
        """Returns a list of all possible permutations."""
        if isinstance(input_list, list) :
            a = list(permutations(input_list))
            return [''.join(i) for i in list(a)]
        else :
            return ''

    def option_1 (self,input_list) :
        """All lowercase"""
        return [i.lower() for i in input_list]

    def option_2 (self,input_list) :
        """All uppercase"""
        return [i.upper() for i in input_list]

    def option_3 (self,input_list) :
        pass

    def option_4 (self,input_list) :
        leet = {
            'A' : '@',
            'B' : '8',
            'C' : '©',
            'E' : '3',
            'G' : '6',
            'I' : '1',
            'O' : '0',
            'P' : '9',
            'S' : '$',
            'T' : '7',
            'U' : 'µ',
            'X' : '×'
        }
        
        ret = []

        if isinstance(input_list, list) :
            for i in input_list :
                for key,val in leet.items() :
                    if key in i or key.lower() in i :
                        i = i.replace(key,val)
                        i = i.replace(key.lower(),val)
                ret.append(i)
        else : 
            for key,val in leet.values() :
                    if key in input_list :
                        ret = input_list.replace(key,val)

        return ret
