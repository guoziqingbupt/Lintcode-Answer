class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """

    def countRotateWords(self, words):
        if len(words) == 0:
            return 0
        record = {words[0]:len(words[0])}
        for word in words[1:]:
            exist = False
            temp = len(word)
            newWord = word + word
            for i in record:
                if i in newWord and len(i) == temp:
                    exist = True
                    break
            if not exist:
                record[word] = len(word)
        return len(record)
