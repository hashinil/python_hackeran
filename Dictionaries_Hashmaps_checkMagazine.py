def checkMagazine(magazine, note):
    m_words = {mw:magazine.count(mw) for mw in magazine}

    for nw in note:
        if nw not in magazine or note.count(nw)> m_words[nw]:
            print("No")
            return
    else:
        print("Yes")
        
            

magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["Give", "one", "grand", "today"]
checkMagazine(magazine, note)



answer2


from collections import Counter
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Create Counter objects for both magazine and note
    magazine_counter = Counter(magazine)
    note_counter = Counter(note)

    # Check if the magazine has enough words to form the ransom note
    for word, count in note_counter.items():
        if magazine_counter[word] < count:
            print("No")
            return

    print("Yes")

# Example usage:
magazine = "attack at dawn".split()
note = "Attack at dawn".split()
checkMagazine(magazine, note)
