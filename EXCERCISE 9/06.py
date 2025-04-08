def alt_merge_files():
    f1 = open('a.txt', 'r')
    f2 = open('b.txt', 'r')
    out = open('merged_lines.txt', 'w')

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    l1 = len(lines1)
    l2 = len(lines2)

    for i in range(max(l1, l2)):
        if i < l1:
            out.write(lines1[i])
        if i < l2:
            out.write(lines2[i])

    f1.close()
    f2.close()
    out.close()

    print("Merging done.")

alt_merge_files()
