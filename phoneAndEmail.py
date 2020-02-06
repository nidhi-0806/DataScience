import re
import pprint

with open('D:\\Suven_python\\linkedin_comments.txt') as txt_file:
	raw_text = txt_file.read()

comments_list = str(raw_text).split('\n\n')
#pprint.pprint(comments_list)
	
phoneRegex = re.compile(r'\d{10}',re.VERBOSE)
emailRegex = re.compile(r'[\w\.-]+@[\w\.-]+',re.VERBOSE)
# TODO: Find matches in text file.

for comment in comments_list:
	matched_no = phoneRegex.findall(comment)
	matched_email = emailRegex.findall(comment)
	if matched_no:
		print('Number -> ',matched_no)
	else:
		print('Number -> NA')

	if matched_email:
		print('Email -> ',matched_email)
	else:
		print('Email -> NA')

	print('-'*50)



