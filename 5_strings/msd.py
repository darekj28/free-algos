# Source : https://gist.github.com/nlguillemot/3093825

def MSD_radix_string_sort(L, i):

	# base case (list must already be sorted)
	if len(L) <= 1:
		return L

	# divide (first by length, then by lexicographical order of the first character)
	done_bucket = []
	buckets = [ [] for x in range(27) ] # one for each letter in a-z

	for s in L:
		if i >= len(s):
			done_bucket.append(s)
		else:
			buckets[ ord(s[i]) - ord('a') ].append(s)

	# conquer (recursively sort buckets)
	buckets = [ MSD_radix_string_sort(b, i + 1) for b in buckets ]

	# marry (chain all buckets together)
	return done_bucket + [ b for blist in buckets for b in blist ]

def main():
	L = ['joe', '', 'bob', 'rot', 'rocket', 'rock', 'z', 'mary', 'suzy', 'sue']
	print L
	L = MSD_radix_string_sort(L, 0)
	print L

if __name__ == '__main__':
	main()