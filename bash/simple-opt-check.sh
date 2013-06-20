#Super simple quick opt checker to make sure all options are specified.
#It's better to use the more complete version, but this is good for quick hacks


if [[ -z $1 ]] || [[ -z $2 ]] || [[ -z $3 ]] || [[ -z $4 ]] || [[ -z $5 ]]; then
    echo 'This command does blah blah'
    echo 'This command also does blah blah'
    echo "Usage: $0 opt1 opt2 opt3 opt4 opt5"
else
    ./MY-COMMAND-HERE $1 $2 $3 $3
fi
