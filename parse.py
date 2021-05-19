def Parse(file): 
    file_name = file.rstrip(".txt")
    new_lines = []

    with open(file) as file: 
        lines = file.readlines()

        for line in lines: 
            if line != "\n": 
                words = line.split()
                if words[0][0] == "2": 
                    new_line = ""
                    new_line_array = []
                    for x in range(len(words)-1): 
                        new_line_array.append(words[x+1] + ", ")
                        if x == len(words) - 2:
                            new_line_array.append(words[x+1] + "\n")

                    new_lines.append(new_line.join(new_line_array))


    new_file = open(file_name + "_parsed.txt", 'w')
    new_file.writelines(new_lines)
    new_file.close()

