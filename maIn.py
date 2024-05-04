"""
where to find models to use with the projects

https://alphacephei.com/vosk/models
"""

import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
# open audio file
wf = wave.open("/Users/Geiousta/Downloads/ASSIGNMENT1.wav", "rb")

# Initialize model
# You can find several models at https://alphacephei.com/vosk/models
# I decided to go with the largest vosk-model-en-us-0.22
model = Model("/Users/Geiousta/Downloads/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, wf.getframerate())

# To store our results
transcription = []

#rec.SetWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Convert json output to dict
        result_dict = json.loads(rec.Result())
        # Extract text values and append them to transcription list
        transcription.append(result_dict.get("text", ""))

# Get final bits of audio and flush the pipeline
final_result = json.loads(rec.FinalResult())
transcription.append(final_result.get("text", ""))

# merge or join all list elements to one big string
transcription_text = ' '.join(transcription)
#print(transcription_text)

f= open("transcription1.txt","w+")
f.write(transcription_text)
f.close()