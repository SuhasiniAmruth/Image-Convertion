#7. Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.	
#X-DSPAM-Confidence:    0.8475



str = 'X-DSPAM-Confidence:    0.8475'
search = str.find('0.8475')
print(float(str[23: ]))
print(search)

