##!/bin/sh 
##SBATCH  --job-name=vasp_job    ###任务名，可自行更改###
##SBATCH  --output=log.out.%j    ###作业运行输出文件###
##SBATCH  --error=log.err.%j     ###作业报错输出文件###
##SBATCH  --partition=liquan    ###任务队列，按分配队列更改###
##SBATCH  --nodes=1              ###任务节点数，根据使用节点数修改###
##SBATCH  --ntasks-per-node=12  ###每个节点内使用的核数###
##SBATCH  --nodelist=c1101      ###指定节点提交任务
##SBATCH  --exclusive            ###资源是否独占，不独占需注释此项

###source /public1/soft/modules/module.sh
###module load anaconda/3-2020.11
##source activate /work/home/sxq/miniconda3/envs/my_pymatgen 
python -u iiintpso_shear.py
