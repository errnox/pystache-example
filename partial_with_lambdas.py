
def rot(s, n=13):
    r = ""
    for c in s:
        cc = c
        if cc.isalpha():
            cc = cc.lower()
            o = ord(cc)
            ro = (o+n) % 122
            if ro == 0: ro = 122
            if ro < 97: ro += 96
            cc = chr(ro)
        r = ''.join((r,cc))
    return r

class PartialWithLambdas(object):
	def rot13(self, text=None):
		return rot

