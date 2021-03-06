#! /bin/bash

#SBATCH --job-name=C9kl64h
#SBATCH --partition=batch
#SBATCH --gres=gpu:1
#SBATCH --time=3-00:00:00
#SBATCH --mail-type=end
#SBATCH --mail-user=joshua.arnold1@uq.net.au

JOBNAME="C9kl64h"

module load tensorflow
ARGS="--error=$JOBNAME.err --output=$JOBNAME.out"
srun --gres=gpu:1 -n1 $ARGS python batchNetRun.py > $JOBNAME.log
mv "$JOBNAME".* "$JOBNAME"_batch_results/

wait
