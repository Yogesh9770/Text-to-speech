# Import necessary libraries
import speech_recognition as sr
from gtts import gTTS
import os

# Create a speech recognition object
r = sr.Recognizer()

# Use the microphone as a source for audio input
with sr.Microphone() as source:
    print("Speak anything:")
    print("Listening....")
    # Listen to the audio input
    audio = r.listen(source)
    # Recognize speech using Google's speech recognition
    text = r.recognize_google(audio)

# Print the recognized speech
print("You said:", text)

# Split the recognized text into words
result = text.split(" ")

# Count the number of occurrences of the word "India"
count = 0
word = "India"
for i in range(0, len(result)):
    if word == result[i]:
        count += 1

# Print the count of occurrences
print("The number of times " + word + " occurs in the sentence is", count)

# Convert count to string for text-to-speech output
str_count = str(count)

# Prepare text for speech synthesis
my_text = "The number of times " + word + " occurs in the sentence is " + str_count
language = "en"

# Create a gTTS (Google Text-to-Speech) object
output = gTTS(text=my_text, lang=language, slow=False)

# Save the synthesized speech to an audio file
output.save("output.mp3")

# Play the generated audio file
os.system("start output.mp3")
