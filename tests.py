import pyautogui, time, random

time.sleep(3)

import os
def push():
    while True:
        os.system("git add . && git commit -m 'update' && git push origin main")
        time.sleep(60*60)

import threading
threading.Thread(target=push).start()

while True:
    pyautogui.hotkey('ctrl', 's')
    pyautogui.typewrite(random.choice(["a","b","c","d","e"]))
    time.sleep(5)

# dacdbcdaaaecaecdabbbebaaacaadbcdedcdbaecceeaeeeeeebeaddadcebeedcabedbaabecadeddddbdbccedeaaebccbbdcddbdabcecacdcbbddaddabddeeaecdcecdadcdbccaaebadbbbebdaebbbabdcbaeddaddcaddecadbccceeecedebddaabeddbddaddcaebaecbaedcbcdcacccedaceeebdbcdacdedebcbcbdbddaacdbecbabbdbbbedaeadcdcebabcecbeecededdcbdcbcaedbabddaeeadecdbccabdacaaaacceedacbbabaedecbaaccceeadcabacaaddccecdaddaceaecdbaceaadcdacdabcedbbdacebcdebcdaacbdeddeacdeeddacaeabaeabbdbdeccdcecbeaaedcdaadbaeeaaaadbecebdadeccebacaccdcabedcbddedbbceecbaccdacbbddaeeccddbabeaacacceddbdceaedddddeabeaedcddbadedccdbcedcebaadeabccceeacbaeeedaddccccacdbebbdbdadddacaeaccdbeacddccebbaacdeeeedebddccdddedecbdaeddbaaaeadadceeccbcceeaeeeceaddcdabedddcebcc