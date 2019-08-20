def format_comments(fstream):
    lines = fstream.readlines()
    for i, line in enumerate(lines):
        if line.endswith('$$\n'):
            continue
        elif line.count('//'):
            lines[i] = ''.join([lines[i][:-1], ' $$', lines[i][-1]])
    fstream.seek(0)
    for line in lines:
        fstream.write(line)
