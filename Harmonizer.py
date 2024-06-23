from music21 import *
import random


#### Dataset of Progressions ####

progressions = {
    'Rock': {
        'major': {
            'I-V-vi-IV': ['I', 'V', 'vi', 'IV'],
            'I-IV-V-I': ['I', 'IV', 'V', 'I'],
            'I-vi-IV-V': ['I', 'vi', 'IV', 'V'],
            'V-IV-I-V': ['V', 'IV', 'I', 'V'],
            'I-iii-vi-IV': ['I', 'iii', 'vi', 'IV'],
            'I-V-IV-I': ['I', 'V', 'IV', 'I'],
            'I-vi-iii-V': ['I', 'vi', 'iii', 'V'],
            'I-V7-IV-I': ['I', 'V7', 'IV', 'I'],
            'I-IVmaj7-V-I': ['I', 'IVmaj7', 'V', 'I'],
            'I-vi7-iii-V': ['I', 'vi7', 'iii', 'V'],
            'I-IV-vi-IV': ['I', 'IV', 'vi', 'IV'],
            'V-IV-vi-V': ['V', 'IV', 'vi', 'V'],
            'I-ii-IV-I': ['I', 'ii', 'IV', 'I'],
            'I-vi-IV-VI': ['I', 'vi', 'IV', 'VI'],
            'I-IV-V-vi': ['I', 'IV', 'V', 'vi']
        },
        'minor': {
            'i-iv-V-i': ['i', 'iv', 'V', 'i'],
            'i-VI-III-VII': ['i', 'VI', 'III', 'VII'],
            'i-VII-VI-V': ['i', 'VII', 'VI', 'V'],
            'i-iv-VI-III': ['i', 'iv', 'VI', 'III'],
            'i-iii-vi-V': ['i', 'iii', 'vi', 'V'],
            'i-V-iv-i': ['i', 'V', 'iv', 'i'],
            'i-vi-III-V': ['i', 'vi', 'III', 'V'],
            'i-iv7-V-i': ['i', 'iv7', 'V', 'i'],
            'i-VI7-III-VII': ['i', 'VI7', 'III', 'VII'],
            'i-VII7-VI-V': ['i', 'VII7', 'VI', 'V'],
            'i-III-VII-VI': ['i', 'III', 'VII', 'VI'],
            'i-iv-ii-V': ['i', 'iv', 'ii', 'V'],
            'i-V-III-iv': ['i', 'V', 'III', 'iv'],
            'i-vi-VII-III': ['i', 'vi', 'VII', 'III'],
            'i-ii-VII-V': ['i', 'ii', 'VII', 'V']
        }
    },
    'Jazz': {
        'major': {
            'ii7-V7-Imaj7-vi7': ['ii7', 'V7', 'Imaj7', 'vi7'],
            'Imaj7-vi7-ii7-V7': ['Imaj7', 'vi7', 'ii7', 'V7'],
            'Imaj7-IVmaj7-iii7-VI7': ['Imaj7', 'IVmaj7', 'iii7', 'VI7'],
            'ii7-V7-Imaj7-IVmaj7': ['ii7', 'V7', 'Imaj7', 'IVmaj7'],
            'Imaj7-vi7-iii7-ii7': ['Imaj7', 'vi7', 'iii7', 'ii7'],
            'Imaj7-IVmaj7-VI7-iii7': ['Imaj7', 'IVmaj7', 'VI7', 'iii7'],
            'ii7-V7-iii7-vi7': ['ii7', 'V7', 'iii7', 'vi7'],
            'Imaj7-vi7-ii7-V7b9': ['Imaj7', 'vi7', 'ii7', 'V7b9'],
            'Imaj7-IVmaj7-iii7-VI7alt': ['Imaj7', 'IVmaj7', 'iii7', 'VI7alt'],
            'ii7-V7-Imaj7-IVmaj7#11': ['ii7', 'V7', 'Imaj7', 'IVmaj7#11'],
            'Imaj7-V7-vi7-ii7': ['Imaj7', 'V7', 'vi7', 'ii7'],
            'ii7-IVmaj7-Imaj7-V7': ['ii7', 'IVmaj7', 'Imaj7', 'V7'],
            'Imaj7-iii7-vi7-ii7': ['Imaj7', 'iii7', 'vi7', 'ii7'],
            'ii7-V7-Imaj7-VI7': ['ii7', 'V7', 'Imaj7', 'VI7'],
            'Imaj7-vi7-IVmaj7-iii7': ['Imaj7', 'vi7', 'IVmaj7', 'iii7']
        },
        'minor': {
            'i7-iv7-V7-i7': ['i7', 'iv7', 'V7', 'i7'],
            'i7-vi7-ii7-V7': ['i7', 'vi7', 'ii7', 'V7'],
            'i7-iv7-bVII7-V7': ['i7', 'iv7', 'bVII7', 'V7'],
            'i7-ii7b5-V7b9-i7': ['i7', 'ii7b5', 'V7b9', 'i7'],
            'i7-vi7-iii7-V7': ['i7', 'vi7', 'iii7', 'V7'],
            'i7-iv7-VI7-iii7': ['i7', 'iv7', 'VI7', 'iii7'],
            'i7-ii7-V7-iv7': ['i7', 'ii7', 'V7', 'iv7'],
            'i7-vi7-ii7-V7#9': ['i7', 'vi7', 'ii7', 'V7#9'],
            'i7-iv7-bVII7-V7alt': ['i7', 'iv7', 'bVII7', 'V7alt'],
            'i7-ii7b5-V7b9-i7#11': ['i7', 'ii7b5', 'V7b9', 'i7#11'],
            'i7-iv7-V7-vi7': ['i7', 'iv7', 'V7', 'vi7'],
            'i7-VI7-ii7-V7': ['i7', 'VI7', 'ii7', 'V7'],
            'i7-vi7-V7-iv7': ['i7', 'vi7', 'V7', 'iv7'],
            'i7-iv7-III7-V7': ['i7', 'iv7', 'III7', 'V7'],
            'i7-V7-iv7-bVII7': ['i7', 'V7', 'iv7', 'bVII7']
        }
    },
    'Pop': {
        'major': {
            'I-V-vi-IV': ['I', 'V', 'vi', 'IV'],
            'vi-IV-I-V': ['vi', 'IV', 'I', 'V'],
            'I-IV-V-I': ['I', 'IV', 'V', 'I'],
            'I-V-vi-iii': ['I', 'V', 'vi', 'iii'],
            'I-iii-vi-IV': ['I', 'iii', 'vi', 'IV'],
            'I-V-IV-I': ['I', 'V', 'IV', 'I'],
            'I-vi-iii-V': ['I', 'vi', 'iii', 'V'],
            'I-V7-IV-I': ['I', 'V7', 'IV', 'I'],
            'I-IVmaj7-V-I': ['I', 'IVmaj7', 'V', 'I'],
            'I-vi7-iii-V': ['I', 'vi7', 'iii', 'V'],
            'I-V-IV-vi': ['I', 'V', 'IV', 'vi'],
            'I-vi-IV-ii': ['I', 'vi', 'IV', 'ii'],
            'I-IV-ii-V': ['I', 'IV', 'ii', 'V'],
            'vi-IV-ii-V': ['vi', 'IV', 'ii', 'V'],
            'I-iii-IV-ii': ['I', 'iii', 'IV', 'ii']
        },
        'minor': {
            'i-VI-III-VII': ['i', 'VI', 'III', 'VII'],
            'i-iv-vi-V': ['i', 'iv', 'vi', 'V'],
            'i-iv-V-i': ['i', 'iv', 'V', 'i'],
            'i-III-VI-VII': ['i', 'III', 'VI', 'VII'],
            'i-vi-III-V': ['i', 'vi', 'III', 'V'],
            'i-iv-VI-V': ['i', 'iv', 'VI', 'V'],
            'i-iii-vi-V': ['i', 'iii', 'vi', 'V'],
            'i-VI7-III-VII': ['i', 'VI7', 'III', 'VII'],
            'i-iv7-V-i': ['i', 'iv7', 'V', 'i'],
            'i-VII7-VI-V': ['i', 'VII7', 'VI', 'V'],
            'i-ii7-vi-V': ['i', 'ii7', 'vi', 'V'],
            'i-vi-ii7-V': ['i', 'vi', 'ii7', 'V'],
            'i-iv7-vi7-V': ['i', 'iv7', 'vi7', 'V'],
            'i-iii-vi-ii': ['i', 'iii', 'vi', 'ii'],
            'i-V-iv7-VII': ['i', 'V', 'iv7', 'VII']
        }
    },
    'Classical': {
        'major': {
            'I-IV-V-I': ['I', 'IV', 'V', 'I'],
            'ii6-V-I-I': ['ii6', 'V', 'I', 'I'],
            'I-vi-ii-V': ['I', 'vi', 'ii', 'V'],
            'I-IV-V-viio': ['I', 'IV', 'V', 'viio'],
            'I-iii-vi-IV': ['I', 'iii', 'vi', 'IV'],
            'I-V-IV-I': ['I', 'V', 'IV', 'I'],
            'I-vi-iii-V': ['I', 'vi', 'iii', 'V'],
            'I-IVmaj7-V-I': ['I', 'IVmaj7', 'V', 'I'],
            'I-vi7-iii-V': ['I', 'vi7', 'iii', 'V'],
            'I-V7-IV-I': ['I', 'V7', 'IV', 'I'],
            'I-ii-V-I': ['I', 'ii', 'V', 'I'],
            'IV-I-V-vi': ['IV', 'I', 'V', 'vi'],
            'I-vi-IV-V': ['I', 'vi', 'IV', 'V'],
            'I-V-vi-ii': ['I', 'V', 'vi', 'ii'],
            'IV-V-I-ii': ['IV', 'V', 'I', 'ii']
        },
        'minor': {
            'i-iv-V-i': ['i', 'iv', 'V', 'i'],
            'i-VII-VI-V': ['i', 'VII', 'VI', 'V'],
            'i-iv-VI-V': ['i', 'iv', 'VI', 'V'],
            'i-iv-v-i': ['i', 'iv', 'v', 'i'],
            'i-iii-vi-V': ['i', 'iii', 'vi', 'V'],
            'i-V-iv-i': ['i', 'V', 'iv', 'i'],
            'i-vi-III-V': ['i', 'vi', 'III', 'V'],
            'i-iv7-V-i': ['i', 'iv7', 'V', 'i'],
            'i-VII7-VI-V': ['i', 'VII7', 'VI', 'V'],
            'i-iii-vi-V7': ['i', 'iii', 'vi', 'V7'],
            'i-V-iv-VI': ['i', 'V', 'iv', 'VI'],
            'i-VII-V-VI': ['i', 'VII', 'V', 'VI'],
            'i-iv-VII-vi': ['i', 'iv', 'VII', 'vi'],
            'i-ii-vi-V': ['i', 'ii', 'vi', 'V'],
            'i-iv-vi-V7': ['i', 'iv', 'vi', 'V7']
        }
    }
}

