"""
Program to translate into Pig Latina
"""

consonant_end = 'a'
vowel_end = 'way'
consonant_clusters_end = 'ay'


original_word = input('Enter a word: ')

if len(original_word) > 0 and original_word.isalpha():
  word = original_word.lower()
  first = word[0]
  if first in 'aeiou':
  	new_word = word + vowel_end
  	print (new_word)
  else:
  	if first in 'cst':
  		second = word[1]
  		if second in 'hmtqw':
  			third = word[2]
  			if third in 'aeiou':
  				new_word = word[2:len(word)] + word[0:2] + consonant_clusters_end
  				print (new_word)
  			else:
  				new_word = word[3:len(word)] + word[0:3] + consonant_clusters_end
  				print (new_word)
  		else:
  			new_word = word[1:len(word)] + word[0] + consonant_end
  			print (new_word)
  	else:
  		new_word = word[1:len(word)] + word[0] + consonant_end
  		print (new_word)
else:
    print ('empty')