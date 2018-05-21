from PyPDF2 import PdfFileWriter, PdfFileReader

# Creates individual PDFs from each page
# Names the inidivudal PDF the employee number + page number

src_filename = 'source.pdf'
# employee number immediately follows ' Number12345 '
split_text_by = ' Number12345 '
chars_in_employee_number = 5

open_src = open(src_filename, 'rb')
pdf_reader = PdfFileReader(open_src)

for i in range(2):
    page = pdf_reader.getPage(i)
    page_text = page.extractText()
    split_page_text = page_text.split(split_text_by)[1]
    employee_number = split_page_text[:chars_in_employee_number]
    print(employee_number)

    #instantiate PdfFileWriter() within loop so it's a new page each time
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page)
    with open('%d - Page %i.pdf' % (int(employee_number), i), 'wb') as f:
        pdf_writer.write(f)

open_src.close()