#### Dataset of Rhythms ####
#### Rhythms to be used in the Harmony blocks #####

rhythms = {
    'Rock': [
        [4],  ## Whole note
        [2, 2],  ## Two half notes
        [1, 1, 1, 1],  ## Four quarter notes
        [1.5, 0.5, 1, 1]  ## Dotted quarter, eighth, two quarter notes
    ],
    'Jazz': [
        [1.5, 0.5, 1, 1],  ## Swing rhythm
        [2, 2],  ## Two half notes
        [1, 1, 1, 1],  ## Four quarter notes
        [3, 1]  ## Dotted half, quarter
    ],
    'Pop': [
        [4],  ## Whole note
        [2, 2],  ## Two half notes
        [1, 1, 1, 1],  ## Four quarter notes
        [1, 1.5, 1.5]  ## Quarter, dotted quarter, dotted quarter
    ],
    'Classical': [
        [4],  ## Whole note
        [2, 2],  ## Two half notes
        [1, 1, 1, 1],  ## Four quarter notes
        [3, 1]  ## Dotted half, quarter
    ]
}

### First Quantization Step, align the melody of the original recording to the grid of 16th  ###


def quantize_melody(melody_stream, rhythmic_grid='16th'):

    melody_stream = melody_stream.flat
    quantized_melody = stream.Stream()

    if melody_stream.timeSignature is not None:
        quantized_melody.append(meter.TimeSignature(melody_stream.timeSignature.ratioString))

    grid_duration_map = {
        '16th': 0.25,  ## 16th note duration in quarterLength units
        '8th': 0.5,    ## 8th note duration in quarterLength units
        'quarter': 1.0  ## Quarter note duration in quarterLength units
    }

    if rhythmic_grid not in grid_duration_map:
        raise ValueError("Invalid rhythmic grid specified.")

    grid_duration = grid_duration_map[rhythmic_grid]

    for note_or_rest in melody_stream.notesAndRests:
        if isinstance(note_or_rest, note.Note):
            #### Quantize the note duration to the nearest rhythmic grid duration
            quantized_duration = round(note_or_rest.duration.quarterLength / grid_duration) * grid_duration
            new_note = note.Note(note_or_rest.pitch, quarterLength=quantized_duration)
            quantized_melody.append(new_note)
        elif isinstance(note_or_rest, note.Rest):

            quantized_melody.append(note_or_rest)

    ### Make the melody still fit in 4 bars
    total_duration = sum(note_or_rest.quarterLength for note_or_rest in quantized_melody.notesAndRests)
    four_bars_duration = 4 * melody_stream.timeSignature.barDuration.quarterLength
    final_quantized_melody = stream.Stream()
    current_duration = 0
    for element in quantized_melody.notesAndRests:
        if current_duration + element.quarterLength <= four_bars_duration:
            final_quantized_melody.append(element)
            current_duration += element.quarterLength
        else:
            break

    if current_duration < four_bars_duration:
        final_quantized_melody.append(note.Rest(quarterLength=four_bars_duration - current_duration))

    return final_quantized_melody


