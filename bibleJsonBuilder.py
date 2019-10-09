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

def getBooksAndChapters():
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
    print(books)

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
    print(books)
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

def getTopics():
    jsonFile = open("topics.json", "r")
    booksdata = json.load(jsonFile)
    jsonFile.close()
    uniqueWords = []
    commonwords = ["in", "the", "of", "so", "be", "is", "was", "a", "with", "I", "thy", "thine", "thou", "they", "we"]
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''SELECT id, shortName, chapter, word FROM kjv''')
    rows = cursor.fetchall()
    db.commit()
    db.close()
    for row in rows:
      id = row[0]
      print(id)
      bookTitle = row[1]
      chapter = str(row[2])
      chapterindex = row[2]-1
      text = row[3].strip()
      wordarray = text.split(" ")
      for word in wordarray:
         _word = word.replace(".", "")
         _word = _word.replace("[", "")
         _word = _word.replace("]", "")
         _word = _word.replace("'s", "")
         _word = _word.replace(":", "")
         _word = _word.replace(",", "")
         _word = _word.replace(";", "")
         _word = _word.replace("!", "")
         _word = _word.replace("?", "")
         _word = _word.replace("(", "")
         _word = _word.replace(")", "")

         if _word.lower() in uniqueWords:
          if not id in booksdata[_word.lower()]:
            booksdata[_word.lower()].append(id)
            #print(booksdata)

         if not _word.lower() in uniqueWords:
          uniqueWords.append(_word.lower())
          booksdata[_word.lower()] = []
          booksdata[_word.lower()].append(id)
          #print(_word.lower())
    jsonFile = open("topics.json", "w+")
    jsonFile.write(json.dumps(booksdata))
    jsonFile.close()

    # with open('bibleBooks.json', 'w') as outfile:
    #    json.dump(data, outfile)

getTopics()
