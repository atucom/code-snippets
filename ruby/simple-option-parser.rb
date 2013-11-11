#its better to use the actual option parser gem versus doing it yourself like this

if ARGV.empty?
    puts "This script does ZOMG MAGIC"
    puts "\t Usage: #{$0} file1.xml file2.xml file3.xml ... "
else
    ARGV.each do |blah|
        AMAZING_MAGIC(blah)
    end
end