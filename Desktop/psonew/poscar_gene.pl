#! /usr/bin/perl

use strict;

open (IN,"CONTCAR");
open (OUT,">POSCAR");

my $det = 0.01;   # strain of a step
#shear
my @deformation = (     [1,0,0],
                        [0,1,0],
                        [$det,0,1]);
#tensile
#my @deformation = (     [1,0,0],
#                        [0,1,0],
#                       [0,0,1+$det]);

my (@abc,@next_abc);
my $count = 0;

while(<IN>){
    $count++;
    if($count>=3 && $count<=5){
	my @tmp = split;
	push @abc, [@tmp];
    }
    elsif($count==6){
	@next_abc = &multiply(\@abc,\@deformation);
	for my $i(0..$#next_abc){
	    for (0..$#{$next_abc[$i]}){
		printf OUT "\t%12.9f",$next_abc[$i][$_];
	    }
	    printf OUT "\n";
	}
	printf OUT "$_";
    }
    else{
	printf OUT "$_";
    }
}

sub multiply{
    my ($m,$n)=@_;
    my @product;
    my ($n1,$n2,$n3,$n4) = ($#$m,$#{$m->[0]},$#$n,$#{$n->[0]});
    if($n2!=$n3){die "Can't do the multiply";}
    else{
        for my $i(0..$n1){
            for my $j(0..$n4){
                for my $k(0..$n2){
                    $product[$i][$j] += ($m->[$i][$k]*$n->[$k][$j]);
                }
            }
        }
    }
    @product;
}
