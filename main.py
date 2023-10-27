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
