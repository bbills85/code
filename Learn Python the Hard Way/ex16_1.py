from sys import argv

script, filename = argv

txt = open(filename)

print "Here is what is inside of %r" % filename
print txt.read()

txt.close()