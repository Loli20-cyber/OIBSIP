
import  pyttsx3 #this is the voice guy 
import chatgpt  #to get definition or answers


luella=pyttsx3.init()
voice=luella.getProperty('voice')

luella.setProperty('voice',voice[0].id)

searchforsomething=input("search for:")#ask the user to search for something 
answer=chatgpt.summary(searchforsomething,sentences=1)

print(answer)#to print out answ2er in consle
luella.say(answer)#microphone must tell you the answer
luella.runAndWait()