import time

nonsense = 'zsxdrcftvgbyhnjxrctvfgy;buhnjxrectvfgybuhnjimrxectvygbuhnrxectvygbuhnjimkctrvybuhnjim'

for char in nonsense:
    if char == ';':
        break
    time.sleep(0.5)
    print(char)