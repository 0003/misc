__author__ = 'wleach'

with open('/usr/share/dict/words','r') as f:
    words = f.read()
words = [ word for word in words if all([word[0].lower() in 'abc', len(word)>3])]

print words
