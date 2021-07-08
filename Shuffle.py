#coding: utf8
from Options import *

class shuffle () :
    def __init__ (self,input_list) :
        """
        0 : line by line mode.
        1 : full file mode.
        """
        self.return_list = [] #Returned list with all possible combinations

        self.modes_call_dic = { #The different possible modes
            "0" : self.mode_lines,
            "1" : self.mode_full_file
        }
        
        mode = self.modes_choice()#Mode choice by user
        self.options_user = self.options_choice () #Options choice by user

        self.modes_call_dic[mode](input_list)   

    def mode_lines (self,input_list):
        lines = [i.split(':') for i in input_list]
        comb = 1 if '!' in self.options_user else 0
        self.options_user = self.options_user.replace('!','')

        #We apply options to the words line by line for input text and for generated pass
        switchOptions = options_call()
        for line in lines :
            self.return_list.append('')
            for option in self.options_user :
                a = switchOptions.indirect(option,line)
                if a != '' :
                    self.return_list[-1] += ':' + ':'.join(a)
                    if comb : #If combination option is raised
                        line += a
            self.return_list[-1] = self.return_list[-1][1:] #delete fist ':'        

    def mode_full_file (self,input_list) :
        words = [i.split(':') for i in input_list]
        pass

    def options_choice(self) :
        options = {
            '0' : 'Mix words (default)',
            '1' : 'All lowercase',
            '2' : 'All uppercase',
            '3' : 'Mix upper and lowercase',
            '4' : 'Leet speak',
            '!' : 'Combine options (Choice order is important)'
        }

        print('\n[+] Please select the desired options. Example: 014!')
        ask = 1
        for key,val in options.items() :
            print('{} : {}'.format(key,val))
        while ask == 1 :
            ask = 0
            options_user = str(input('\n>>> '))

            if options_user == '' :
                options_user = '0' 
            elif options_user == '!' :
                options_user = ''
                print('\n[+] You can\'t use this option alone.')
                ask = 1

            for i in str(options_user) : #Check if user use wrong option
                if not i in options.keys() :
                    print('\n[+] Thank you for choosing a good option.')
                    ask = 1
                    break
        
        return options_user
    
    def modes_choice(self) :
        print("[+] Chose mode :")
        print("0 : Generate a list of passwords from the input text line by line (word1:word2:...).")
        print("1 : Generate a list of passwords from the full input text (1 word per line).")
        while (1) :
            a = input("\n>>> ")
            if a in self.modes_call_dic.keys() :
                return a
            print("\n[+] Wrong choice.")