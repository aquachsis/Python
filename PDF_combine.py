import os, subprocess
from PyPDF2 import PdfFileReader, PdfFileMerger

ext = ('Pdf','pdf','PDF')
files_dir = '/Users/aquach/Desktop/combine'
output_dir = '/Users/aquach/Desktop'
end_of_filename = 'ok'

fileName = input('File name?: ') + end_of_filename
pdf_files = [f for f in os.listdir(files_dir) if f.endswith(ext)]
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(output_dir, fileName+'.pdf'))

filelist = [ f for f in os.listdir(files_dir) if f.endswith(ext) ]
for f in filelist:
    os.remove(files_dir+"/"+f)

subprocess.run(["open", "-a", "/Applications/Preview.app", "/Users/aquach/Desktop/"+fileName+'.pdf'])
