#Colorizing functions
#will print "[+]" in the color and the rest of the line in the default terminal color
#mimics metasploit

red () { echo -en "\033[0;31m[+]\033[0m" ;}
green () { echo -en "\033[0;32m[+]\033[0m"; }
blue () { echo -en "\033[0;34m[+]\033[0m"; }
purple () { echo -en "\033[0;35m[+]\033[0m"; }


#you can also simply use the terminfo definitions:
#   -Once you call the color, the rest of the text will be that color until you call something else (typically call $NORMAL to end it)
BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
LIME_YELLOW=$(tput setaf 190)
POWDER_BLUE=$(tput setaf 153)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
BRIGHT=$(tput bold)
NORMAL=$(tput sgr0)
BLINK=$(tput blink)
REVERSE=$(tput smso)
UNDERLINE="$(tput smul)"
