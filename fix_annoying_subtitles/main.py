#finds if there's (TEXTexample) and -(TEXTexample)
#then deletes them and characters inside them too
# !!didnt work this time idk what happened!!

import re

TEXT = r'Subtitle_1_2.srt'

def no_dash_and_braces(input):
    input = input()
    eng_sub = open(input).read()
    no_dash_eng_sub = re.sub(r'-\(.*\)', '', eng_sub)

    open(input, "w").write(no_dash_eng_sub)

    #braces
    eng_sub = open(TEXT).read()
    no_braces_eng_sub = re.sub(r'\(.*\)', '', eng_sub)

    open(input, "w").write(no_braces_eng_sub)

no_dash_and_braces()
