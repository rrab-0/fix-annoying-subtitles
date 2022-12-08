#finds if there's (TEXTexample) and -(TEXTexample)
#then deletes them and characters inside them too
# !!didnt work this time idk what happened!!

import re

file_name = input()

def no_dash_and_braces():
    
    eng_sub = open(file_name).read()
    no_dash_eng_sub = re.sub(r'-\(.*\)', '', eng_sub)

    open(file_name, "w").write(no_dash_eng_sub)

    #braces
    eng_sub = open(file_name).read()
    no_braces_eng_sub = re.sub(r'\(.*\)', '', eng_sub)

    open(file_name, "w").write(no_braces_eng_sub)

no_dash_and_braces()
