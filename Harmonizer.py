from music21 import *


rock_progressions = {
    'I-IV-V': ['I', 'IV', 'V', 'I'],
    'I-V-vi-IV': ['I', 'V', 'vi', 'IV'],
    'ii-V-I': ['ii', 'V', 'I']
}
midi_file= 'Midi_Recordings/output_basic_pitch.mid'


key_Signature = None


def quantize_melody(melody_stream, rhythmic_grid='16th'):
    # Ensure the melody stream is flat (no nested voices or parts)
    melody_stream = melody_stream.flat

    # Create a new stream to hold the quantized melody
    quantized_melody = stream.Stream()

    # Set the time signature for the quantized melody
    quantized_melody.append(meter.TimeSignature(melody_stream.timeSignature.ratioString))

    # Define the duration of the rhythmic grid (e.g., 16th note)
    if rhythmic_grid == '16th':
        grid_duration = 0.25  # 16th note duration in quarterLength units

    for note_or_rest in melody_stream.notesAndRests:
        if isinstance(note_or_rest, note.Note):
            # Quantize the note duration to the nearest rhythmic grid duration
            quantized_duration = round(note_or_rest.duration.quarterLength / grid_duration) * grid_duration
            new_note = note.Note(note_or_rest.pitch, quarterLength=quantized_duration)
            quantized_melody.append(new_note)
        elif isinstance(note_or_rest, note.Rest):
            # For rests, simply append them with their original duration
            quantized_melody.append(note_or_rest)

    return quantized_melody

def correct_melody_and_write_to_midi(melody_stream,time_signature='4/4'):
    melody_quantized = quantize_melody(melody_stream)
    melody_quantized = melody_stream.flat

    # Create a new stream to hold the melody with measures
    melody_with_bars = stream.Stream()

    # Set the time signature for the melody
    melody_with_bars.append(meter.TimeSignature(time_signature))

    # Variables to track current measure and its accumulated length
    current_measure = stream.Measure()
    current_measure_length = 0

    # Iterate through notes in the melody stream
    for note_or_rest in melody_quantized.notesAndRests:
        # Append notes and rests to current measure
        current_measure.append(note_or_rest)
        current_measure_length += note_or_rest.duration.quarterLength

        # If the current measure reaches the time signature's length (e.g., 4 beats for 4/4)
        if current_measure_length >= meter.TimeSignature(time_signature).barDuration.quarterLength:
            # Add the current measure to the melody with bars stream
            melody_with_bars.append(current_measure)

            # Create a new measure
            current_measure = stream.Measure()
            current_measure_length = 0

    # Add the last measure if it contains notes or rests
    if current_measure_length > 0:
        melody_with_bars.append(current_measure)

    return melody_with_bars

  


def analyze_midi_melody(midi_file_path):
    # Parse the MIDI file
    midi_stream = converter.parse(midi_file_path)

    # Analyze the key of the melody
    key_finder = midi_stream.analyze('key')
    key = key_finder
  
    

    key_pitches = [pitch.pitchClass for pitch in key.getScale().getPitches()]

    # Correct the pitches of the notes in the original melody
    for element in midi_stream.recurse():
        if isinstance(element, note.Note):
            if element.pitch.pitchClass not in key_pitches:
                nearest_pitch = min(key_pitches, key=lambda p: abs(p - element.pitch.pitchClass))
                element.pitch.pitchClass = nearest_pitch

    # Return the corrected melody
    return correct_melody_and_write_to_midi(midi_stream)


# Function to detect the scale degree of a note
def get_scale_degree(note, key_signature):
    scale = key_signature.getScale()
    
    return scale.getScaleDegreeFromPitch(note.pitch)


# Harmonize the melody
def harmonize_melody(melody, key_signature, progressions):
    measures = melody.getElementsByClass('Measure')
    num_measures = len(measures)
    print(f'Number of measures: {num_measures}')
    best_progression = None
    best_match_count = 0

    for progression_name, progression in progressions.items():
        match_count = 0
        for i, measure in enumerate(measures):
            if i < len(progression):
                notes = measure.notes
               
                if notes:
                    first_note = notes[0]
                    print(key_signature)
                    scale_degree = get_scale_degree(first_note, key_signature)
                    
                    chord_symbol = progression[i]
                    rn = roman.RomanNumeral(chord_symbol, key_signature)
                    if scale_degree == rn.scaleDegree:
                        
                        match_count += 1

        if match_count > best_match_count:
            best_match_count = match_count
            best_progression = progression

    # Generate chords for the best matching progression
    harmonized_melody = stream.Part()
    for i, measure in enumerate(measures):
        if i < len(best_progression):
            chord_symbol = best_progression[i]
            rn = roman.RomanNumeral(chord_symbol, key_signature)
            rock_chord = chord.Chord(rn.pitches, quarterLength=4)
            harmonized_melody.append(rock_chord)
        else:
            break

    return harmonized_melody


        

if __name__ == '__main__':

   

    # Store the corrected MIDI file
    
    adjusted_melody = analyze_midi_melody(midi_file)
# You can now work with the adjusted_melody object, e.g., save it as a MIDI file
    adjusted_melody.write('midi', fp="Corrected_Recordings/corrected_midi_file.mid")

    # Harmonize the melody and store the result
    melody_file = converter.parse('Corrected_Recordings/corrected_midi_file.mid')

    melody = melody_file.parts[0]  # Assuming the melody is in the first part
    key_Signature = melody.analyze('key')
    print(f'Key signature: {key_Signature}')
    harmonized_melody = harmonize_melody(melody, key_Signature, rock_progressions)

    # Store the harmonized chords in a separate MIDI file
    harmony_score = stream.Score()
    harmony_score.insert(0, harmonized_melody)

    harmony_midi_file = midi.translate.music21ObjectToMidiFile(harmony_score)
    harmony_midi_file.open('harmony_midi_file.mid', 'wb')
    harmony_midi_file.write()
    harmony_midi_file.close()


