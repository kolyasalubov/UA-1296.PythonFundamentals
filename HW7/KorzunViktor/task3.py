def counter(word):
    
    answer = {}
    for letter in word.lower():
        if letter in answer:
            answer[letter] += 1
        else:
            answer[letter] = 1
    print(answer)
counter('Hhello')

