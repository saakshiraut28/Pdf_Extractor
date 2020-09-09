from PyPDF2 import PdfFileReader

# Enter your pdf file location:
file=open('C:/Users/Owner/Documents/Virtualization in cc.pdf', "rb")

# Reads the file info
reader=PdfFileReader(file)
print("\nDocument INFO: ",(reader.getDocumentInfo()))

print("\n__________________________________________________________________________________________________\n")

print("\nPages: ",reader.getNumPages())

print("\nPDF File created by: ",reader.getDocumentInfo().creator)

print("\n__________________________________________________________________________________________________\n")

pages=reader.getNumPages()
for i in range(0,pages):
    print("Page Number: ",i+1)
    print("\n***\n")
    pageobj = reader.getPage(i)
    print(pageobj.extractText)
    print("\n__________________________________________________________________________________________________\n")
file.close()
