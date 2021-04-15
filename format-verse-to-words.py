""" CREATE TABLE words (
    id INTEGER PRIMARY KEY NOT NULL,
    book INTEGER NOT NULL,
    chapter INTEGER NOT NULL,
    paragraph INTEGER NOT NULL,
    verse INTEGER NOT NULL,
    position INTEGER NOT NULL,
    word TEXT NOT NULL,
    punctuation TEXT,
    italic BOOLEAN NOT NULL,
    close_parentheses BOOLEAN NOT NULL,
    open_parentheses BOOLEAN NOT NULL
);
INSERT INTO words VALUES(1,1,1,1,1,0,'In',NULL,0,0,0);
INSERT INTO words VALUES(2,1,1,1,1,1,'the',NULL,0,0,0);
INSERT INTO words VALUES(3,1,1,1,1,2,'beginning',NULL,0,0,0);
INSERT INTO words VALUES(4,1,1,1,1,3,'God',NULL,0,0,0);
INSERT INTO words VALUES(5,1,1,1,1,4,'created',NULL,0,0,0); """

import os

bible_file = open("output.csv", "rt")
try:
    os.remove("verses-script.txt")
except FileNotFoundError:
    pass
output_file = open("verses-script.txt", "a")

verse_id = 1
italic = 0

iterBible = iter(bible_file)
next(iterBible)


for line in iterBible:
    spl = line[:len(line) - 1].split("{")
    book = int(spl[0])
    chapter = int(spl[1])
    verse = int(spl[2])
    position = 0
    paragraph = 1
    open_parentheses = 0
    close_parentheses = 0

    for word in spl[3].split(" "):
        try:
            if not word[len(word) - 1].isalpha() and not word[len(word) - 1] == ")":
                punctuation = f"'{word[len(word) - 1]}'"
                word = word[:len(word) - 1]
            else:
                punctuation = "NULL"

            if(word[0] == "("):
                open_parentheses = 1
                word = word[1:]
            else:
                open_parentheses = 0

            if(word[len(word) - 1] == ")"):
                close_parentheses = 1
                word = word[:len(word) - 1]
            else:
                close_parentheses = 0

            output_file.write(
                f"INSERT INTO words VALUES({str(verse_id)},{str(book)},{str(chapter)},{str(paragraph)},{str(verse)},{str(position)},'{word}',{punctuation},{str(italic)},{str(open_parentheses)},{str(close_parentheses)});\n")
            output_file.flush()

            verse_id += 1
            position += 1
        except IndexError:
            continue

bible_file.close()
output_file.close()
