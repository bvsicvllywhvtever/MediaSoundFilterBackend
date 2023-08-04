from ..db_connection import db
from flask import jsonify

def getSupportedSounds():
    cursor = db.cursor()

    cursor.execute("SELECT Sounds.sound, Sound_Categories.category FROM Sounds INNER JOIN Sound_Categories ON Sounds.category=Sound_Categories.id")
    
    result = cursor.fetchall()
    result = categorizeSounds(result)

    return jsonify(result)

def categorizeSounds(sounds):
    categorized_sounds = {}

    for sound in sounds:
        if sound[1] not in categorized_sounds.keys():
            categorized_sounds[sound[1]] = [sound[0]]
        else:
            categorized_sounds[sound[1]].append(sound[0])


    categorized_sounds = [{"category" : k, "sounds": v} for k, v in categorized_sounds.items()]
    
    return categorized_sounds