from ..db_connection import db

def getSupportedSounds():
    cursor = db.cursor()

    cursor.execute("SELECT Sounds.sound, Sound_Categories.category FROM Sounds INNER JOIN Sound_Categories ON Sounds.category=Sound_Categories.id")
    
    result = cursor.fetchall()
    result = categorizeSounds(result)

    return result

def categorizeSounds(sounds):
    categorized_sounds = {}

    for sound in sounds:
        if sound[1] not in categorized_sounds.keys():
            categorized_sounds[sound[1]] = [sound[0]]
        else:
            categorized_sounds[sound[1]].append(sound[0])
    
    return categorized_sounds