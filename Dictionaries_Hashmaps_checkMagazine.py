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
