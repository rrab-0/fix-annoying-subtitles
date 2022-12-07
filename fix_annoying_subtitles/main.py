#finds if there's (TEXTexample) and -(TEXTexample)
#then deletes them and characters inside them too
# !!didnt work this time idk what happened!!


# update, it works now
# no need to use findall, sub function does the work itself

import re

TEXT = r'Subtitle_1_2.srt'

# def no_dash():
#     eng_sub = open(TEXT).read()
#     no_dash_eng_sub = re.sub(r'-\(.*\)', '', eng_sub)

#     open(TEXT, "w").write(no_dash_eng_sub)

# def no_braces():
#     eng_sub = open(TEXT).read()
#     no_braces_eng_sub = re.sub(r'\(.*\)', '', eng_sub)

#     open(TEXT, "w").write(no_braces_eng_sub)

def no_dash_and_braces():
    #dash
    eng_sub = open(TEXT).read()
    no_dash_eng_sub = re.sub(r'-\(.*\)', '', eng_sub)

    open(TEXT, "w").write(no_dash_eng_sub)

    #braces
    eng_sub = open(TEXT).read()
    no_braces_eng_sub = re.sub(r'\(.*\)', '', eng_sub)

    open(TEXT, "w").write(no_braces_eng_sub)


# no_dash()
# no_braces()
no_dash_and_braces()
