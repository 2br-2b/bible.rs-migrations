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


newlines = 0
currently_in_verse = False

book = 42
chapter = 1

bible_file = open("Test 1.txt", "rt")
output_file = open("output.txt", "a")
seperator = "{"

for line in bible_file:
    line = line[:len(line) - 1]

    if(len(line) == 0):
        newlines += 1
        if(currently_in_verse):
            output_file.write("\n")
            output_file.flush()
            currently_in_verse = False
        continue

    elif(line[0].isdigit()):
        newlines = 0
        currently_in_verse = True

        reference = line.split(".")[0]
        reference_length = len(reference) + 2

        reference_list = reference.split(":")
        chapter = reference_list[0]
        verse = reference_list[1]

        to_write = str(book) + seperator + chapter + seperator + \
            verse + seperator + line[reference_length:]
    elif(currently_in_verse):
        to_write = " " + line
    else:
        continue

    output_file.write(to_write)
    output_file.flush()

output_file.close()
