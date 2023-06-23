#!/bin/sh
for line in `cat sbatch.txt`
do
        y=$line
done
for line in `cat deisbatch.txt`
do
        a=$line
done
cp ./pos ./particle_${y}/${a}
cp ./iter.txt ./particle_${y}/${a}
cd ./particle_${y}/${a}
sbatch deislurm.sh
cd ../..