### Function to make sure the new melody still fits in 4 bars ###

def correct_melody(melody_stream, time_signature='4/4'):
    melody_quantized = quantize_melody(melody_stream)
    melody_quantized = melody_quantized.flat
    melody_with_bars = stream.Stream()
    melody_with_bars.append(meter.TimeSignature(time_signature))

    # Variables to track current measure and its accumulated length
    current_measure = stream.Measure()
    current_measure_length = 0

    for note_or_rest in melody_quantized.notesAndRests:

        current_measure.append(note_or_rest)
        current_measure_length += note_or_rest.duration.quarterLength

        # If the current measure reaches the time signature's length (4/4)
        if current_measure_length >= meter.TimeSignature(time_signature).barDuration.quarterLength:
            melody_with_bars.append(current_measure)
            current_measure = stream.Measure()
            current_measure_length = 0

    if current_measure_length > 0:
        melody_with_bars.append(current_measure)

    return melody_with_bars

### Tune notes to the right pitch in A440 Hz Tuning ###

def pitch_correction(original_pitch):
    corrected_pitch = pitch.Pitch()
    corrected_pitch.midi = round(original_pitch.midi)
    return corrected_pitch

### Function to correct the scale of the melody, ensuring every note is on the scale ###

def scale_correction(midi_file_path):
    midi_stream = converter.parse(midi_file_path)
    key = midi_stream.analyze('key')
    scale_pitches = [pitch.pitchClass for pitch in key.getScale().getPitches()]

    ### Correct the pitches of the notes in the original melody
    for element in midi_stream.recurse():
        if isinstance(element, note.Note):
            tuned_pitch = pitch_correction(element.pitch)
            element.pitch = tuned_pitch
            closest_pitch = min(scale_pitches, key=lambda p: abs(p - element.pitch.pitchClass))
            element.pitch.pitchClass = closest_pitch

    return correct_melody(midi_stream)


