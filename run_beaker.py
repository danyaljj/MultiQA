import os

# os.system("export TRAIN_DATASET=SQuAD1-1")
os.system('beaker experiment create --expand-vars -f training_config.yaml')



