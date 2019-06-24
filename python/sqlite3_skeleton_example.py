#!/usr/bin/env python3
# This is a sample sqlit3 code to use in other projects
# This mimics a password store/retrieval projects
import sqlite3
import os
import hashlib

pathToDB = os.path.join(os.path.dirname(__file__), 'passwordHashDatabase.sqlite3')

# isloation_level=None autocommits execute statements
# Otherwise you need to periodically call con.commit() to save to the DB
# also, creating the connection automatically creates the file if it doesnt exist
con = sqlite3.connect(pathToDB, isolation_level=None) 
cur = con.cursor()

def setupDB():
    """
    Creates the table structure within the DB
    """
    firstTable = """
    CREATE TABLE hashes (
        userName text PRIMARY_KEY,
        passwordHash text NOT NULL)
        """
    cur.execute(firstTable)

def hashPassword(password):
    hashAlgo = hashlib.md5()  # ya ya I know its bad, its an example....
    hashAlgo.update(password.encode('utf8'))
    return hashAlgo.hexdigest()

def addPasswordHash(username, password):
    """
    Saves the hashsed password it to the DB
    """
    passwordHash = hashPassword(password)
    cur.execute("INSERT INTO hashes (userName, passwordHash) VALUES (?,?)", (username, passwordHash))

def validatePassword(username, password):
    cur.execute("SELECT passwordHash FROM hashes WHERE userName=?", (username,) )
    databasePasswordHash = cur.fetchone()
    suppliedPasswordHash = hashPassword(password)
    if databasePasswordHash == suppliedPasswordHash:
        print("CORRECT PASSWORD")
    else:
        print("WRONG PASSWORD")
            
validatePassword('jimmy', 'Password1')