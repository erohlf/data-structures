from hash_quad import *
import string


def remove_punctuation(string):
    no_punct = ''
    for i in string:
        if i.isalpha():
            no_punct += i
        elif i != "'":
            no_punct += ' '
    return no_punct

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            with open(filename, 'r') as f:
                stop_words = f.read().split('\n')
            
            self.stop_table = HashTable(191)
            for word in stop_words:
                self.stop_table.insert(word, None)
            f.close()
        except:
            raise FileNotFoundError('file not found')


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            with open(filename, 'r') as f:
                words = f.read().split('\n')
            
            self.concordance_table = HashTable(191)

            for i in range(len(words)):
                line = words[i]
                line = remove_punctuation(line)
                line = line.lower()
                line = line.strip()
                line = line.split(' ')
                line = set(line)

                for w in line:
                    if self.stop_table.in_table(w) == False:
                        if w != '':
                            if self.concordance_table.in_table(w) == False:
                                line_nums = []
                                line_nums.append(i+1)
                                self.concordance_table.insert(w,line_nums)
                            elif self.concordance_table.in_table(w) == True:
                                val = self.concordance_table.get_value(w)
                                val.append(i+1)
                                self.concordance_table.insert(w,val)
                    else:
                        pass
        
        except:
            raise FileNotFoundError('file not found')

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        keys = self.concordance_table.get_all_keys()
        keys.sort()
        with open(filename, 'w+') as f:
            for word in keys:
                out = ''
                value = self.concordance_table.get_value(word)
                for n in value:
                    out = out + str(n) + ' '
                if word == keys[len(keys) - 1]:
                    f.write('%s: %s'%(word,out))
                else:
                    f.write('%s: %s\n'%(word,out))
        f.close()
                    
