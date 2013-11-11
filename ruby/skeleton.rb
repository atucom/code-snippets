#!/bin/env ruby
#Ruby command line skeleton file
#@atucom


#check if the proper gems are installed
  [ 'rubygems','optparse' ].each {|required_gem| 
    begin
      require required_gem
    rescue LoadError
      puts "You need to install the #{required_gem} gem to use this script"
      exit
    end
  }
#parse command line options
x=nil
options = {} #hash that hold the options
o=OptionParser.new do |opts|
   opts.banner = "Usage: #{$0} [options] ..." #the banner to display at the top
   optparse = OptionParser.new do|opts| #start defining options below
   opts.on( '-u', '--user USERNAME', 'The username to login with' ) {|i| options[:username] = i}
   opts.on( '-p', '--password PASSWORD', 'The password to login with. 
                                     leave blank for interactive' ) {|i| options[:password] = i}
   opts.on( '-r', '--report REPORTNAME', 'The report to download' ) {|i| options[:report] = i}
   opts.on( '-h', '--help', 'Display this screen' ) {puts opts; exit}
   x=opts
  end.parse!(ARGV)
end
#if username argument is not specified, then output help screen and exit
if options[:username].nil?
 puts x
 exit
end