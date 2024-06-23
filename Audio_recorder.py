import sounddevice as sd
import numpy as np
import wave
import time
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH as model
import tensorflow as tf
import wavio as wv
import os
import simpleaudio
import time


sample_rate = 48000  ## Sample rate in Hz
channels = 2         ## Stereo recording
duration = 8         ## Duration of the recording

### Recording locations
recording_folder = "Recordings"
midi_folder = "Midi_Recordings"
corrected_recordings = "Corrected_Recordings"
harmony_files = "Harmony_Files"
filename_template = "recording_{}.wav"
midi_filename_template = "recording_{}.mid"

#### Metronome #####


def play_metronome():

    strong_beat = simpleaudio.WaveObject.from_wave_file(
        'Metronome_Files/strong_beat.wav')
    weak_beat = simpleaudio.WaveObject.from_wave_file(
        'Metronome_Files/weak_beat.wav')
    count = 0
    start_time = time.time()
    end_time = start_time + 6
    while time.time() < end_time:
        count = count + 1
        if count == 1:
            strong_beat.play()
        else:
            weak_beat.play()
        if count == 4:
            count = 0
        remaining_time = int(end_time - time.time())
        print(f"Countdown: {remaining_time} seconds")
        time.sleep(0.5)


def record_audio(duration, filename):

    print("Start recording!")
    myrecording = sd.rec(int(duration * sample_rate),
                         samplerate=sample_rate, channels=channels)
    sd.wait()  ### Wait until recording is finished

    print("Recording stopped, saving file...")
    wv.write(filename, myrecording, sample_rate, sampwidth=4)


def main():

    for file in os.listdir(recording_folder):
        os.remove(os.path.join(recording_folder, file))
    for file in os.listdir(midi_folder):
        os.remove(os.path.join(midi_folder, file))
    for file in os.listdir(corrected_recordings):
        os.remove(os.path.join(corrected_recordings, file))
    for file in os.listdir(harmony_files):
        os.remove(os.path.join(harmony_files, file))

    filename = os.path.join(recording_folder, filename_template.format(1))
    
    print("Prepare to record audio in 6 seconds...")
    play_metronome()

    
    record_audio(duration, filename)

    ##### Convert the recording into MIDI #####
    predict_and_save([filename], midi_folder, True, False, False, False, model, 0.5, 0.3, 200)


if __name__ == "__main__":
    main()
