sentence = input("Enter a sentence: ")
#split the sentence into words
words = sentence.split()
#initialize a dictionary
word_count = {}
#count word frequency
for word in words:
    word = word.lower() #convert to lower case
    if word in word_count: 
        word_count[word] += 1 #increment the count
    else:
        word_count[word] = 1 #initialize the count
print(word_count) #print the dictionary