import os
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3

engine = pyttsx3.init()
genai.configure(api_key="AIzaSyDzh_mN_sNF9fkxNm6wQ8s-mv-OQbwsBTM")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": ["hey\n"],
    },
    {
      "role": "model",
      "parts": ["Hey there! What can I do for you today? \n"],
    },
  ]
)

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize speech from the microphone
def recognize_speech_from_mic():
    with sr.Microphone() as source:
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        # Recognize speech using Google Web Speech API
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        response = chat_session.send_message(f"limit to 100 words \n {text}")
        print(response.text)
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('rate', 180)
        engine.say(response.text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    try:
        while True:
            recognize_speech_from_mic()
    except KeyboardInterrupt:
        print("\nConversation ended.")
