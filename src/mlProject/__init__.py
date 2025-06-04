"""Lets say you deployeed your project in cloud plaftform you get any termina for you to monitor the code so we
     we  creatre the loging file so we check the eroor
     """
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #simple logging string consits that show sdci time and level like info leve or bug level and then it show mdule and messge

log_dir = "logs" # create log folder
log_filepath = os.path.join(log_dir,"running_logs.log") # isnisde thsat folder it will create runinng.log
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # it will create log folder insdie that it wll save all the logginf
        logging.StreamHandler(sys.stdout) #print my log in my terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")