#DS - Task - 2

sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog!.' #single string
sentence_1 = sentence.replace('!', ' ') #remove exclamation mark
print(sentence_1)
sentence_2 = sentence_1.replace('.', '') #remove dot at the end of the sentence
sentence_3 = sentence_2.strip(' ') #strip blank space 
sentence_4 = sentence_3 + '.' #add dot without blank space
print(sentence_4)
print(sentence_4.upper()) #print in upper case
print(sentence_4[::-1]) #print string in reverese