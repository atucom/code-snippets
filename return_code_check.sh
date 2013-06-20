check(){
  if [ $? == 0 ];
    then echo "COMPLETE"
    else echo "FAILED"
  fi
};