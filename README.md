# slurm_tasks

## to do list:
1. set in send_to_slurm.py your log directory path.
2. set in config.ymal your task parameter and a command to run.

The python script will create a new directory for the run under your LOG_BASE_DIR(set in send_to_slurm.py) and send a new slurm task. The path to the log directory will be sent as a command line argument.
