import os
import yaml
from datetime import datetime

# The scratch directory is not limited in quota
LOG_DIR_BASE_PATH = "/vol/scratch/CONTINUE_WITH_YOUR_PATH"

if __name__ == "__main__":
    with open("config.yaml", 'r') as fp:
        config = yaml.safe_load(fp)
    slurm_config = config['slurm_params']
    sbatch_command = 'sbatch'
    logdir = f"{LOG_DIR_BASE_PATH}/{config['run_name']}_transcriber-{datetime.now().strftime('%y%m%d-%H%M%S')}" # ckpts and midi will be saved here
    config['logdir'] = logdir
    slurm_config['output'] = os.path.join(logdir, slurm_config['output'])
    slurm_config['error'] = os.path.join(logdir, slurm_config['error'])
    os.makedirs(logdir, exist_ok=True)
    with open(os.path.join(logdir, 'run_config.yaml'), 'w') as fp:
        yaml.dump(config, fp)
    
    for param in slurm_config:
        sbatch_command += f' --{param}={slurm_config[param]}'
    sbatch_command += f" {config['command']} {logdir}"
    os.system(sbatch_command)
    