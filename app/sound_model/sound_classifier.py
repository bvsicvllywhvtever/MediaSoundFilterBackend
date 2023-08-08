import os
from IPython import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_io as tfio

from flask import current_app

THRESHOLD = .1
CLIP_SECONDS = 1

#grabbing model
yamnet_model_handle = "https://tfhub.dev/google/yamnet/1"
yamnet_model = hub.load(yamnet_model_handle)

#defining function to extract wav from (wav) filename
@tf.function
def load_wav_16k_mono(filename):
    file_contents = tf.io.read_file(filename)
    wav, sample_rate = tf.audio.decode_wav(
        file_contents,
        desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav

def run_inference(id):

    filename = "sound_model/test_data/" + id + ".wav"

    #grabbing wav of miaow_16, plotting it, and displaying the audio (for use in a jupyter file)
    wav_data = load_wav_16k_mono(filename)

    seconds = round(len(wav_data) / 16000 / CLIP_SECONDS)

    #get class names that YAMNet can recognize
    class_map_path = yamnet_model.class_map_path().numpy().decode('utf-8')
    class_names = list(pd.read_csv(class_map_path)['display_name'])

    sounds = {}

    for i in range(seconds):
        scores, embeddings, spectrogram = yamnet_model(wav_data[i * 16000 * CLIP_SECONDS : (i+1) * 16000 * CLIP_SECONDS])
        class_scores = tf.reduce_mean(scores, axis = 0)

        for j in range(len(class_scores)):

            if(class_scores[j] > THRESHOLD):
                if(j in sounds):
                    sounds[j].append(i)
                else:
                    sounds[j] = [i]

    return sounds