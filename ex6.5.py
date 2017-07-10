text = "X-DSPAM-Confidence:    0.8475";
rmSpText = text.replace(" ","")
beg = rmSpText.find(":")
num = float(rmSpText[beg+1:])
print(num)

