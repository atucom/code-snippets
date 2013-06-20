#/bin/bash
#this file contains the template function for error checking and reporting in scripts
#this allows you to not have to worry about any external functions or their nuances.
#2012 - Atucom

errorcode(){
	#this function checks for error status and reports the description
  if [ $1 == "" ]; then
    echo "You didnt specify an error code for this code section"
  fi
  case $1 in
    1)
      echo "you are missing the necessary binaries in \$PATH"
      ;;
    2)
      echo "this file does not exist"
      ;;
    *)
      echo "${1} is not a known error code"
      ;;
  esac
exit
}

#USAGE:
#if [ ! -f $file ]; then
#	errornum "2"
#fi

#errorcode "$1"