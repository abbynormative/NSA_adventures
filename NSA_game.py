from sys import exit
import random

def check(input):
	input = input.lower()
	if input == "y":
		return True
	if input == "yes":
		return True
	return False

def submit_FOIA():
	print "So you want to submit a FOIA request to the NSA on this company." 
	print "Do you know their full company name and address?" 
	next = raw_input("y/n> ")
	if check(next) == True:
		print "Go ahead and submit your FOIA!"
		FOIA_response()

	elif check(next) == False:
		print "You submit the FOIA and get a letter back from the NSA."
		print "They say they cannot find records from a 'key word' search!"
		print "Would you like to appeal?"
		appeal = raw_input("y/n> ")
		if check(appeal) == True:
			print "'Key word' search - my ass."
			print "You wanted them find files on the company, not a key word."
			print "You find the full company name and address and write your appeal."
			submit_appeal()

		elif check(appeal) == False:
			print "Congratulations, you have turned into a newt."
			exit(0)

def FOIA_response():
	print "Are you a member of the media?" 
	next = raw_input("y/n> ")
	if check(next) == True:
		print "You receive two 20 page contracts."
		print "The amounts and item descriptions are redacted."
		print "Would you like to appeal the redactions?"
		appeal = raw_input("y/n> ")
			
		if check(appeal) == True:
			submit_appeal()

		elif check(appeal) == False:
			print "Congratulations, you know the NSA contracts with this evil company..."
			print "But you may never know the details of what they've done." 
			print "I suppose you must enjoy a good mystery."
			exit(0) 

	elif check(next) == False:
		x = random.randint(1, 10)
		if x < 8:
			print "You receive a letter back stating that you are an 'all other requester.'"
			print "The NSA wants a commitment from you to pay for searches done in excess of 2 hours."
			print "Do you want to pay?"
			pay = raw_input("y/n> ")
			if check(pay) == True:
				print "You respond saying that you'll pay up to 100 coconuts."
				print "You wait patiently and send follow up letters."
				print "After 4 years you receive one twenty page contract."
				print "The amounts and item descriptions are redacted."
				print "Would you like to appeal the redactions?"
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
		else:
			print "After ten days you receive a ten page contract."
			print "You tweet out a link to the contract."
			print "Within 3 hours you've gotten media coverage from around the world."
			print "The CEO of this company who contracted with the NSA starts taunting you on Twitter."
			print "He impishly suggests you send out FOIAs on his competition."
			print "You had planned on sending out more FOIAs anyway. Do you follow his leads?"
			next = raw_input("y/n> ")
			if check(next) == True:
				print "YOLO. You decide to send out a FOIA of each of the CEO's leads."
				submit_FOIA()
			if check(next) == False:
				print "It creeps you out that the CEO of this company is tweeting at you."
				print "You don't want any trouble."
				print "This experience has scared you and you never send out a FOIA again."
				print "On the one hand, you live out your days fairly content."
				print "On the other hand, you always wonder what would have happened..."
				print "If only you had taken a chance and continued your investigations."
				exit(0)
def submit_appeal():
	x = random.randint(1, 10)
	if x < 5:
		print """You submit your appeal. You wait. And you wait. And wait. You die waiting.  
You are posthumously given the Pulitzer Prize when the contracts come in after 10 years.
The contracts reveal a plot to replace the President with a mindless automaton 
developed by Boston Dynamics. None of this matters to you because you are dead."""
		exit(0)

	else:
		print """You submit your appeal. You wait. And you wait. And you wait.
You write followup letters once a month for three years.
Three years and 8 days after you submitted your appeal you receive a denial letter.
The denial states that the information you seek would harm national security.
Would you like to sue the NSA to pursue what you requested?"""
		next = raw_input("y/n> ")

		if check(next) == True:
			print """You pitch your FOIA appeal case to the ACLU.
They take it on the grounds that the NSA should be more open about their activities.
Unfortunately the district court disagrees and finds in favor of the NSA.
Do you want to appeal your court case?"""
			sue = raw_input("y/n> ")
			
			if check(sue) == True:	
				print """The ACLU files an appeal for your court case.
The appeals court hands you a VICTORY!
Unfortunately the DOJ appeals your case to the Supreme Court.
You testify before the Supreme Court about open access to gov't information.
And the evils of mass surveillance, and contractor abuse.
You are an instant media star. You lose the case, but become a famous journalist.
You go on to discover additional contracts that reveal a plot...
to replace the President with a mindless automaton developed by Boston Dynamics.
You are eventually killed in a mysterious car crash...
But not before you change the world.
		\('v')/"""
				exit(0)	
				
			if check(sue) == False:	
				print "You were almost there! Victory was yours! But you gave up too easily."
				print "Next time don't be afraid to take that extra step."
				exit(0)
					
		elif check(next) == False:
			print "You were almost there! Victory was yours! But you gave up too easily."
			print "Next time don't be afraid to take that extra step."
			exit(0)
	
	
print "You're researching a technology company that's been doing some pretty evil stuff:"
print "Are they a likely NSA contractor?"
next = raw_input("y/n> ")
if check(next) == True:
	submit_FOIA()
			
elif check(next) == False:		
	print "You continue your research and try to find other agencies they might do business with."
	exit(0)
	
	
