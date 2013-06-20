#simple little function to check if the previous command completed or not
#usage: "ping -c1 google.com; check"
check(){
  if [ $? == 0 ];
    then echo "COMPLETE"
    else echo "FAILED"
  fi
};