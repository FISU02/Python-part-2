import string

def count_words(text):
    
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).split()


    word_count = len(words)

    
    stats = {}

   
    for word in words:
        if word[-1].isalpha():  
            last_letter = word[-1].lower()  
            if last_letter in stats:
                stats[last_letter] += 1
            else:
                stats[last_letter] = 1

    return word_count, stats


file_path = "C:\Users\User\Downloads\"
with open(file_path, "r") as file:
    text = file.read()


word_count, letter_stats = count_words(text)

print("Liczba słów:", word_count)
print("Statystyki liter kończących słowa:")
for letter, count in letter_stats.items():
    print(f"{letter}: {count}")
