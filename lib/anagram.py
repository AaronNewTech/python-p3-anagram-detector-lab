# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        

    def match(self, word_list):
        tested_list = list()
        
        sorted_word = "".join(sorted(self.word))
        for i in range(len(word_list)):
            sorted_list_word = "".join(sorted(word_list[i]))
            if sorted_list_word == sorted_word:
                tested_list.append(word_list[i])


        
        print(tested_list)
        return tested_list
        
        # Class Anagram in anagram.py returns an empty list if the input list contains no words that match the initialized word.
        # tested_list = list()
        # for i in range(len(list)):
        #     for j in range(len(word)):
        #         if word[j] == list[i][j]:
        #             tested_list.append(list[i])
        #         else:
        #             return tested_list
            
        pass
            
            
    
listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])