#### Function to detect the scale degree of a note ###
def get_scale_degree(note, key_signature):
    scale = key_signature.getScale()
    return scale.getScaleDegreeFromPitch(note.pitch)

### Function to find a fitting chord for a given note ###

def find_fitting_chord(note, key_signature, genre, progressions):
    relevant_progressions = progressions[genre][key_signature.mode]
    fitting_chords = []

    for progression in relevant_progressions.values():
        for chord_symbol in progression:
            rn = roman.RomanNumeral(chord_symbol, key_signature)
            if note.pitch in rn.pitches or get_scale_degree(note, key_signature) == rn.scaleDegree:
                fitting_chords.append(rn)

    if fitting_chords:
        return random.choice(fitting_chords)
    return None

### Function that harmonizes a melody based on a given genre, key signature ###

def harmonize_melody(melody, key_signature, genre, progressions, rhythms):
    measures = melody.getElementsByClass('Measure')

    best_progression = None
    best_match_count = 0

    if key_signature.mode == 'major':
        relevant_progressions = progressions[genre]['major']
    elif key_signature.mode == 'minor':
        relevant_progressions = progressions[genre]['minor']
    else:
        raise ValueError("Key signature mode not recognized.")

    ### List to store progressions with the highest match count
    best_progressions = []

    for progression_name, progression in relevant_progressions.items():
        match_count = 0
        for i, measure in enumerate(measures):
            if i < len(progression):
                notes = measure.notes
                if notes:
                    first_note = notes[0]
                    scale_degree = get_scale_degree(first_note, key_signature)
                    chord_symbol = progression[i]
                    rn = roman.RomanNumeral(chord_symbol, key_signature)

                    if scale_degree == rn.scaleDegree:  ### If note corresponds to the scale degree of the chord
                        match_count += 2
                    elif first_note.pitch in rn.pitches:  ### If note is in the chord
                        match_count += 1

        if match_count > best_match_count:

            best_match_count = match_count
            best_progressions = [progression_name]
        elif match_count == best_match_count:
            ### If multiple progressions have the same match count, add them to the list
            best_progressions.append(progression_name)

    if not best_progressions:
        raise ValueError("No suitable chord progression found.")

    best_progression = random.choice(best_progressions)
    harmonized_melody = stream.Part()

    for i, measure in enumerate(measures):
        if i < len(relevant_progressions[best_progression]):
            chord_symbol = relevant_progressions[best_progression][i]
            rn = roman.RomanNumeral(chord_symbol, key_signature)

            for note_or_rest in measure.notesAndRests:
                if isinstance(note_or_rest, note.Note):
                    if note_or_rest.pitch not in rn.pitches and get_scale_degree(note_or_rest, key_signature) != rn.scaleDegree:
                        if random.random() < 0.2:  ### Replacing one chord of the progression with a random chord that fits
                            fitting_chord = find_fitting_chord(note_or_rest, key_signature, genre, progressions)
                            if fitting_chord:
                                rn = fitting_chord

            ### Apply a rhythmic pattern to the chord that has been chosen randomly
            rhythm_pattern = random.choice(rhythms[genre])
            for duration in rhythm_pattern:
                harmonized_melody.append(chord.Chord(rn.pitches, quarterLength=duration))

        else:
            break

    return harmonized_melody

