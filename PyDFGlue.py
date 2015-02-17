__author__ = 'Washburn'

print 'load imports'
import sys
from pyPdf import PdfFileWriter, PdfFileReader

print 'load args'
outputPDFName = sys.argv[1]  # TODO: if end is not .pdf add .pdf
pdfsAsString = sys.argv[2:]  # get all pdfs from command line
pdfs = sys.argv[2:]  # just for size
outputPDF = PdfFileWriter()

# glue them
print 'read all PDF as PDF'
for i in range(len(pdfsAsString)):  # load all PDF
    pdfs[i] = PdfFileReader(file(pdfsAsString[i], 'rb'))

print 'glue all pages from all pdf'
for pdf in pdfs:  # get all pages from all PDFs in the new outputPDF
    for i in range(pdf.getNumPages()):
        outputPDF.addPage(pdf.getPage(i))

print 'write to file'
outputStream = file(outputPDFName + '.pdf', 'wb')
outputPDF.write(outputStream)

outputStream.close()
