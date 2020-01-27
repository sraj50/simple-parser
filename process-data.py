# import regular expression library
import re as re


'''

function: 
preprocessLine(inputLine)

description:
converts character reference to original form and removes any HTML tags

input: 
(string) inputLine, a line from input XML file

returns: 
(string) cleanTxt, cleaned body with HTML tags removed

'''


def preprocessLine(inputLine):

	# substitute "&amp;" with "&" for pattern "amp;" preceded by "&amp;"
	inputLine = re.sub(r'&amp;(?<=amp;)', '&', inputLine)

	inputLine = re.sub(r'&lt;', '<', inputLine)
	inputLine = re.sub(r'&gt;', '>', inputLine)
	inputLine = re.sub(r'&apos;', '\'', inputLine)
	inputLine = re.sub(r'&quot;', '\"', inputLine)
	inputLine = re.sub(r'&amp;', '&', inputLine)
	inputLine = re.sub(r'&#xA;', ' ', inputLine)
	inputLine = re.sub(r'&#xD;', ' ', inputLine)
	inputLine = re.sub(r'"', '', inputLine)
	inputLine = re.sub(r'/>', '', inputLine)

	# substitute any character with 0 or more repeating patterns in <...> with empty character
	cleanTag = re.compile('<.*?>')
	cleanTxt = re.sub(cleanTag, '', inputLine)

	return cleanTxt


'''

function:
splitFile(inFile, outputFile_question, outputFile_answer)

description:
reads input XML file, perform pre-processing to clean the body and split the file into question
and answer based on the post ID type

input:
(file) inFile, input file to be read
(file) outFileQ, output file to be written for questions
(file) outFileA, output file to be written for answers

returns:
None

'''


def splitFile(inFile, outFileQ, outFileA):

	# open file to read input XML file and write to output files
	with open(inFile, 'r', encoding='utf-8') as inFile, open(outFileQ, 'w', encoding='utf-8') as fOutQ,\
			open(outFileA, 'w', encoding='utf-8') as fOutA:

		for line in inFile:

			# check based on postTypeId and write to respective files
			postIdType = re.search('PostTypeId="', line)

			if postIdType is not None:

				# question
				if line[postIdType.end()] == '1':
					line = preprocessLine(line)
					fOutQ.write(line)

				# answer
				elif line[postIdType.end()] == '2':
					line = preprocessLine(line)
					fOutA.write(line)


if __name__ == '__main__':

	fQuestion = 'question.txt'
	f_answer = 'answer.txt'
	f_data = 'data.xml'

	splitFile(f_data, fQuestion, f_answer)
