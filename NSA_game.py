from sys import exit

def check(input):
	input = input.lower()
	if input == "y":
		return True
	if input == "yes":
		return True
	return False

def submit_FOIA():
	print "So you want to submit a FOIA request to the NSA on this company. Do you know their full company name and address?" 
	next = raw_input("y/n> ")
	if check(next) == True:
		print "Go ahead and submit your FOIA!"
		FOIA_response()
		 	
	elif check(next) == False:
		print "You submit the FOIA and get a letter back saying they cannot find records from a 'key word' search!"
		print "Would you like to appeal?" 
		appeal = raw_input("y/n> ")
			
		if check(appeal) == True:
		    print "You find the company name and address and write your appeal."
		    submit_appeal()
		    	
		elif check(appeal) == False:
			print "Congratulations, you have turned into a newt."
			exit(0)

def FOIA_response():
	print "Are you a member of the media?" 
	next = raw_input("y/n> ")
	if check(next) == True:
		print "You receive two 20 page contracts with the amounts and/or item descriptions redacted. Would you like to appeal?"
		appeal = raw_input("y/n> ")
			
		if check(appeal) == True:
		    submit_appeal()
		    	
		elif check(appeal) == False:
			print "Congratulations, you know the NSA contracts with this evil company but you may never know the details of what they've done." 
			print "I suppose you must enjoy a good mystery."
			exit(0) 
			
	elif check(next) == False:	
		print "You receive a letter back stating that you are an 'all other requester.'" 
		print "The NSA wants a commitment from you to pay for any searches done in excess of 2 hours. Do you want to pay?"
		pay = raw_input("y/n> ")
		if check(pay) == True:
			print "You respond saying that you'll pay up to 100 coconuts for additional search efforts."
			print "You wait patiently and send follow up letters."
			print "After 4 years you receive one twenty page contract with the amounts and/or item descriptions redacted. Would you like to appeal?"
			appeal = raw_input("y/n> ")
			if check(appeal) == True:
				submit_appeal()
			 
			elif check(appeal) == False:
				print "Seriously, you waited that long and you don't want to appeal the redactions?"  
				print "It is pitch black. You are likely to be eaten by a grue." 				
				exit(0)
					
		if check(pay) == False:
			print "Would you like to appeal the determination that you're not a media requester?"
			appeal = raw_input("y/n> ")
			if check(appeal) == True:
				submit_appeal()
			
			elif check(appeal) == False:
				print "No pay? No appeal? No candy for you. Why did you send a FOIA request, anyway?" 
		    	print "You give up too easy. You die unknown and unloved."

def submit_appeal():
	print "You submit your appeal. You wait. And you wait. And you wait. You die waiting."  
	print "You are posthumously given the Pulitzer Prize when the contracts come in after 10 years."
	print "The contracts reveal a plot to replace the President with a mindless automaton developed by Boston Dynamics."
	print "None of this matters to you because you are dead."
	exit(0)
	
print "You're researching a technology company that's been doing some pretty evil stuff:"
print "Are they a likely NSA contractor?"
next = raw_input("y/n> ")
if check(next) == True:
	submit_FOIA()
			
elif check(next) == False:		
	print "You continue your research and try to find other agencies they might do business with."
	exit(0)
	
	
