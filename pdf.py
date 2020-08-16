import PyPDF2
import sys # this is for input the arguments

input=sys.argv[1:] #so as to take argument

def pdf_combiner(pdf_list):
 merger=PyPDF2.PdfFileMerger()
 for pdf in pdf_list:
  print(pdf)
  merger.append(pdf)
 merger.write('super.pdf')



pdf_combiner(input)


