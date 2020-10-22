#!/usr/bin/python3
# words = ["ab", "bac", "bb"]
# alphabet = ['c', 'a', 'b']
# result: true

# words2=["ba","ca","cc","bba","aaabbbbccc"]  
"""
func (w,alph):boolean
  loop over words
	two pointers
	c counter
	  looping the nth and nth+1
		check if nth is lesser than nth+1 (Check the index of every character in the word according the alphabet)

"""


def isSorted(options, abc):
	for i in range(1,len(options)):  # For every word in options
		first = options[i-1]
		second = options[i]
		minl = min(len(first), len(second))
		x = 0
		while x < minl:  # For every letter in min len
			first_index = abc.index(first[x])
			second_index = abc.index(second[x])
			if first_index > second_index:
				return False
			elif first_index < second_index:
				x = minl
			x += 1
	return True

print(isSorted(["ab", "bac", "bb"],['c', 'a', 'b']))
print(isSorted(["cab", "cba", "bb"],['c', 'a', 'b']))
print(isSorted(['hajaz','jazcu','hujuz'],['h','u','j','a','z','c','b']))
		
