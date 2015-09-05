__author__ = 'Obstc0rp'

print 'load imports'
import sys
from pyPdf import PdfFileWriter, PdfFileReader

print 'load args'
outputPDFName = sys.argv[1]  # TODO: if end is not .pdf add .pdf
rotationAngle = int(sys.argv[2])  # angle for rotation (clockwise)
pdfsAsString = sys.argv[3:]  # get all pdfs from command line
pdfs = sys.argv[3:]  # just for size
outputPDF = PdfFileWriter()

# glue them
print 'read all PDF as PDF'
for i in range(len(pdfsAsString)):  # load all PDF
    pdfs[i] = PdfFileReader(file(pdfsAsString[i], 'rb'))

print 'rotate all pages from all pdf'
for pdf in pdfs:  # get all pages from all PDFs in the new outputPDF
    for i in range(pdf.getNumPages()):
        pdf.getPage(i).rotateClockwise(rotationAngle)
        outputPDF.addPage(pdf.getPage(i))

print 'write to file'
outputStream = file(outputPDFName + '.pdf', 'wb')
outputPDF.write(outputStream)

outputStream.close()
