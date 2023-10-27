To create a simple text-to-speech program for your Raspberry Pi 4, you can use the gTTS (Google Text-to-Speech) library, 
which allows you to convert text into speech. You'll also need to install the pygame library to play the generated speech. 
Here's a Python program for text-to-speech on your Raspberry Pi:

1) First, make sure you have Python installed on your Raspberry Pi. If it's not installed, you can typically use python3.
2) Install the required libraries by running the following commands:
```bash
  pip3 install gTTS pygame
```

Create a Python script, e.g., text_to_speech.py, and add the following code:
```python
String firstName;
from gtts import gTTS
import pygame

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

# Function to play the generated speech
def play_speech():
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
    play_speech()
```
Run the script using the command:
```bash
python3 text_to_speech.py
```

The program will ask you to enter the text you want to convert to speech. It will then save the generated speech to an "output.mp3" file and play it using __pygame__.

Make sure your Raspberry Pi is connected to a speaker or headphones to hear the generated speech. You can adjust the language setting in __gTTS__ by changing the __lang__ parameter if you want to use a different language for text-to-speech conversion.