### Function to readjust the melody to the harmony, to avoid clashing with the harmony ###

def readjust_melody(melody_stream, harmony_stream, rhythmic_grid='8th'):

    melody_stream = melody_stream.flat
    harmony_stream = harmony_stream.flat
    readjusted_melody = stream.Stream()

    if melody_stream.timeSignature is not None:
        readjusted_melody.append(meter.TimeSignature(melody_stream.timeSignature.ratioString))

    grid_duration_map = {
        '16th': 0.25,    ## 16th note duration in quarterLength units
        '8th': 0.5,      ## 8th note duration in quarterLength units
        'quarter': 1.0,  ## Quarter note duration in quarterLength units

    }

    if rhythmic_grid not in grid_duration_map:
        raise ValueError("Invalid rhythmic grid specified.")

    grid_duration = grid_duration_map[rhythmic_grid]

    harmony_chords = harmony_stream.getElementsByClass('Chord')

    ### Iterate through the melody stream and adjust rhythm to harmony
    melody_notes_and_rests = list(melody_stream.notesAndRests)
    harmony_index = 0

    i = 0
    while i < len(melody_notes_and_rests):
        melody_element = melody_notes_and_rests[i]

        if isinstance(melody_element, note.Note):

            combined_quarter_length = melody_element.quarterLength

            #### Find sequence of notes to be combined
            j = i + 1
            while (j < len(melody_notes_and_rests) and isinstance(melody_notes_and_rests[j], note.Note) and melody_notes_and_rests[j].offset - melody_element.offset < grid_duration):
                combined_quarter_length += melody_notes_and_rests[j].quarterLength
                j += 1

            ### Append the combined note with adjusted offset
            if melody_element.offset >= harmony_chords[harmony_index].offset:
                new_offset = round(melody_element.offset / grid_duration) * grid_duration
                new_offset = max(new_offset, harmony_chords[harmony_index].offset)

                harmony_pitch = harmony_chords[harmony_index].root()
                melody_pitch = melody_element.pitch
                if melody_pitch < harmony_pitch:
                    melody_pitch.octave += 1  ### Ensuring melody is higher in octave than harmony
                ### If combined duration is 0.5 or smaller (8th note or smaller)
                if combined_quarter_length <= 0.5:
                    if readjusted_melody and isinstance(readjusted_melody[-1], note.Note):
                        readjusted_melody[-1].quarterLength += combined_quarter_length
                else:
                    readjusted_melody.append(note.Note(melody_element.pitch, quarterLength=combined_quarter_length, offset=new_offset))
            else:
                readjusted_melody.append(note.Note(melody_element.pitch, quarterLength=combined_quarter_length, offset=melody_element.offset))

            i = j

        elif isinstance(melody_element, note.Rest):

            readjusted_melody.append(note.Rest(quarterLength=melody_element.quarterLength, offset=melody_element.offset))
            i += 1

        else:

            readjusted_melody.append(melody_element)
            i += 1

    ### Iterate through the melody stream and adjust rhythm to harmony
    melody_nested = readjusted_melody
    harmony_index = 0
    final_melody = stream.Stream()

    for melody_element in melody_nested:
        if isinstance(melody_element, note.Note):
            melody_offset = melody_element.offset
            melody_pitch = melody_element.pitch

            ### Find the corresponding chord in harmony
            while harmony_index < len(harmony_chords) - 1 and harmony_chords[harmony_index + 1].offset <= melody_offset:
                harmony_index += 1

            current_chord = harmony_chords[harmony_index]
            current_chord_offset = current_chord.offset

            next_chord_offset = current_chord_offset
            if harmony_index < len(harmony_chords) - 1:
                next_chord_offset = harmony_chords[harmony_index + 1].offset

            ### Determine the adjusted offset for the melody note
            if melody_offset >= current_chord_offset:
                if melody_offset > next_chord_offset - grid_duration:
                    #### If melody_offset is too close to the next chord, align with the next chord
                    new_offset = next_chord_offset
                else:
                    ### Otherwise, quantize to the nearest grid_duration within the chord bounds
                    new_offset = round(melody_offset / grid_duration) * grid_duration
                    new_offset = max(new_offset, current_chord_offset)

                final_melody.append(note.Note(melody_pitch, quarterLength=melody_element.quarterLength, offset=new_offset))
            else:
                final_melody.append(note.Note(melody_pitch, quarterLength=melody_element.quarterLength, offset=melody_offset))

        elif isinstance(melody_element, note.Rest):
            final_melody.append(note.Rest(quarterLength=melody_element.quarterLength, offset=melody_element.offset))

    ### Making sure duration of the final melody is the same as the original melody
    if final_melody.duration.quarterLength < melody_stream.duration.quarterLength:
        last_element = readjusted_melody[-1]
        if isinstance(last_element, note.Note) or isinstance(last_element, note.Rest):
            last_element.quarterLength += melody_stream.duration.quarterLength - final_melody.duration.quarterLength

    return final_melody

