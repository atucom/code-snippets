
#if they supply -h,--help, no args, or if arg1 is not a file
if [[ "$1" = '-h' ]] || [[ "$1" = '--help' ]] || [[ -z "$1" ]] || [[ ! -f "$1" ]]; then
  echo "Specify a n input file for WHATEVERCOMMAND"
  echo "This tool runs some stuff and does other useful stuff for stuff reasons"
  echo "Usage: $0 <targetfile>"
  echo "Example: $0 'ranges.provided'"
  exit 1
else
  inputfile="$1"
  <MYCOMMAND GOES HERE>
fi