
from string import Template

def main() :
	TemplateTest.demo()
	UnpackingTest.demo()

class TemplateTest:
	
	KEYWORD_VARIABLE_TEMPLATE = '<foo="{foo}" bar:"{bar}">'
	
	@classmethod
	def demo(Class):
		Class.KeywordVariableTemplate.demo()
	
	class KeywordVariableTemplate:
		
		@classmethod
		def demo(Class):
			kwargs = {'foo':'qaz', 'bar':'qazqaz'}
			print(TemplateTest.KEYWORD_VARIABLE_TEMPLATE.format(**kwargs))
				#--> <foo="qaz" bar:"qazqaz">
			print(TemplateTest.KEYWORD_VARIABLE_TEMPLATE.format(foo="qaz", bar="qazqaz"))
				#--> <foo="qaz" bar:"qazqaz">
			
			result = Class().template("qaz")
			print("result", "is", result)
				#--> result is <foo="qaz" bar:"qazqaz">
			
			print('{}, {}, {}'.format('foo', 'bar', 'baz'))
				#--> foo, bar, baz
			print('{0}, {1}, {2}'.format('foo', 'bar', 'baz'))
				#--> foo, bar, baz
			print('{2}, {1}, {0}'.format('foo', 'bar', 'baz'))
				#--> baz, bar, foo
			
			t = Template('{foo:"$foo" bar:"$bar"}')
			print(t.substitute(foo="qaz", bar="qazqaz"))
				#--> {foo:"qaz" bar:"qazqaz"}
			d = dict(foo="qaz", bar="qazqaz")
			print(t.substitute(d))
				#--> {foo:"qaz" bar:"qazqaz"}
		
		def template(self, foo):
			bar = foo + foo
			return TemplateTest.KEYWORD_VARIABLE_TEMPLATE.format(**locals())

class UnpackingTest:
	
	@classmethod
	def demo(Class):
		instance = Class()
		
		instance.print_args(1, 2, 3, x='X')
			#--> tuple (1, 2, 3) dict {'x': 'X'}
		instance.print_args(1, 2, 3, x='X', y='Y')
			#--> tuple (1, 2, 3) dict {'y': 'Y', 'x': 'X'}
		
		d = {'x':'X', 'y':'Y'}
		instance.print_args(1, 2, 3, d)
			#--> tuple (1, 2, 3, {'x': 'X', 'y': 'Y'}) dict {}
		instance.print_args(1, 2, 3, **d)
			#--> tuple (1, 2, 3) dict {'x': 'X', 'y': 'Y'}
		
		instance.print_args(1, 2, 3, dict(x="X", y="Y"))
			#--> tuple (1, 2, 3, {'x': 'X', 'y': 'Y'}) dict {}
		instance.print_args(1, 2, 3, **dict(x="X", y="Y"))
			#--> tuple (1, 2, 3) dict {'y': 'Y', 'x': 'X'}
		
		s = (1, 2, 3)
		d = dict(x="X", y="Y")
		instance.print_args(*s, **d)
			#--> tuple (1, 2, 3) dict {'y': 'Y', 'x': 'X'}
		
		s = ['a', 'b', 'c', 'd']
		instance.unpack(s)
			#--> a b
			#--> tuple ('z', 'b', ['c', 'd']) dict {}
			#--> tuple ('z', 'b', 'c', 'd') dict {}
	
	def print_args(self, *args, **kwargs):
		print(args.__class__.__name__, args,
			kwargs.__class__.__name__, kwargs)
	
	def unpack(self, sequence):
		first, second, *rest = sequence
		print(first, second)
		self.print_args(first, second, rest)
		self.print_args(first, second, *rest)

if __name__ == "__main__":
	main()
