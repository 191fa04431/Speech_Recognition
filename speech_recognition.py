import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize recognizer and TTS engine
listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def hear():
    """Listen for a voice command and return it as text."""
    cmd = ""  # Initialize cmd to an empty string
    try:
        with sr.Microphone() as mic:
            print('Listening...')
            listening.adjust_for_ambient_noise(mic)
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'avinash' in cmd:
                cmd = cmd.replace('avinash', '')
                print(f"Command after removing trigger word: {cmd}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cmd

def run():
    """Main function to run the voice assistant."""
    cmd = hear()
    print(f"Received command: {cmd}")
    # if 'hello' in cmd:
    song = cmd.replace('play', '')
    speak(f'Playing {song}')
    print(f'Playing {song}')
    pk.playonyt(song)  # Play the song on YouTube
    # else:
    # print("No valid command received or 'play' not in command.")

# Call the run function
run()
