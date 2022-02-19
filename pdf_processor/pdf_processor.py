import PyPDF2
import os
import sys


input = sys.argv[1:]


def pdf_merger(all_pdfs, destination):
    merger = PyPDF2.PdfFileMerger()
    for pdf in all_pdfs:
        merger.append(pdf)
        print(pdf)
    merger.write(destination)


pdf_merger(input[1:], input[0])
