#Colorizing functions
#will print "[+]" in the color and the rest of the line in the default terminal color
#mimics metasploit

red () { echo -en "\033[0;31m[+]\033[0m" ;}
green () { echo -en "\033[0;32m[+]\033[0m"; }
blue () { echo -en "\033[0;34m[+]\033[0m"; }
purple () { echo -en "\033[0;35m[+]\033[0m"; }