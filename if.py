age = input('嗨～您好 請輸入您的年齡')
age = int(age)
if age >= 20:
	print('你可以投票')
else:
	print('你還不能投票喔')
	diff = 20 - age
	print('再等',diff,'年就可以投票啦')
