#!/bin/sh
#SBATCH  --job-name=vasp_job
#SBATCH  --output=log.out.%j
#SBATCH  --error=log.err.%j
#SBATCH  --partition=normal
#SBATCH  --nodes=1
#SBATCH  --ntasks=16
##SBATCH  --time=1000:00:00
#SBATCH  --ntasks-per-node=16

source /public/env/mpi_intelmpi-2021.3.0.sh
source /public/env/compiler_intel-compiler-2021.3.0.sh
EXEC_std=/public/software/apps/vasp/intelmpi/5.4.4/bin/vasp_std
IFS=$'\n'
#for line in `cat iter.txt`
#do
#        pnum=$line
#done
pnumb=0
bef=0.00
pstress=0.001
store=0.00
cat direct >> pos
cp pos POSCAR
mpirun -n 16 $EXEC_std  > vasp.log 2>&1
 #初始结构优化
cp CONTCAR CONTCAR_0
cp OUTCAR OUTCAR_0
#./poscar_gene_shear.pl  #施加应变
#前疏后密
#1+det的n次方 
for a in $(seq 1 60) 
do
 ./poscar_gene.pl   #施加应变
 mpirun -n 16 ./vasp5.3_s > vasp.log 2>&1 #计算应力
 cp OUTCAR OUTCAR_$a  #保留应力信息
 cp CONTCAR CONTCAR_$a  #保留应变后的结果
 P=`awk '/in kB /{ print $8 }' OUTCAR_$a |tail -1`
 x=$(printf "%.5f" `echo "scale=5;$P " |bc`)
 if [[ `echo "$x >= $store" |bc` -eq 1 ]]   #判断结果是否出现负值
 then
        w=$(printf "%.3f" `echo "scale=3;$a *0.01" |bc`)
        echo -e "$w \t 0" >> tmp_${pnumb}.dat
        break
 else
        if [[ `echo "$x <= $bef" |bc` -eq 1 ]] #判断是否到达峰值
        then
 		j=$(printf "%.3f" `echo "scale=3;$a *0.01" |bc`)
        	p=$(printf "%.5f" `echo "($x) *-0.1"|bc`)
        
        	echo -e "$j \t $p" >> tmp_${pnumb}.dat
#        	./poscar_gene_shear.pl  #施加应变，计算下一个应变点
        	bef=$x       
        else
        	break
        fi
 fi
done
#./poscar_gene_more.pl
#for a in $(seq 1 30)
#do
# mpirun -n 64 ./vasp5.3_t > vasp.log 2>&1 #计算应力
# b=$(printf "%d" `echo "($a) +2"|bc`)
# cp OUTCAR OUTCAR_$b  #保留应力信息
# cp CONTCAR CONTCAR_$b  #保留应变后的结果
# P=`awk '/in kB /{ print $5 }' OUTCAR_$b |tail -1`
# x=$(printf "%.5f" `echo "scale=5;$P " |bc`)
# if [[ `echo "$x >= $store" |bc` -eq 1 ]]   #判断结果是否出现负值
# then
#        break
# else
#        if [[ `echo "$x <= $bef" |bc` -eq 1 ]] #判断是否到达峰值
#        then
#                j=$(printf "%.3f" `echo "scale=3;0.1+$a *0.02" |bc`)
#                p=$(printf "%.5f" `echo "($x) *-0.1"|bc`)
#
#                echo -e "$j \t $p" >> tmp_${pnumb}.dat
#                ./poscar_gene_more.pl  #施加应变，计算下一个应变点
#                bef=$x
#        else
#                break
#        fi
# fi
#done
cp ./tmp_${pnumb}.dat ./tmp.dat
rm tmp_${pnumb}.dat
echo -e "$pnumb" >> ../../watch.txt


 
