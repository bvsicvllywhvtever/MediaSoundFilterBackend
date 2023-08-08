from sound_model.youtube_extractor_pytube import extract_audio
from sound_model.sound_classifier import run_inference
from sound_model.supported_sounds import supportedSounds
import db.DAO.sounds_DAO as sounds_DAO

from flask import current_app

def cleanSounds(sounds):
    #grab only the sounds currently supported, and translate them to the id in the DB (values in supportedSounds)
    condensed_sounds = {}

    for sound_id in sounds:
        if(sound_id in supportedSounds):
            if(supportedSounds[sound_id] in condensed_sounds):
                condensed_sounds[supportedSounds[sound_id]].extend(sounds[sound_id])
            else:
                condensed_sounds[supportedSounds[sound_id]] = sounds[sound_id]

    #sort each array in dict
    for sound in condensed_sounds:
        condensed_sounds[sound].sort()

    #create pairs
    all_pairs = {}
    for sound in condensed_sounds:
        arr = condensed_sounds[sound]
        pairs = []

        if(len(arr) == 1):
            pairs.append((arr[0], arr[0] + 1))
        else:
            start = arr[0]
            for i in range(len(arr) - 1):
                if(arr[i+1] > arr[i] + 2):
                    pairs.append((start, arr[i] + 1))
                    start = arr[i+1]
                if(i == len(arr) - 2):
                    pairs.append((start, arr[i+1] + 1))

        all_pairs[sound] = pairs

    return all_pairs
    

def setSounds(id, pairs):
    sounds_DAO.setSounds(id, pairs)

def run_model(id):
    extract_audio(id)
    sounds = run_inference(id)
    pairs = cleanSounds(sounds)
    setSounds(id, pairs)