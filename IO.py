import miniPascal_Shahabi


while True:
	text = input('miniPascal > ')
	if text.strip() == "": continue
	result, error = miniPascal_Shahabi.run('<input>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
			
			


# RUN("example.txt")