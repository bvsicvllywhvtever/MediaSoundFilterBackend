from ..db_connection import db
import pandas as pd
import json

def getSupportedSounds():
    cursor = db.cursor()

    cursor.execute("SELECT Sounds.sound, Sound_Categories.category FROM Sounds INNER JOIN Sound_Categories ON Sounds.category=Sound_Categories.id")
    
    result = cursor.fetchall()

    df = pd.DataFrame(result, columns = cursor.column_names)
    json_data = df.to_json(orient='records')
    json_data = json.loads(json_data)
    json_data = json.dumps(json_data, indent=4)

    return json_data