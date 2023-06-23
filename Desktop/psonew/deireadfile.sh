#!/bin/sh
for line in `cat readfile.txt`
do
        w=$line
done
for line in `cat deireadfile.txt`
do 
        a=$line
done
cp ./particle_${w}/${a}/tmp.dat ./
