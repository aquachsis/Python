from PyPDF2 import PdfFileWriter, PdfFileReader

src_file = open('check_stub.PDF', 'rb')
reader = PdfFileReader(src_file)
employee_id_chars = 5

for i in range(2):
    page = reader.getPage(i)
    page_text = page.extractText()
    employee_id_substring = page_text.split('Employee ID\n')[1]
    employee_id = employee_id_substring[:employee_id_chars]

    print('Page: ' + str(i + 1))
    print('Employee ID: ' + employee_id)
    print('\n')

    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page)
    with open('%d.pdf' % int(employee_id), 'wb') as file:
        pdf_writer.write(file)
# page = reader.getPage(0)
# page_text = page.extractText()
# print(page_text)

src_file.close()
