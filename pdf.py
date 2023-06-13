import PyPDF2
import sys

pdf_list = ['dummy.pdf', 'twopage.pdf']

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(pdf_list)