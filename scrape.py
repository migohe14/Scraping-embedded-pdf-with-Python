import requests, PyPDF2
# import textract
import subprocess
import os
from time import sleep
import random

session = requests.session()
session.proxies = {}


r = session.get('http://www.urlexample.com/')

# Install TOR
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

session.proxies['http'] = 'http://89.36.219.208:3128'
session.proxies['http'] = 'http://89.36.219.208:3128'

# Check your IP
r = session.get('http://httpbin.org/ip')
print(r.text)


for i in range(50,100):
    if i < 10:
        i = "%02d" % (i,)
 
    url = 'http://www.urlexample.com/21739{}'.format(i)
    r = session.get(url)
    my_raw_data = r.content

    with open("{}pdf.pdf".format(i), 'wb') as my_data:
        my_data.write(my_raw_data)

    open_pdf_file = open("{}pdf.pdf".format(i), 'rb')
    read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
    if read_pdf.isEncrypted:
        print("Encrypted")
        read_pdf.decrypt("")
        # print(read_pdf.getPage(0).extractText())

    else:
        print("Not Encrypted")
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print(page_content)
        subprocess.call(['pdftotext', '{}pdf.pdf'.format(i), '{}output'.format(i)])
        j = random.randint(1,10)
        print(j)
        sleep(j)
        

# Delete PDF

for i in range(0,100):   
    i = "%02d" % (i,)
    os.remove('{}pdf.pdf'.format(i))
       
