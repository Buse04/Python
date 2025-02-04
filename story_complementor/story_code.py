with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for index, char in enumerate(story):
    if char == target_start:
        start_of_word = index

    if char == target_end and target_start != -1:
        word = story[start_of_word : index + 1]
        words.append(word)
        start_of_word = -1

answers = {}
for word in words:

    answer = input("Enter a word " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

