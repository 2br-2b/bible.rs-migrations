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
from itertools import islice
newlines = 0
currently_in_verse = False

book = 1
chapter = 1
last_chapter = 0
last_verse = 0

bible_file = open("pg8300.txt", "rt")
# The output is given as a csv, but the only seperators should be {s
try:
    os.remove("output.csv")
except FileNotFoundError:
    pass
output_file = open("output.csv", "a")
seperator = "{"

output_file.write("book{chapter{verse{text\n")
output_file.flush()

# iterBible = iter(bible_file)
# next(iterBible)

# for line in bible_file[195:]:
for line in islice(bible_file, 195, None):
    line = line[:len(line) - 1]

    if(len(line) == 0):
        newlines += 1
        if(currently_in_verse):
            output_file.write("\n")
            output_file.flush()
            currently_in_verse = False
        continue

    elif(line[0].isdigit() and newlines > 0 and not " Chapter " in line and len(line.split(":")[0]) < 3):
        newlines = 0
        currently_in_verse = True

        reference = line.split(".")[0]
        reference_length = len(reference) + 2

        reference_list = reference.split(":")
        chapter = reference_list[0]
        verse = reference_list[1]

        # (last_chapter > int(chapter) or
        if (last_verse > int(verse) and last_chapter == 1 and not book == 73):
            book += 1
        last_chapter = int(chapter)
        last_verse = int(verse)

        to_write = str(book) + seperator + chapter + seperator + \
            verse + seperator + line[reference_length:]
    elif(currently_in_verse):
        to_write = " " + line
    else:
        """ if(newlines == 5):
             book += 1
             newlines = 0
         if(line == "THE NEW TESTAMENT"):
             book -= 1"""
        if (line == "End of the Project Gutenberg EBook of The Bible, Douay-Rheims, Old and New"):
            break
        continue

    output_file.write(to_write)
    output_file.flush()

output_file.close()
bible_file.close()
