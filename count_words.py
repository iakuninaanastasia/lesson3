with open('referat.txt','r', encoding='utf-8') as file:
    text = file.read()
    word_count_in_text = int(text.count(' ')) + int(text.count('\n')) + 1
    print(word_count_in_text)