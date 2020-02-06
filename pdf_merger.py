import PyPDF2
from PyPDF2 import PdfFileMerger,PdfFileWriter, PdfFileReader
import os

dir_list = os.listdir('D:\\Suven_python')
# dir_list = os.listdir('D:\\')
merge_list = []

for f_name in dir_list:
    if f_name.endswith('.pdf'):
        print('File -> ',f_name)
        merge_list.append(f_name)

merge_list.sort()

#start_page = int(input('Enter first page -> '))
#last_page = int(input('Enter last page -> '))        

# merger = PdfFileMerger()
# for pdf in merge_list:
    # merger.append(pdf, pages=(start_page,last_page))
# with open('merged.pdf','wb') as merge_file:
    # merger.write(merge_file)
    
pdf_writer = PdfFileWriter()

for pdf in merge_list:
    start_page = int(input('Enter first page -> '))
    last_page = int(input('Enter last page -> '))    
    pdf_reader = PdfFileReader(pdf)
    for page_no in range(start_page,last_page):
        if pdf_reader.getNumPages() > page_no :
            pdf_writer.addPage(pdf_reader.getPage(page_no))

with open('merge.pdf','wb') as merge_file:
            pdf_writer.write(merge_file)
