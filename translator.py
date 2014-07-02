#encoding=utf8
class translator:
	def __init__(self):
# [ consonant, vowel]
		self.words = {
u'تَ'.encode("utf8")[-2:]:['a', "a"],
u'تِ'.encode("utf8")[-2:]:['e', "e"],
u'تُ'.encode("utf8")[-2:]:['o', "o"],
u'ﻁْ'.encode("utf8")[-2:]:["."],
u'ا'.encode("utf8"):['a', 'a'],
u'آ'.encode("utf8"):['a', 'a'],
u'ئ'.encode("utf8"):["a"],
u'ء'.encode("utf8"):["a"],
u'ب'.encode("utf8"):["b"],
u'پ'.encode("utf8"):["p"],
u'ت'.encode("utf8"):["t"],
u'ث'.encode("utf8"):["s"],
u'ج'.encode("utf8"):["j"],
u'چ'.encode("utf8"):["ch"],
u'ح'.encode("utf8"):["h"],
u'خ'.encode("utf8"):["kh"],
u'د'.encode("utf8"):["d"],
u'ذ'.encode("utf8"):["z"],
u'ر'.encode("utf8"):["r"],
u'ز'.encode("utf8"):["z"],
u'ژ'.encode("utf8"):["zh"],
u'س'.encode("utf8"):["s"],
u'ش'.encode("utf8"):["sh"],
u'ص'.encode("utf8"):["s"],
u'ض'.encode("utf8"):["z"],
u'ط'.encode("utf8"):["t"],
u'ظ'.encode("utf8"):["z"],
u'ع'.encode("utf8"):["", 'a'],
u'غ'.encode("utf8"):["gh"],
u'ف'.encode("utf8"):["f"],
u'ق'.encode("utf8"):["gh"],
u'ک'.encode("utf8"):["k"],
u'گ'.encode("utf8"):["g"],
u'ل'.encode("utf8"):["l"],
u'م'.encode("utf8"):["m"],
u'ن'.encode("utf8"):["n"],
u'و'.encode("utf8"):['v', 'o'],
u'ه'.encode("utf8"):["h"],
u'ی'.encode("utf8"):['y', 'i'],
u'ي'.encode("utf8"):['y', 'i']
}
		self.vowels = [u'ﺕَ'.encode("utf8")[-2:],u'ﺕِ'.encode("utf8")[-2:],u'ﺕُ'.encode("utf8")[-2:]]
	def simplef2f(self,word):
		result = ""
		state = 0
		i = 0
# State Machine:
# 0 - (c,?) -> 1 - (v,?) -> 2 - (c,?) -> 3 - (c) -> 4 - (c) -> 5
#                           ^            |          |          |
#                           |___(v,?)____<___(v,?)__<___(v,?)__|
# in the word list first item is always consonant and the second 
# is always vowel
		while i < len(word):
			ch = word[i:i+2]
			if ch not in self.words.keys():
				i += 2
				continue
			if self.words[ch][0] == '.':
				state = 0
				i += 2
                                continue
			if state == 0:
				# definitely a consonant
				result += self.words[ch][0]
				state = 1
			elif state == 1:
				if len(self.words[ch]) > 1: # vowels and semi-vowels both 
				# have a vowel in their presentation
					result += self.words[ch][1]
				else:
					result += 'a'
					i -= 2
				state = 2
			elif state == 2:
				result += self.words[ch][0]
				state = 3
			elif state == 3:
				if len(self.words[ch]) > 1: # vowels and semi-vowels both 
				# have a vowel in their presentation
					result += self.words[ch][1]
					state = 2
				else:
					result += self.words[ch][0]
					state = 4
			elif state == 4:
				if len(self.words[ch]) > 1: # vowels and semi-vowels both 
				# have a vowel in their presentation
					result += self.words[ch][1]
					state = 2
				else:
					result += self.words[ch][0]
					state = 5
			elif state >= 5: # prevent error!
				if len(self.words[ch]) > 1: # vowels and semi-vowels both 
				# have a vowel in their presentation
					result += self.words[ch][1]
					state = 2
				else:
					result += self.words[ch][0]
					state += 1
			else:
				pass
			i += 2
		result = result.replace('aa', 'a')
		result = result.replace('ao', 'o')
		result = result.replace('ae', 'e')
		return result

	def pronf2f(self, pron, word):
		pron = pron.split(" ")
		i = 0
		index = -1
		while i < len(pron):
			if pron[i] == u'یا'.encode("utf8"):
				break
			index = word.find(pron[i][0:2], index + 1)
			if index != -1:
				word = word[:index+2]+pron[i][2:]+word[index+2:]
			else:
				break
			i = i + 1
		return word
	def trf2f(self,pron,word):
		if type(pron) == unicode:
			pron = pron.encode("utf8")
		pron = pron.replace("<p>","")
		pron = pron.replace("</p>","")
		pron = pron.replace(")","")
		pron = pron.replace("(","")
		if pron == word:
			return self.simplef2f(word)
		return self.simplef2f(self.pronf2f(pron,word))

