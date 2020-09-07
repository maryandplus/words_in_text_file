with open(r"my_ascii_file.txt") as f:
    word_list=f.readlines()

for i in range(len(word_list)):
    
    print(word_list[1:][i])
    counter = len(word_list[1:][i].split()) 
    print('number of words'+' ' + str(counter) + '\n')
