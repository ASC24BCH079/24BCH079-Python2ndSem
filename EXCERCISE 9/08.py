def remove_some_words():
    f = open('para.txt', 'r')
    new = open('filtered_para.txt', 'w')

    for line in f:
        words = line.split()
        clean = []
        for w in words:
            if w.lower() not in ['a', 'an', 'the']:
                clean.append(w)
        new.write(' '.join(clean) + '\n')

    f.close()
    new.close()
    print("Words removed and saved.")

remove_some_words()
