def check_palindrome(num):
	num = str(num)
	reversed_num = num[::-1]
	
	if num == reversed_num:
		return True
	else:
		return False
		

print 'checking 123: ', check_palindrome(123)
print 'checking 12321: ', check_palindrome(12321)

