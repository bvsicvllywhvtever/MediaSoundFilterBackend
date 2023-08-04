from ..db_connection import db
import pandas as pd
import json
from flask import current_app

def setMuteTime(videoId, sound, start_time, end_time):
    cursor = db.cursor()

    cursor.execute(f"INSERT INTO Sound_Times (video_id, sound, start_time, end_time) SELECT %s, id, %s, %s FROM Sounds WHERE sound=%s", videoId, start_time, end_time, sound)

    db.commit()

def getMuteTimes(videoId, sounds):
    cursor = db.cursor()

    sound_placeholders = ', '.join(['%s'] * len(sounds))
    placeholder_values = (videoId,) + tuple(sounds)

    cursor.execute(f"SELECT start_time, end_time FROM Sound_Times JOIN Sounds on Sound_Times.sound = Sounds.id WHERE video_id=%s AND Sounds.sound IN ({sound_placeholders}) " +
                   "ORDER BY start_time, end_time",
                    placeholder_values)

    result = cursor.fetchall()
    result = simplify_times(result)

    df = pd.DataFrame(result, columns = cursor.column_names)
    json_data = df.to_json(orient="records")
    json_data = json.loads(json_data)
    json_data = json.dumps(json_data, indent=4)
    
    return json_data


def simplify_times(times):
    current_app.logger.info(times)
    simplified_times = []

    start = times[0][0]

    for i in range(0, len(times) - 1):
        first = times[i][1]
        second = times[i+1][0]

        if(second > first + 1):
            simplified_times.append((start, first))
            start = second
        elif i == len(times) - 2:
            simplified_times.append((start, times[i+1][1]))

    return simplified_times
