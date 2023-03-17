# Open and read the first file
with open('test.en', 'r') as file1:
    words1 = set(file1.read().split())

# Open and read the second file
with open('pred_nbest5.txt', 'r') as file2:
    words2 = set(file2.read().split())

# Find the intersection of the two sets of words
common_words = words1.intersection(words2)
print(len(common_words))

# Print the common words
# print("Common words in both files: ", common_words)
# with open("small_inter.en", "w")as f:
#      for word in common_words:
#          f.write(word+"\n")