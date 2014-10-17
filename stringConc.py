"""
string conc test
"""

import yappi
import sys
import datetime

a = "Lok"
b = "Lsak"
c = "Lok"
d = "Looook"
e = "Yikes"
f = "POL"

#yappi.set_clock_type('cpu')

def slow(a, b, c, d):
	print a + b + c + d

def fast(a, b, c, d):
	print "%s%s%s%s" % (a, b, c, d)

#yappi.start(builtins=False, profile_threads=True)

print "The slow is: "
slow(a, b, c, d)

print "The fast is: "
fast(a, b, c, d)

print "me"

#yappi.stop()   
#yappi.get_func_stats().print_all()
