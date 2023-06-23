#!/bin/sh
for line in `cat dir.txt`
do
        y=$line
done
mkdir particle_${y}
cp ./KPOINTS ./particle_${y}
cp ./POTCAR ./particle_${y}
cp ./INCAR ./particle_${y}
cp ./direct ./particle_${y}
cp ./poscar_gene.pl ./particle_${y}
#cp ./poscar_gene_more.pl ./particle_${y}
cp ./vasp5.3_s ./particle_${y}
cp ./slurm.sh ./particle_${y}
for a in $(seq 0 5)
do
  cp -r ${a} particle_${y}
  cp ./KPOINTS ./particle_${y}/${a}
  cp ./POTCAR ./particle_${y}/${a}
  cp ./INCAR ./particle_${y}/${a}
  cp ./direct ./particle_${y}/${a}
  cp ./poscar_gene.pl ./particle_${y}/${a}
  cp ./vasp5.3_s ./particle_${y}/${a}
  cp ./deislurm.sh ./particle_${y}/${a}
done
