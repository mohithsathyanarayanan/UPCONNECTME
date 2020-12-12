from os import write


reader = open("demofile.txt", "r")
writer = open("doc_to_html.html", "a")
writer.write("<!DOCTYPE html>\n")
writer.write("<html>\n")
writer.write("<body>\n")
count = 1


for i in reader :

    if(count==1) :  #for title
        count = 2 
        writer.write("<h1>"+i+"</h1>\n")
        continue

    if(count!=1):
        writer.write(i+"<br>")

writer.write("</body>\n")
writer.write("</html>\n")

reader.close()
writer.close()

        
    