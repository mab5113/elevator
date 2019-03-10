	try:   	
		while True:
			time.sleep(.5)
			#print ('.')
			pass # do the loop here
	except KeyboardInterrupt:
		# This will catch the ctrl-c to allow clean-up
		print ('Done')
		# do cleanup here
		pass 
		