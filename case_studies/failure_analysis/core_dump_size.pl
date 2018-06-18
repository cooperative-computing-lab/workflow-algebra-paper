
use Number::Bytes::Human qw(parse_bytes);

$input =$ARGV[0];
$output=$ARGV[1];
$limit =$ARGV[2];

open(IN,  $input)  or die("Could not open  file.");

my $segf = 0;
my $core = 0;
my $stac = 0;

foreach $line (<IN>)  {   
    chomp $line;    
	my @line = split ' ', $line;
    if ($line[8] =~ /core.*/){
		$segf += 1;
		$core += parse_bytes($line[4]);
    } elsif ($line[8] =~ /div_by_0_\S*st/){
		$stac += $line[4];
    }
}
close(IN);

open(OUT, '>', $output) or die("Could not open  file.");
print OUT "$limit $segf $core $stac\n";
close(OUT);

