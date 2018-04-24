s = 'X-DSPAM-Confidence: 0.8475 '
start = s.find(':')
str = float(s[start+1:])
print(str)
