import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')  
print (rate)                        
engine.setProperty('rate', 108) 
engine.say("Hii ")
engine.runAndWait()
 