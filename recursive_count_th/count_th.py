'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if length of the word only has 1 or less letters, it can't have "th" in it
    if len(word) <= 1:
        return 0
    
    #set the variable to 0 to keep track
    count = 0
    
    #If the word has a "t" and is followed by an "h", add it to the count
    if word[0] == 't' and word [1] == 'h':
        count += 1
        
    #use recursion to check adjacent letters
    #remove the first position and check the next until they match
    
    return count + count_th(word[1: ])
