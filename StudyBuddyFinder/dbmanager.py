from flask import g
from StudyBuddyFinder.db import Database

def get_db():
    if 'db' not in g:
        g.db = Database()
    return g.db