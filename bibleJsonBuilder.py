import sqlite3
import json

def getVerses():
    booklist = []
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM kjv''')
    rows = cursor.fetchall()
    data = {"bible":[]}
    book = ""
    chapter = 0
    verse = 0
    for row in rows:
      bookTitle =  row[8]
      bookTitleShort = row[9]
      chapter = row[2]
      verse = row[3]
      word = row[4].strip()
      element = {"book": bookTitle, "chapter": chapter, "verse": verse, "word": word}
      data["bible"].append(element)
    db.commit()
    db.close()
    with open('bibleBooks.json', 'w') as outfile:  
       json.dump(data, outfile)

def getBooks():
    booklist = []
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''SELECT shortName, totalChapters FROM BibleInfo''')
    rows = cursor.fetchall()
    data = {}
    books = []
    bookandchapters = {}
    db.commit()
    db.close()
    for row in rows:
      bookTitle = row[0]
      books.append(bookTitle)
      totalChapters = row[1]
      bookandchapters[bookTitle] = totalChapters
      # bookTitleShort = row[9]
      # chapter = row[2]
      # verse = row[3]
      # word = row[4].strip()
      # element = {"book": bookTitle, "chapter": chapter, "verse": verse, "word": word}
    jsonFile = open("bibleBooks.json", "r")
    booksdata = json.load(jsonFile)
    jsonFile.close()
    for book in books:
        totalchapters = bookandchapters[book]
        for x in range(1, totalchapters+1):
            chapters = {x: []}
            booksdata[book].append(chapters)
    jsonFile = open("bibleBooks.json", "w+")
    jsonFile.write(json.dumps(booksdata))
    jsonFile.close()

    # with open('bibleBooks.json', 'w') as outfile:
    #    json.dump(data, outfile)

def getWord():
    jsonFile = open("bibleBooks.json", "r")
    booksdata = json.load(jsonFile)
    jsonFile.close()

    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''SELECT shortName, chapter, word FROM kjv''')
    rows = cursor.fetchall()
    db.commit()
    db.close()
    for row in rows:
      bookTitle = row[0]
      chapter = str(row[1])
      chapterindex = row[1]-1
      word = row[2].strip()
      booksdata[bookTitle][chapterindex][chapter].append(word)

    jsonFile = open("bibleBooks.json", "w+")
    jsonFile.write(json.dumps(booksdata))
    jsonFile.close()

    # with open('bibleBooks.json', 'w') as outfile:
    #    json.dump(data, outfile)

getWord()