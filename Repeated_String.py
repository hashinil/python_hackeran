def repeatedString(s, n):
    a_in_s = s.count('a')
    s_repeat = n//len(s)

    a_in_str = a_in_s * s_repeat
    
    letters_in_str = len(s) * s_repeat
    remain_letters = n - letters_in_str

    a_in_remain = s[0:remain_letters].count('a')
    
    return a_in_str + a_in_remain
