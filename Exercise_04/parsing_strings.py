txt = 'X-DSPAM-Confidence: 0.8475'

ipos = txt.find(':')
print(ipos)

piece = txt[ipos:] # get the value from ':' to the end of the text
print(piece)

piece = txt[ipos+1:]
print(piece) # keeps a blank space at the beginning

value = float(piece)
print(value) # removes the blank space