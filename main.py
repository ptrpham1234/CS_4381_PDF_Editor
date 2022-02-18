import glob
import os

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

basePath = r"".join(os.getcwd())
files_list = []

filePaths = glob.glob(os.path.join(basePath, '*.pdf'.format('')))

print(filePaths)

writer = PdfFileWriter()  # create a writer to save the updated results
merger = PdfFileMerger()

for file in filePaths:
    pdf = PdfFileReader(file)

    files_list.append(pdf)

with open("result.pdf", "ab+") as f:
    for file in files_list:
        i = 1
        for i in range(1, file.getNumPages() - 1):

            page = file.getPage(i)

            page.cropBox.setLowerLeft((60, 60))
            page.cropBox.setUpperRight((561.6, 725))

            writer.addPage(page)

    writer.write(f)


