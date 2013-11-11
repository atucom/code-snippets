#this code iterates over the gems you mention, tries to load each one, and errors out if it cant.
#this takes the place of the normal "require blahgem"

  [ 'rubygems','optparse' ].each {|required_gem| 
    begin
      require required_gem
    rescue LoadError
      puts "You need to install the #{required_gem} gem to use this script"
      exit
    end
  }