#!/bin/bash
#this code takes the arguments supplied at runtime and sources them as variables
#it is expected that the user supplies the proper variables (duh)

#DEFAULTS
var1="wut"
var2="lol"
var3='meep'

cat <<KITTY
This is whats currently configured:
var1=${var1} #this is var1
var2=${var2} #this is var2
KITTY

#for every argument, parse the halves for comparison to existing vars
for i in ${BASH_ARGV[@]}; do
    echo $i
    half1=$(echo $i | cut -d'=' -f1)
    half2=$(echo $i | cut -d'=' -f2)
    
done
  #if grep $(echo $i | cut -d'=' -f1) <(echo )






#take in ARGV as an array
#compare every entry of the array to variables that already exist
#if var exists, replace it
#else echo "you supplied the wrong var"
#	exit
#fi

###NOT COMPLETE
# declare -A variables #associative arrays only work on bash v4

# variable[asd]= #example of assoc array
# variable[qwe]=


# echo zero:${BASH_ARGV[0]}
# echo one: ${BASH_ARGV[1]}
# echo all: ${BASH_ARGV[@]}

# for i in `${BASH_ARGV[@]}`; do
# 	if grep $(echo $i | cut -d'=' -f1) <(echo )