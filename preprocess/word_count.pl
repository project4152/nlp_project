#!/usr/bin/perl
# word-ngrams-f.pl

$n = 1;

while (<>) {
  while (/'?[a-zA-Z]+/g) {
     push @ng, lc($&); shift @ng if scalar(@ng) > $n;
     &collect(@ng) if scalar(@ng) == $n;
  }
}

sub collect {
  my $ng = "@_";
  $f{$ng}++; ++$tot;
}


print "Total $n-grams: $tot\n";

my $filename = 'words.txt';
open (my $fh, '>', $filename) or die "Could not open file '$filename' $!";


for (sort { $f{$b} <=> $f{$a} } keys %f) {
  print $fh sprintf("%5d %lf %s\n",
                $f{$_}, $f{$_}/$tot, $_);
}
close $fh;
print "done\n";


