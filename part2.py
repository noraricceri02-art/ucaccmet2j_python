import json
names_list =["jenseits_von_gut_und_boese", "hamlet", "beyond_good_and_evil"]

data={}
for text_name in names_list:
   
    with open (f'texts/{text_name}.txt', encoding='utf-8') as file: #the encoding = "utf-8" function is needed because the text migth (and most probabbly will contain) special characters such as accents. So the function just enables Python to read those charaters
        content= file.read()
        split_exercise = content.split()
        
        #Cleaning the data
        cleaned_words = []
        for x in split_exercise:
            count= x.strip(",.!?'';:()-")
            cleaned_words.append(count)
        
        #Making all of the text in lower cases
        for i in range(len(cleaned_words)):
           cleaned_words[i]=cleaned_words[i].lower()
        #print(len(cleaned_words))
        
         #Counting the amount of letters (consisting of two steps) I took this code from my part1
         #1:Computing the length of each word
        length_words = []
        for words in cleaned_words:
            count=  len(words)
            length_words.append(count)

        #2:Adding all the lengths
        count=0
        for number in length_words:
            count= count + number
            
        #creating a set so to have the total amount of unique words
        unique_words_set=set()
        for i in cleaned_words:
            unique_words_set.add(i)
        #print(len(unique_words_set))

        #count frequency of the word 'the' in each text
        counts = {}
        for word in cleaned_words:
            if word in counts:
                counts[word] = counts[word]+1
            else:
                counts[word]=1
        #print(counts['the'])

        #keeping only the words that appear at least 10 times
        high_words =[]
        for word in counts:
            if counts[word]>=10:
                high_words.append(word)
        print(len(high_words))

        #computing the average to insert in the JSON file.
        # Dividing the length of the 'non-split' text by the amount of words in the 'spli by space' text
        Average= count/len(split_exercise)
        
#saving to JASON
    data[text_name] = {'word_count': len(split_exercise),
        'unique_words': len(unique_words_set),
        'avg_word_length': Average,
         }
    
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
