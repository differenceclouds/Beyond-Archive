with open('merge.txt', 'w') as outfile:
    for i in range(628):
        with open("page"+str(i + 1)+".txt") as infile:
            outfile.write(infile.read())