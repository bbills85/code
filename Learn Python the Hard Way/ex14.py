from sys import argv

script, user_nameFirst, user_nameLast = argv
prompt = '$ '

print "Hi %s %s, I'm the %s script." % (user_nameFirst, user_nameLast, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_nameFirst
likes = raw_input(prompt)

print "Where do you live %s?" % user_nameFirst
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about like me.
You live in %r. Not sure what that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)