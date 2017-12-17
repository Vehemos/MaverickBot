from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def response(audio):
	with sr.Microphone() as source:
		print(audio)
	tts = gTTS(text = audio, lang = 'en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3')

def takecommand():
		getcmd = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening to your command...')
			getcmd.pause_threshold = 1
			getcmd.adjust_for_ambient_noise(source, duration = 1)
			audio = getcmd.listen(source)
		try:
			command = getcmd.recognize_google(audio)
			with sr.Microphone() as source:
				print('You said: ' + command)
		except sr.UnknownValueError:
			with sr.Microphone() as source:
				print('UnknownValueError')
				response('Sorry, I did not get that.')
			maverick(takecommand())
		
		return command

def maverick(command):
	
	if 'open Gmail' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.gmail.com'
		webbrowser.get(chrome_path).open(url)
		
	if 'open Facebook' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.fb.com'
		webbrowser.get(chrome_path).open(url)
		
	if 'open Quora' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.quora.com'
		webbrowser.get(chrome_path).open(url)
		
	if 'open Linked In' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.linkedin.com'
		webbrowser.get(chrome_path).open(url)
		
	if 'open Google' in command:
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.google.com'
		webbrowser.get(chrome_path).open(url)
	
	if 'search Google' in command:
		response('What do you want to search?')
		searchTerm = takecommand()
		chrome_path = "/usr/bin/google-chrome"
		url = 'https://www.google.co.in/search?q=' + command
		webbrowser.get(chrome_path).open(url)
		
	if 'send an email' in command:
		response('To whom do you want to send the mail?')
		recipientName = takecommand()
		response('What is their E-Mail Address?')
		recipientID = takecommand()
		response('Please tell me the content of the mail which you weant to send to ' + recipientID)
		content = takecommand()
		
		mail = smtplib.SMTP('smtp.gmail.com', 80)
		mail.ehlo()
		mail.starttls()
		mail.login('E-Mail ID','password')
		mail.sendmail(recipientName, recipientID, content)
		mail.close()
		
		response('Your E-Mail has been sent, check your sent mail for confirmation')
	
	if 'calculate' in command:
			response('What type of calculation do you want to perform?')
			calctype = takecommand()
			if 'Multiplication' in calctype:
				response('What is the multiplier?')
				multiplier = takecommand()
				response('What is the multiplicand?')
				multiplicand = takecommand()
				product = multiplier * multiplicand
				response('The product of your specified numbers is' + product)
			if 'Addition' in calctype:
				response('What is the fist addend?')
				numOne = takecommand()
				response('What is the second addend?')
				numTwo = takecommand()
				sumof = numOne * numTwo
				response('The sum of your specified numbers is' + sumof)
			if 'Subtraction' in calctype:
				response('What is the minuend?')
				minuend = takecommand()
				response('What is the subtrahend?')
				subtrahend = takecommand()
				difference = minuend - subtrahend
				response('The subtraction of your specified numbers is' + difference)
			if 'Division' in calctype:
				response('What is the dividend?')
				dividend = takecommand()
				response('What is the divisor?')
				divisor = takecommand()
				quotient = dividend / divisor
				response('The quotient of your specified numbers is' + quotient)
	else:
		with sr.Microphone() as source:
			response('Sorry, I did not get that. Please try again')
			maverick(takecommand())

response('Initialized and ready!')

while True:
	maverick(takecommand())
