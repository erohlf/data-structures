from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if other == None:
            return False
        return self.freq == other.freq and self.char == other.char
    
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            if self.char < other.char:
                return True
        return False

        
def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    freq_list = [0] * 256
    try:
        with open(filename) as f:
            file = f.read()
            if file == '':
                return [0]*256
            else:
                for i in file:
                    freq_list[ord(i)] += 1 
                return freq_list
    except:
        raise FileNotFoundError('file not found')

def make_node(a, b):
    c_freq = a.freq + b.freq
    c_char = None
    if a.char < b.char:
        c_char = a.char
    else:
        c_char = b.char
    
    c = HuffmanNode(c_char, c_freq)

    if a.freq < b.freq:
        c.left = a
        c.right = b
    elif a.freq == b.freq and a.char < b.char:
        c.left = a
        c.right = b
 
    return c

def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    huff_list = OrderedList()
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            huff_list.add(HuffmanNode(i, char_freq[i]))
    if huff_list.size() == 1:
        return huff_list.pop(0)
    elif huff_list.size() == 0:
        return None
    else:
        while huff_list.size() > 1:
             a = huff_list.pop(0)
             b = huff_list.pop(0)
             new_node = make_node(a, b)
             huff_list.add(new_node)
                     
     
        return huff_list.pop(0)
        
    
def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    codes = [0]*256
    create_code_helper(node,'', codes)
    return codes

def create_code_helper(node,code,codes):
    if node.left == None and node.right == None:
        codes[node.char] = code
    if node.left != None:
        create_code_helper(node.left, code + '0', codes)
    if node.right != None:
        create_code_helper(node.right, code + '1', codes)
    return codes
 
def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = []
    for i in range(len(freqs)):
        if freqs[i] != 0:
            header.append(str(i))
            header.append(str(freqs[i]))
    return ' '.join(header)
    
def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    try:
        with open(in_file) as f:
            file = f.read()
            if file == '':
                new_f = open(out_file, 'w+')
                new_f.close()
            else:
                freq_list = cnt_freq(in_file)
                hufftree = create_huff_tree(freq_list)
                codes = create_code(hufftree)
                output = ''
                header = create_header(freq_list) + '\n'   
                if hufftree.left == None and hufftree.right == None:
                    output += str(hufftree.char)
                    output += ' '
                    output += str(hufftree.freq)
                else:
                    for char in file:
                        output += codes[ord(char)]
                new_f = open(out_file, 'w+')
                new_f.write(header)
                new_f.write(output)
                new_f.close()

                comp_f = out_file[:out_file.find('.txt')]
                comp_f = comp_f + '_compressed.txt'
                bit = HuffmanBitWriter(comp_f)
                bit.write_str(header)
                bit.write_code(output) 
                bit.close()
    except:
        raise FileNotFoundError('file not found')
  
 
def parse_header(header_string):
    freqs = [0]*256
    header_lst = header_string.split()
    for i in range(len(header_lst)):
        if i % 2 == 0:
            ascii = int(header_lst[i])
        elif i % 2 != 0:
            freqs[ascii] = (int(header_lst[i]))
    return freqs 


def count_char(freqs):
    sum = 0
    for i in freqs:
        sum += i
    return sum  
    
def huffman_decode(encoded_file, decode_file):
    try:
        bits = HuffmanBitReader(encoded_file)
        header = bits.read_str()
        freqs = parse_header(header)
        char_count = count_char(freqs)
        hufftree = create_huff_tree(freqs)    
        out = open(decode_file, 'w+')
        output = ''

        if hufftree.left == None and hufftree.right == None:
            out.write(chr(hufftree.char) * hufftree.freq)
            out.close()
            bits.close()
        else:
            for i in range(char_count):
                current_node = hufftree
                while current_node.left != None and current_node.right != None: 
                    if bits.read_bit() == False:
                        current_node = current_node.left
                    else:
                        current_node = current_node.right
                output += chr(current_node.char)
            out.write(output)                           
            out.close()
            bits.close()
    except FileNotFoundError:
        raise FileNotFoundError('file not found')
    except AttributeError:
        out.close()
        bits.close()    
