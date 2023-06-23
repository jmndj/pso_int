#!/bin/sh
for line in `cat sbatch.txt`
do
        y=$line
done
cp ./pos ./particle_${y}
cp ./iter.txt ./particle_${y}
cd ./particle_${y}
sbatch slurm.sh
cd ..
