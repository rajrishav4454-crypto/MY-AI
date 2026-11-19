import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

# Rani ki aawaz (Text-to-Speech) set karna
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def rani_bolo(text):
  print(f"Rani: {text}")
  engine.say(text)
  engine.runAndWait()


def command_suno():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("\nSun rahi hoon... Boliye...")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

  try:
    print("Samajh rahi hoon...")
    query = r.recognize_google(audio, language="hi-IN")
    print(f"Rishav: {query}\n")
    return query.lower()
  except Exception:
    print("Awaaz saaf nahi aayi, phir se boliye...")
    return ""


# Shuruat
rani_bolo("Hello Rishav! Main Rani hoon. Bataiye main aapki kya madad kar sakti hoon?")

while True:
  user_input = command_suno()

  if user_input == "":
    continue

  # 1. Greeting
  if (
      "hello" in user_input
      or "hi" in user_input
      or "namaste" in user_input
  ):
    rani_bolo("Hello Rishav! Kaise hain aap?")

  # 2. Naam poochne par
  elif (
      "tumhara naam" in user_input
      or "your name" in user_input
      or "who are you" in user_input
  ):
    rani_bolo("Mera naam Rani hai, aur mujhe Rishav Raj ne banaya hai.")

  # 3. Samay (Time)
  elif "time" in user_input or "samay" in user_input:
    now = datetime.datetime.now().strftime("%I:%M %p")
    rani_bolo(f"Abhi samay ho raha hai {now}")

  # 4. Tareekh (Date)
  elif "date" in user_input or "tareekh" in user_input:
    today = datetime.datetime.now().strftime("%d %B, %Y")
    rani_bolo(f"Aaj ki tareekh hai {today}")

  # 5. Youtube aur Google kholna
  elif "open youtube" in user_input or "youtube" in user_input:
    rani_bolo("YouTube khol rahi hoon...")
    webbrowser.open("https://www.youtube.com")

  elif "open google" in user_input or "google" in user_input:
    rani_bolo("Google khol rahi hoon...")
    webbrowser.open("https://www.google.com")

  # 6. Band karne ke liye
  elif (
      "bye" in user_input
      or "exit" in user_input
      or "stop" in user_input
  ):
    rani_bolo("Bye Rishav! Phir milenge. Apna khayal rakhna.")
    break