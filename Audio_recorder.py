import sounddevice as sd
import numpy as np
import wave
import time
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH as model
import tensorflow as tf
import wavio as wv




sample_rate = 48000  # Sample rate in Hz
channels = 2         # Stereo recording
duration = 8        # Duration will be set by user start/stop input
filename="Recordings/output.wav"



def record_audio(duration, filename):
    print("Start recording!")
    myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait until recording is finished
    print("Recording stopped, saving file...")
   
    wv.write(filename,myrecording, sample_rate, sampwidth=3)
    

def main():
    
    record_audio(duration, filename)
    predict_and_save([filename],'',True,False,False,False,model)


if __name__ == "__main__":
    main()
    