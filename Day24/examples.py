# https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing
# Above link covers possible modes to open file
# a+ is read/write mode with starting pointer at the end
# seek function is used to move pointer since from that position we will do read/write functions

with open("textfile.txt", "a+") as file:
    file.seek(0)
    print(file.read())
    file.write("New stuff")
    file.seek(0)
    print(file.read())