### Functions to apply fade effects to the melody and harmony streams ###

def apply_fade_effects(melody_stream, harmony_stream, fade_in_duration=0.4, fade_out_duration=0.4):

    melody_stream = melody_stream.flat
    harmony_stream = harmony_stream.flat

    #### Applying fade effects to melody stream
    for m_note in melody_stream.getElementsByClass('Note'):
        apply_fade_to_note(m_note, fade_in_duration, fade_out_duration)

    #### Applying fade effects to harmony stream
    for h_note in harmony_stream.getElementsByClass(['Note', 'Chord']):
        if isinstance(h_note, note.Note):
            apply_fade_to_note(h_note, fade_in_duration, fade_out_duration)
        elif isinstance(h_note, chord.Chord):
            for chord_note in h_note:
                apply_fade_to_note(chord_note, fade_in_duration, fade_out_duration)


def apply_fade_to_note(note_obj, fade_in_duration, fade_out_duration):
    start_velocity = 40
    end_velocity = 80

    start_offset = note_obj.offset
    end_offset = start_offset + note_obj.quarterLength

    fade_in_start = start_offset
    fade_in_end = start_offset + fade_in_duration
    fade_out_start = end_offset - fade_out_duration
    fade_out_end = end_offset

    if start_offset <= fade_in_end:
        fade_in_ratio = min(1.0, (fade_in_end - start_offset) / fade_in_duration)
        fade_in_velocity = int(start_velocity + fade_in_ratio * (end_velocity - start_velocity))
        note_obj.volume.velocity = fade_in_velocity

    if fade_out_start >= start_offset:
        fade_out_ratio = min(1.0, (end_offset - fade_out_start) / fade_out_duration)
        fade_out_velocity = int(end_velocity - fade_out_ratio * (end_velocity - start_velocity))
        note_obj.volume.velocity = fade_out_velocity


def main(midi_file):

    genre_options = ['Rock', 'Jazz', 'Pop', 'Classical']
    print("Select a genre:")
    for idx, genre in enumerate(genre_options, 1):
        print(f"{idx}. {genre}")

    selected_genre_index = int(
        input("Enter the number corresponding to your choice: ")) - 1

    if selected_genre_index < 0 or selected_genre_index >= len(genre_options):
        print("Invalid selection. Exiting.")
        return

    genre = genre_options[selected_genre_index]

    adjusted_melody = scale_correction(midi_file)

    melody = adjusted_melody
    key_signature = melody.analyze('key')

    harmonized = harmonize_melody(melody, key_signature, genre, progressions, rhythms)
    harmony_score = stream.Score()
    harmony_score.insert(0, harmonized)

    new_melody_stream = readjust_melody(melody, harmony_score)

    apply_fade_effects(new_melody_stream, harmony_score)

    new_melody_stream.write('midi', fp="Corrected_Recordings/corrected_midi_file.mid")
    harmony_score.write('midi', fp="Harmony_Files/harmony_midi_file.mid")


if __name__ == '__main__':
    main('Midi_Recordings/recording_1_basic_pitch.mid')
