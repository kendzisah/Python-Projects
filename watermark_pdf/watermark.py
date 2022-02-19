import PyPDF2
import sys


input_files = sys.argv[1:]
number = 0


def get_files(input_files):
    watermark = PyPDF2.PdfFileReader(open(input_files[0], 'rb'))

    for pdfs in input_files[1:]:
        new_file_name = pdfs[0:len(pdfs) - 4]
        template = PyPDF2.PdfFileReader(open(pdfs, 'rb'))
        output = PyPDF2.PdfFileWriter()
        watermark_pdf(template, output, watermark, new_file_name)


def watermark_pdf(template, output, watermark, new_file_name):
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        global number
        with open(f'{new_file_name}_watermarked_output{number}.pdf', 'wb') as file:
            output.write(file)
    number += 1


get_files(input_files)
