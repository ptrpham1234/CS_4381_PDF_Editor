#############################################################################################################
# Author:              Peter Pham (pxp180041)
# Date Started:        02/17/2022
# IDE:                 pycharm
#
# Description:
# This program is a program specifically tailored for the PDF powerpoints made by Prof Paulk. It trims the
# PDFs and consolidates it all into one powerpoint. It is currently a set trim amount because trimming
# dynamically is not within my skill level. This program will consolidate all PDF within the file so be warned.
#
# TODO: make a user interface for better control of what the program will do. Option to select trim or no trim
#############################################################################################################
import glob
import os

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

basePath = r"".join(os.getcwd())  # get the current directory
files_list = []
savePath = "".join(os.path.join(basePath, 'data'))

if not os.path.exists(savePath):
    os.makedirs(savePath)

print(os.path)

pdfFiles = glob.glob(os.path.join(basePath, '*.pdf'.format('')))  # returns a list of all the PDF files in the directory

writer = PdfFileWriter()  # create a writer to save the updated results

# creates a list of pdf file object types
for file in pdfFiles:
    pdf = PdfFileReader(file)

    files_list.append(pdf)

# open the resulting file to be printed
with open(os.path.join(savePath, "result.pdf"), "wb+") as f:
    for file in files_list:
        # the for loop removes the title page and the last questions page
        for i in range(1, file.getNumPages() - 1):
            page = file.getPage(i)

            # trims the page
            page.cropBox.setLowerLeft((60, 60))
            page.cropBox.setUpperRight((561.6, 725))

            # add it to the page to be printed
            writer.addPage(page)

    # write it to file.
    writer.write(f)
