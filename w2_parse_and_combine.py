# Splits single single by employee numbers
# recombines PDFs where employee numbers are the same

from PyPDF2 import PdfFileWriter, PdfFileReader

src_filename = 'source.pdf'
# employee number immediately follows ' Number12345 '
split_text_by = ' Number12345 '
ee_num_chars = 5

open_src = open(src_filename, 'rb')
pdf_reader = PdfFileReader(open_src)
last_employee = ''

for i in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(i)
    page_text = page.extractText()
    split_page_text = page_text.split(split_text_by)[1]
    employee_number = split_page_text[:ee_num_chars]

    if i == 0:
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page)
    elif last_employee == employee_number:
        pdf_writer.addPage(page)
        print('added page')
    else:
        with open('%d.pdf' % (int(last_employee)), 'wb') as f:
            pdf_writer.write(f)
        # NOTE for debugging
        print('file created' + 'Page %i - %d.pdf' % (i, int(last_employee)) + ' else statement')
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page)

    print(
        'iteration:  '+ str(i) + '\n' +
        'last employee: ' + last_employee  + '\n' +
        'this employee: ' + employee_number
        )
    last_employee = employee_number
    print('\n')
    with open('%d.pdf' % (int(last_employee)), 'wb') as f:
        pdf_writer.write(f)
    # NOTE for debugging
    print('file created' + 'Page %i - %d.pdf' % (i, int(last_employee)))
open_src.close()
