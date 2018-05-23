from pystache import TemplateSpec
class NestedContext(TemplateSpec):
	def _init_(self, renderer):
		self.renderer = renderer
	
	def _context_get(self, key):
		return self.renderer.context.get(key)
	
	def outer_thing(self):
		return "two"

	# remove the triple quotes to get desired output
	# This example is about nested if type.... if quotes removed you will open foo function and it will work.
"""
	def foo(self):
		return {'thing1': 'one', 'thing2': 'foo'}

	def derp(self):
        	return [{'inner': 'car'}]

    	def herp(self):
        	return [{'outer': 'car'}]
	
    	def nested_context_in_view(self):
        	if self._context_get('outer') == self._context_get('inner'):
        	    return 'it works!'
		return ''
"""
