
$input =$ARGV[0];
$output=$ARGV[1];

open(IN,  $input)  or die("Could not open  file.");

my $host = 0;
my $pull = 0;

foreach $line (<IN>)  {   
    chomp $line;    
    if ($line =~ /processing/){
		if($line =~ /(from host)/){
			$host += 1;
		} else {
			$pull += 1;
		}
    }
}
close(IN);

#open(OUT, '>', $output) or die("Could not open  file.");
print "$host $pull\n";
#close(OUT);

