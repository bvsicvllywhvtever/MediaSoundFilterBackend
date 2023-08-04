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

    current_app.logger.info("GOT HERE", file=sys.stderr)
    print (sounds)
    print(sound_placeholders)

    cursor.execute(f"SELECT start_time, end_time FROM Sound_Times JOIN Sounds on Sound_Times.sound = Sounds.id WHERE video_id=%s AND Sounds.sound IN ({sound_placeholders})" +
                   "ORDER BY start_time, end_time",
                    videoId, sounds)

    result = cursor.fetchall
    simplify_times(result)

    df = pd.DataFrame(result, columns = cursor.column_names)
    json_data = df.to_json(orient="records")
    json_data = json.loads(json_data)
    json_data = json.dumps(json_data, indent=4)
    
    return json_data


def simplify_times(times):
    simplified_times = []

    start = times[0].get("start_time")

    for i in range(0, len(times) - 1):
        first = times[i].get("end_time")
        second = times[i+1].get("start_time")

        if(second > first + 1):
            simplified_times.add((start, first))
            start = second
        elif i == len(times) - 2:
            simplified_times.add(start, times[i+1].get("end_time"))

    return simplified_times
