import json

jsonFile = open("bibleBooks.json", "r")
booksdata = json.load(jsonFile)
jsonFile.close()

book = input("book: ")
chapter = input("chapter: ")
verse = input("verse: ")

print(booksdata[book][int(chapter)-1][chapter][int(verse)-1])