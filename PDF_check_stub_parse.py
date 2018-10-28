from PyPDF2 import PdfFileWriter, PdfFileReader

src_file = open('check_stubs.PDF', 'rb')
reader = PdfFileReader(src_file)
employee_id_chars = 5

for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page_text = page.extractText()
    if i == 0:
        employee_id_substring = page_text.split('Employee ID\n')[1]
        employee_id = employee_id_substring[:employee_id_chars]
        print('Page: ' + str(i) + ' -- Employee ID: ' + employee_id + '\n')
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page)
    else:
        try:
            employee_id_substring = page_text.split('Employee ID\n')[1]
            with open(str(i) + ' - %d.pdf' % int(employee_id), 'wb') as file:
                pdf_writer.write(file)
            employee_id = employee_id_substring[:employee_id_chars]
            print('Page: ' + str(i) + ' -- Employee ID: ' + employee_id + '\n')
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(page)
        except IndexError:
            pdf_writer.addPage(page)
src_file.close()
