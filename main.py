from PyPDF2 import pdf


watermark = pdf.PdfFileReader(open('./assets/215_wtr.pdf', 'rb'))
template = pdf.PdfFileReader(open('./assets/215_twopage.pdf', 'rb'))
writer = pdf.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)

writer.write(open('./out/output.pdf', 'wb'))
