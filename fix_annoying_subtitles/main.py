# finds if there's (TEXTexample) and -(TEXTexample)
# then deletes them and characters inside them too
# !!didnt work this time idk what happened!!
# it works bro idk what ^ ur talking about
# accepts only .srt format

import re

print('type in the file (srt format) name including .srt')
file_name = input()


def no_dash_and_braces():

    eng_sub = open(file_name).read()
    no_dash_eng_sub = re.sub(r'-\(.*\)', '', eng_sub)

    open(file_name, "w").write(no_dash_eng_sub)

    # braces
    eng_sub = open(file_name).read()
    no_braces_eng_sub = re.sub(r'\(.*\)', '', eng_sub)

    open(file_name, "w").write(no_braces_eng_sub)


no_dash_and_braces()
