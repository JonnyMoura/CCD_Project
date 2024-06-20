from music21 import *
import random


# Major and Minor Progressions
major_progressions = {
    'ii-V-I': ['ii', 'V', 'I', 'IV'],
    'I-V-vi-IV': ['I', 'V', 'vi', 'IV'],
    'I-IV-V': ['I', 'IV', 'V', 'I'],
    'I-vi-IV-V': ['I', 'vi', 'IV', 'V'],
    'I-V-IV-I': ['I', 'V', 'IV', 'I'],
    'vi-IV-I-V': ['vi', 'IV', 'I', 'V'],
    'I-IV-I-V': ['I', 'IV', 'I', 'V'],
    'V-I-vi-IV': ['V', 'I', 'vi', 'IV'],
    'I-V-iii-vi': ['I', 'V', 'iii', 'vi'],
    'I-IV-vi-V': ['I', 'IV', 'vi', 'V'],
    'V-I-IV-vi': ['V', 'I', 'IV', 'vi']
}

minor_progressions = {
    'i-iv-V': ['i', 'iv', 'V', 'i'],
    'i-V-vi-iv': ['i', 'V', 'vi', 'iv'],
    'i-iv-vi-V': ['i', 'iv', 'vi', 'V'],
    'V-i-iv-vi': ['V', 'i', 'iv', 'vi'],
    'vi-iv-i-V': ['vi', 'iv', 'i', 'V']
}
midi_file= 'Midi_Recordings/output_basic_pitch.mid'


key_Signature = None


def quantize_melody(melody_stream, rhythmic_grid='16th'):
    # Ensure the melody stream is flat (no nested voices or parts)
    melody_stream = melody_stream.flat

    # Create a new stream to hold the quantized melody
    quantized_melody = stream.Stream()

    # Set the time signature for the quantized melody
    if melody_stream.timeSignature is not None:
        quantized_melody.append(meter.TimeSignature(melody_stream.timeSignature.ratioString))

    # Define the duration of the rhythmic grid
    grid_duration_map = {
        '16th': 0.25,  # 16th note duration in quarterLength units
        '8th': 0.5,    # 8th note duration in quarterLength units
        'quarter': 1.0 # Quarter note duration in quarterLength units
    }

    if rhythmic_grid not in grid_duration_map:
        raise ValueError("Invalid rhythmic grid specified.")

    grid_duration = grid_duration_map[rhythmic_grid]

    for note_or_rest in melody_stream.notesAndRests:
        if isinstance(note_or_rest, note.Note):
            # Quantize the note duration to the nearest rhythmic grid duration
            quantized_duration = round(note_or_rest.duration.quarterLength / grid_duration) * grid_duration

            # Extend the duration slightly to make it smoother
            extended_duration = quantized_duration + grid_duration * 0.1
            new_note = note.Note(note_or_rest.pitch, quarterLength=extended_duration)
            quantized_melody.append(new_note)
        elif isinstance(note_or_rest, note.Rest):
            # For rests, simply append them with their original duration
            quantized_melody.append(note_or_rest)

    # Merge consecutive notes that are within a small threshold of each other
    merged_melody = stream.Stream()
    for n in quantized_melody.notes:
        if merged_melody.notes:
            last_note = merged_melody.notes[-1]
            if n.pitch == last_note.pitch and n.offset - last_note.offset <= grid_duration * 0.5:
                last_note.quarterLength += n.quarterLength
            else:
                merged_melody.append(n)
        else:
            merged_melody.append(n)

    return merged_melody

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
  
    # Get the scale pitches
    scale_pitches = [pitch.pitchClass for pitch in key.getScale().getPitches()]

    # Correct the pitches of the notes in the original melody
    for element in midi_stream.recurse():
        if isinstance(element, note.Note):
            # Find the closest pitch in the scale
            closest_pitch = min(scale_pitches, key=lambda p: abs(p - element.pitch.pitchClass))
            # Calculate the octave adjustment
            octave_adjustment = (element.pitch.octave - 4) + (closest_pitch // 12 - element.pitch.pitchClass // 12)
            # Adjust the pitch
            element.pitch.pitchClass = closest_pitch
            element.pitch.octave = 4 + octave_adjustment

    # Return the corrected melody
    return correct_melody_and_write_to_midi(midi_stream)


# Function to detect the scale degree of a note
def get_scale_degree(note, key_signature):
    scale = key_signature.getScale()
    
    return scale.getScaleDegreeFromPitch(note.pitch)


def harmonize_melody(melody, key_signature, major_progressions, minor_progressions):
    measures = melody.getElementsByClass('Measure')
    num_measures = len(measures)
    print(f'Number of measures: {num_measures}')
    best_progression = None
    best_match_count = 0

    # Choose the appropriate set of progressions
    if key_signature.mode == 'major':
        relevant_progressions = major_progressions
    elif key_signature.mode == 'minor':
        relevant_progressions = minor_progressions
    else:
        raise ValueError("Key signature mode not recognized.")

    # List to store progressions with the highest match count
    best_progressions = []

    for progression_name, progression in relevant_progressions.items():
        print(f'Checking progression: {progression_name}')
        match_count = 0
        for i, measure in enumerate(measures):
            if i < len(progression):
                notes = measure.notes
                if notes:
                    first_note = notes[0]
                    scale_degree = get_scale_degree(first_note, key_signature)
                    print(f' (Scale degree: {scale_degree})')
                    chord_symbol = progression[i]
                    rn = roman.RomanNumeral(chord_symbol, key_signature)

                    if scale_degree == rn.scaleDegree:
                        match_count += 2
                    elif first_note.pitch in rn.pitches:
                        match_count += 1
                print(f'  {chord_symbol}: {rn.scaleDegree} ')
        print(f'  Match count: {match_count}')

        if match_count > best_match_count:
            # If a new best progression is found, update the best_progressions list
            best_match_count = match_count
            best_progressions = [progression_name]
        elif match_count == best_match_count:
            # If multiple progressions have the same match count, add them to the list
            best_progressions.append(progression_name)

    if not best_progressions:
        raise ValueError("No suitable chord progression found.")
    print(f'Best progressions: {best_progressions}')
    # Randomly choose one of the best progressions
    best_progression = random.choice(best_progressions)

    print(f'Best progression: {best_progression}')
    print(f'Match count: {best_match_count}')

    harmonized_melody = stream.Part()
    for i, measure in enumerate(measures):
        if i < len(relevant_progressions[best_progression]):
            chord_symbol = relevant_progressions[best_progression][i]
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
    harmonized_melody = harmonize_melody(melody, key_Signature, major_progressions, minor_progressions)

    # Store the harmonized chords in a separate MIDI file
    harmony_score = stream.Score()
    harmony_score.insert(0, harmonized_melody)

    harmony_midi_file = midi.translate.music21ObjectToMidiFile(harmony_score)
    harmony_midi_file.open('harmony_midi_file.mid', 'wb')
    harmony_midi_file.write()
    harmony_midi_file.close()


