#Colorizing functions
#will print "[+]" in the color and the rest of the line in the default terminal color
#mimics metasploit

echo_color() {
	case ${1} in
	black)
		shift 1
		#echo $(COLOR)${user-supplied-text}$(NORMAL-COLOR)
		echo $(tput setaf 0)${*}$(tput sgr0)
		;;
	red)
		shift 1
		echo $(tput setaf 1)${*}$(tput sgr0)
		;;
	green)
		shift 1
		echo $(tput setaf 2)${*}$(tput sgr0)
		;;
	yellow)
		shift 1
		echo $(tput setaf 3)${*}$(tput sgr0)
		;;
	blue)
		shift 1
		echo $(tput setaf 1)${*}$(tput sgr0)
		;;
	cyan)
		shift 1
		echo $(tput setaf 6)${*}$(tput sgr0)
		;;
	magenta)
		shift 1
		echo $(tput setaf 5)${*}$(tput sgr0)
		;;
	white)
		shift 1
		echo $(tput setaf 7)${*}$(tput sgr0)
		;;
	underline)
		#yes i know its not a color, its still usefull though.
		shift 1
		echo $(tput setaf smul)${*}$(tput sgr0)
		;;
	custom)
		color_code=${2}
		shift 2
		echo $(tput setaf ${color_code})${*}$(tput sgr0)
		;;
	ls-color-codes) #this outputs a 16x16 grid of tput codes
		for i in $(seq 0 256); do
		tput setaf ${i}
		printf " %3s" "$i"
		tput sgr0
		if [ $((($i + 1) % 16)) == 0 ] ; then
			echo #New line
		fi
		done
		;;
	*)
		script_name=$(basename ${0})
		cat <<USAGE
${script_name}
This script will echo your text as a specified color.

  Usage:
    ${script_name} <black|red|green|yellow|blue|cyan|magenta|white|underline> <text>
    ${script_name} custom <tput_color_code> <text>
    ${script_name} ls-color-codes

  custom <tput_color_code> <text> - This will output the color in the custom color
                                    code recognized by tput.
  ls-color-codes                  - This will output the color codes recognized by
                                    tput. Use this for the code for the "custom" arg

USAGE
	esac
}

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
