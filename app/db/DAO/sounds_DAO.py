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

def setSounds(id, sounds):
    cursor = db.cursor()

    for sound in sounds:
        for pair in sounds[sound]:
            cursor.execute("INSERT INTO Sound_Times (video_id, sound, start_time, end_time) VALUES (%s, %s, %s, %s)", (id, sound, pair[0], pair[1]))
            db.commit()