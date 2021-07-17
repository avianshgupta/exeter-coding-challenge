import csv
import os, psutil, time
import string
from collections import OrderedDict

def make_dictionary():
    """
    Initialize the english_to_french dictionary with values [english_word, french_translation]
    for words present in find_words.txt that has a translation in the french_dictionary.csv
    """
    dict_words = {}
    words = open('find_words.txt')
    for line in words.readlines():
        dict_words[line.strip()] = 0

    f = open('french_dictionary.csv','r')
    reader = csv.reader(f)
    for row in reader:
        if row[0] in dict_words:
            english_to_french[row[0]] = row[1]

def translate():
    """
    Translate all the words in input file which has a translation in the dictionary while 
    preserving the case (upper, lower, capitalize) and write that to output file (t8.shakespeare.translated.txt)
    and write the english word, replaced word and frequency to another csv file (frequency.csv)
    """
    frequency = OrderedDict()
    output_file = open('t8.shakespeare.translated.txt', 'w')
    input_file = open('t8.shakespeare.txt', 'r')
    for line in input_file:
        for word in line.split():
            if word.lower() in english_to_french or (word[:-1].lower() in english_to_french and word[-1] in string.punctuation):
                t_word = word if word.lower() in english_to_french else word[:-1]
                if t_word.islower():
                    output_file.write(word.replace(t_word, english_to_french[t_word.lower()]))
                elif t_word.isupper():
                    output_file.write(word.replace(t_word, english_to_french[t_word.lower()].upper()))
                elif t_word[0].isupper():
                    output_file.write(word.replace(t_word, english_to_french[t_word.lower()].capitalize()))
                if t_word.lower() in frequency:
                    frequency[t_word.lower()] += 1
                else:
                    frequency[t_word.lower()] = 1
            else:
                output_file.write(word)
            output_file.write(" ")
        output_file.write("\n")
                    
    header = ['English word', 'French word', 'frequency']
    with open('frequency.csv', 'w+', newline='') as frequency_file:
        write = csv.writer(frequency_file) 
        write.writerow(header)
        for translation in sorted(frequency.keys()):
            write.writerow([translation, english_to_french[translation], frequency[translation]])

if __name__ == '__main__':
    start_time = time.time()
    english_to_french = {}
    make_dictionary()
    translate()
    execution_time = str(time.time()-start_time)
    total_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

    #writing execution time and memory usage in performance.txt file
    with open('performance.txt', 'w') as performance_file:
        performance_file.write('Time to process: ' + execution_time + ' seconds')
        performance_file.write("\n" + 'Memory used: ' + str(total_memory) + ' MB') 






   
       
       





















