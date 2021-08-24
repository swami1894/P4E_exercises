text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0.8475')
num = text[23:]
print(float(num))
