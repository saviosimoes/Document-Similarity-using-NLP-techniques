import PyPDF2
import docx
print('Enter the type of file you want To Comapre: ' )
print('Press 1 for .PDF file.')
print('Press 2 for .DOCX file.')
print('Press 3 for .txt file.')

typ = int(input('Enter the number: '))

if typ == 1:
  pdf1 = open('/content/hartanto.pdf', mode='rb')
  pdf2 = open('/content/hartanto.pdf',mode='rb')
  
  pdf_document2 = PyPDF2.PdfFileReader(pdf1)
  pdf_document1 = PyPDF2.PdfFileReader(pdf2)

  lenn1 = pdf_document1.numPages
  lenn2 = pdf_document2.numPages

  array = []
  for i in range(0,lenn1):
    page = pdf_document1.getPage(i)
    print("PDF1 Page ends",i+1)
    a = page.extractText()

  file = open("pdff1.txt", "w") 
  file.write(a) 
  file.close() 

  for i in range(0,lenn2):
    page = pdf_document2.getPage(i)
    print("PDF2 Page ends",i+1)
    b = page.extractText()

  file = open("pdff2.txt", "w") 
  file.write(b) 
  file.close()
  documentSimilarity('pdff1.txt', 'pdff2.txt')
elif typ == 2: 
  def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
      fullText.append(para.text)
    return '\n'.join(fullText)
  
  docc1 = getText('/content/Emerald106Application for L&L.docx')
  docc2 = getText('/content/Emerald1306Application for L&L.docx')

  file = open("docx1.txt", "w") 
  file.write(docc1) 
  file.close() 
  file = open("docx2.txt", "w") 
  file.write(docc2) 
  file.close() 
  documentSimilarity('docx1.txt', 'docx2.txt')
elif typ == 3:
  documentSimilarity('filename1.txt', 'filename2.txt')
else:
  print('Enter Valid option.')



import math
import string
import sys

def read_file(filename):
	
	try:
		with open(filename, 'r') as f:
			data = f.read()
		return data
	
	except IOError:
		print("Error opening or reading input file: ", filename)
		sys.exit()

translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	
def get_words_from_line_list(text):
	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list

def count_frequency(word_list):
	
	D = {}
	
	for new_word in word_list:
		
		if new_word in D:
			D[new_word] = D[new_word] + 1
			
		else:
			D[new_word] = 1
			
	return D

def word_frequencies_for_file(filename):
	
	line_list = read_file(filename)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_frequency(word_list)

	print("File", filename, ":", )
	print(len(line_list), "lines, ", )
	print(len(word_list), "words, ", )
	print(len(freq_mapping), "distinct words")

	return freq_mapping

def dotProduct(D1, D2):
	Sum = 0.0
	
	for key in D1:
		
		if key in D2:
			Sum += (D1[key] * D2[key])
			
	return Sum
  
def vector_angle(D1, D2):
	numerator = dotProduct(D1, D2)
	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	
	return math.acos(numerator / denominator)


def documentSimilarity(filename_1, filename_2):
	sorted_word_list_1 = word_frequencies_for_file(filename_1)
	sorted_word_list_2 = word_frequencies_for_file(filename_2)
	distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
	
	print("The distance between the documents is: % 0.6f (radians)"% distance)
	



