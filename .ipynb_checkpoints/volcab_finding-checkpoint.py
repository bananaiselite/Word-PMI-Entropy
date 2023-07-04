from collections import Counter
import numpy as np
import re 
import pandas as pd
from tqdm import tqdm 
from .utils import fullwidth_to_halfwidth, remove_english

class main:
    
    def __init__(self):
        
        self.stopwords = ['【','】',')','(','、','，','“','”','。','\n','《','》',' ','-','！','？','.','\\','[',']','：','/','.','"','\u3000','’','．',',','…','?','「','」', '+']
            
    
    def n_gram_words(self, text, n_gram):
        """
        To get n_gram word frequency dict
        n_gram : 作為單詞的最大字串長度
        output: word frequency dict
        """
        # 建立空的單詞列表
        words = []
        self.text = text

        # 從文本中擷取從1 ~ n_gram長度的字串，作為單詞計算詞頻
        for i in range(1, n_gram+1):
            words += [text[j:j+i] for j in range(len(self.text)-i+1)]

        # 計算單詞列表中的所有單詞的詞頻
        words_freq = dict(Counter(words))

        return words_freq      
    
    @staticmethod
    def PMI_filter(word_freq_dic, min_p):
        """
        To get words witch  PMI  over the threshold
        word_freq_dic: word frequency dict 
        min_p: min threshold of PMI
        output: condinated word list

        """
        # 建立空的單詞列表
        new_words = []

        # 若單詞長度為 1，則跳過
        for word in word_freq_dic:

            if len(word) == 1:
                continue

            # 如果單詞內的字詞一起出現的頻率越大，該凝合度越大，越可能成為一個單詞

            p_x_y = min([word_freq_dic[word[:i]]* word_freq_dic[word[i:]] for i in range(1, len(word))])

            mpi = p_x_y / word_freq_dic[word]

            # 如果PMI大於thershold，則加入單詞列表
            if mpi > min_p:
                new_words.append(word)

        return new_words
    
    @staticmethod
    def calculate_entropy(char_list):
        """
        To calculate entropy for  list  of char
        char list : 計算過凝合度的候選單詞
        output: entropy of the list  of char
        """
        char_freq_dic =  dict(Counter(char_list)) 
        entropy = (-1) * sum([ char_freq_dic.get(i) / len(char_list) * np.log2(char_freq_dic.get(i) / len(char_list)) 
                            for i in char_freq_dic])
        return entropy

    @classmethod
    def Entropy_left_right_filter(cls, condinate_words, text, min_entropy):
        """
        To filter the final new words from the condinated word list by entropy threshold
        input:  condinated word list ,min threshold of Entropy of left or right
        condinate_words : 計算過凝合度的候選單詞
        output: final word list
        """
        # Initialize an empty list to store the final words
        final_words = []
        
        # 若字串為純數字則跳過
        for word in condinate_words:
            if word.isnumeric():
                continue

            try:
                # 從文本中取出候選單詞出前時所有的前後字
                left_right_char = re.findall('(.)%s(.)'%word, text)
                # 取出候選單詞前一個的字
                left_char = [i[0] for i in left_right_char]
                # 計算前字的自由度
                left_entropy = cls.calculate_entropy(left_char)
                # 取出候選單詞後一個的字
                right_char = [i[1] for i in left_right_char]
                # 計算後字的自由度
                right_entropy = cls.calculate_entropy(right_char)

                # 自由度越高，越有可能為獨立單詞
                if min(right_entropy,left_entropy)> min_entropy:
                    final_words.append(word)
            except Exception as e:
                print("An error occurred while processing the word:", word)
                print("Error message:", str(e))

        return final_words
    
    def run(self,
            text ,
            max_len = 6,
            min_p =4, 
            min_e = 2):
        
        """
        text:要探勘的文本
        max_len: 最大的單詞探勘長度，越大運算量越高，太小會無法抓出單詞，Ex: max_len=3時，會無法抓出智慧型手機
        min_p : 自由度門檻
        min_e : Entropy門檻
        """
        
        text = fullwidth_to_halfwidth(text)
        text = remove_english(text)
        
        # 去除文字中停用字詞
        for s in self.stopwords :
            text = text.replace(s, "")
        

        n_gram = self.n_gram_words(text, max_len)
        condinate = self.PMI_filter(n_gram , min_p)
        final = set(self.Entropy_left_right_filter(condinate, text, min_e))
        
        return final