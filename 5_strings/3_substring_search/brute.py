

def brute_substring_search(txt, pat):
	if len(pat) > len(txt):
		return -1
	output = []
	for i in range(0, len(txt) - len(pat)):
		if pat == txt[i:i+len(pat)]:
			output.append(i)

	return output


if __name__ == "__main__":
	# Driver program to test the above function 
	txt = "GEEKS FOR GEEKS"
	pat = "GEEK"
	print(brute_substring_search(txt, pat) )