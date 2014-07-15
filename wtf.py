__author__ = 'wleach'
import random

MESSAGE = 'wtf'

with open('/usr/share/dict/words','r') as f:
    words = f.readlines()

word_dict = dict((c, []) for c in MESSAGE)
print word_dict
words = [ ''.join(word.split()) for word in words if all([word[0].lower() in MESSAGE, len(word)>3])]

for word in words:
    word_dict[word[0].lower()] += [word]

print word_dict

wtf = random.choice(word_dict['w']) + ' ' + random.choice(word_dict['t']) + ' ' + random.choice(word_dict['f'])

print wtf
