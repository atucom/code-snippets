require 'optparse' #command line options parser
options = {} #hash that hold the options
optparse = OptionParser.new do|opts|
   opts.banner = "Usage: #{$0} [options] ..." #the banner to display at the top
   optparse = OptionParser.new do|opts| #start defining options below
   options[:username] = nil
   opts.on( '-u', '--user USERNAME', 'The SMB User to login as' ) do|user|
     options[:username] = user
   end
   options[:password] = nil
   opts.on( '-p', '--password PASSWORD', 'The SMB Password to login as' ) do|password|
     options[:password] = password
   end
   options[:ipaddr] = nil
   opts.on( '-t', '--target IPADDRESS', 'The remote host to lob everything at' ) do|ipaddr|
     options[:ipaddr] = ipaddr
   end
   # This displays the help screen, all programs are
   # assumed to have this option.
   opts.on( '-h', '--help', 'Display this screen' ) do
     puts opts
   end
 end.parse!(ARGV)

