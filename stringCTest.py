"""
This is a test for markup generator new
"""
import yappi

yappi.set_clock_type('cpu')

def current(a, b, c, d, e, f):
	return a + b + str(c) + d + str(e) + f

def new(a, b, c, d, e, f):
	return "%s%s%s%s%s%s" % (a, b, c, d, e, f)

html1 = "http://ads.engagefront.com/track/imp?"
html2 = "imp_impid="
html3 = 88
html4 = "&pri="
html5 = 500
html6 = "&ord=%%CACHEBUSTER%%&rinf=${REQ_INFO}"

yappi.start(builtins=True, profile_threads=True)

a = current(html1, html2, html3, html4, html5, html6)

b = new(html1, html2, html3, html4, html5, html6)

print a
print b

yappi.stop()   
yappi.get_func_stats().print_all()
