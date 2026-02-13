story = input("Enter the story:\n")

words = story.split()

filtered_words = []

for word in words:

    clean = word.lower().strip('.,!?;:"\'')
    
    if clean not in ['a', 'an', 'the']:
        filtered_words.append(word)

result = " ".join(filtered_words)

print("\nStory without articles:\n")
print(result)
