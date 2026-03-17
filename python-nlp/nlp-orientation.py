for line in open("avatarSpeeches.txt", encoding="utf=8"):
    for word in line.split():
        if word.startswith('a'):
            if word.endswith('ed'):
                print(word)