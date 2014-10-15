import yappi

a = "Sok"
b = "Tsak"
c = "Lok"
d = "Fok"
e = "Yikes"

yappi.set_clock_type('cpu')

def slow(a, b, c, d):
	print a + b + c + d

def fast(a, b, c, d):
	print "%s%s%s%s" % (a, b, c, d)

yappi.start(builtins=True, profile_threads=True)

slow(a, b, c, d)

fast(a, b, c, d)

yappi.stop()   
yappi.get_func_stats().print_all()
