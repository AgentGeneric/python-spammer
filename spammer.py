import pyautogui
import time
import keyboard

print("""
  sSSs   .S_sSSs     .S_SSSs     .S_SsS_S.    .S_SsS_S.     sSSs   .S_sSSs    
 d%%SP  .SS~YS%%b   .SS~SSSSS   .SS~S*S~SS.  .SS~S*S~SS.   d%%SP  .SS~YS%%b   
d%S'    S%S   `S%b  S%S   SSSS  S%S `Y' S%S  S%S `Y' S%S  d%S'    S%S   `S%b  
S%|     S%S    S%S  S%S    S%S  S%S     S%S  S%S     S%S  S%S     S%S    S%S  
S&S     S%S    d*S  S%S SSSS%S  S%S     S%S  S%S     S%S  S&S     S%S    d*S  
Y&Ss    S&S   .S*S  S&S  SSS%S  S&S     S&S  S&S     S&S  S&S_Ss  S&S   .S*S  
`S&&S   S&S_sdSSS   S&S    S&S  S&S     S&S  S&S     S&S  S&S~SP  S&S_sdSSS   
  `S*S  S&S~YSSY    S&S    S&S  S&S     S&S  S&S     S&S  S&S     S&S~YSY%b   
   l*S  S*S         S*S    S&S  S*S     S*S  S*S     S*S  S*b     S*S   `S%b  
  .S*P  S*S         S*S    S*S  S*S     S*S  S*S     S*S  S*S.    S*S    S%S  
sSS*S   S*S         S*S    S*S  S*S     S*S  S*S     S*S   SSSbs  S*S    S&S  
YSS'    S*S         SSS    S*S  SSS     S*S  SSS     S*S    YSSP  S*S    SSS  
        SP                 SP           SP           SP           SP          
        Y                  Y            Y            Y            Y           
                                                                              """)
# Spaces
print("")
print("")

print("[+]Github: https://github.com/c00LAgent/")
print("[+]Twitter: https://twitter.com/AgentGeneric")

# Spaces
print("")
print("")

print("{Press ESC to stop the spammer}")

# Input File Path
filePath = input("[*] Enter File Path: ")
loopSpam = str(input("[*] Spam on an Infinite Loop?(y/n): "))

# Spaces
print("")
print("")

print("[+] Sending...")

time.sleep(5)

# Read File
readFile = open(filePath, 'r')

if loopSpam == "y":
    while True:
        for word in readFile:
            readFile = open(filePath, 'r')
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            if keyboard.is_pressed('Esc'):
                # Spaces
                print("")
                print("[+] Exiting...")
                exit()

elif loopSpam == "n":
    # Read File
    for word in readFile:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        if keyboard.is_pressed('Esc'):
            # Spaces
            print("")
            print("[+] Done")
            print("[+] Exiting...")
            exit()
else:
    # Spaces
    print("")
    print("")

    print("[+] Please choose y/n!")
    exit()

# Spaces
print("")
print("[+] Done")
print("[+] Exiting...")
exit()