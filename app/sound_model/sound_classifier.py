import os
from IPython import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_io as tfio

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

test_filename = "app/test_data/test.wav"

#grabbing wav of miaow_16, plotting it, and displaying the audio (for use in a jupyter file)
testing_wav_data = load_wav_16k_mono(test_filename)

seconds = round(len(testing_wav_data) / 16000)

#get class names that YAMNet can recognize
class_map_path = yamnet_model.class_map_path().numpy().decode('utf-8')
class_names = list(pd.read_csv(class_map_path)['display_name'])

main_sound_each_second = {}

for i in range(seconds):
    scores, embeddings, spectrogram = yamnet_model(testing_wav_data[i * 16000 : (i+1) * 16000])
    class_scores = tf.reduce_mean(scores, axis = 0)
    top_class = tf.math.argmax(class_scores)
    main_sound_each_second[i] = class_names[top_class]


print(main_sound_each_second)

"""
print(f'The main sound is: {inferred_class}')

class_and_scores = {}
for i in range(0, class_scores.shape[0]):
    class_and_scores[class_names[i]] = class_scores[i]

keys = list(class_and_scores.keys())
values = list(class_and_scores.values())
sorted_index = tf.argsort(values)
class_and_scores = {keys[i]: values[i] for i in sorted_index}

for class_name in class_and_scores:
    print(class_name, ", ", class_and_scores[class_name].numpy().item())

"""