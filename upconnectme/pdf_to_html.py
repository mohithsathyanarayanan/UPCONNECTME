# Importing required modules
from os import write
import PyPDF2

# Creating a pdf file object

pdfFileObj = open('sample.pdf','rb')
writer = open("pdf_to_html.html","a")
writer.write("<!DOCTYPE html>\n")
writer.write("<html>\n")
writer.write("<body>\n")
count =1

# Creating a pdf reader object

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Getting number of pages in pdf file

pages = pdfReader.numPages

# Loop for reading all the Pages

for i in range(pages):

        # Creating a page object

        pageObj = pdfReader.getPage(i)

       

        # Extracting text from page
        # And splitting it into chunks of lines

        text = pageObj.extractText().split("  ")

        # Finally the lines are stored into list
        # For iterating over list a loop is used

        for i in range(len(text)):

                # Lines are seprated using "\n"
        
                if(count==1): #for detecting the title of the pdf
                    writer.write("<h1>"+text[i]+"</h1>")
                    count=2
                    continue

                if(count!=1):
                    writer.write(text[i]+"<br>\n")

writer.write("</body>\n")
writer.write("</html>\n")

writer.close()
pdfFileObj.close()