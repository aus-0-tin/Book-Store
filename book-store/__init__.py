import sqlite3

CONN = sqlite3.connect('books.db')
CURSOR = CONN.cursor()
