import os

# os.system("export TRAIN_DATASET=SQuAD1-1")
os.system('beaker experiment create --expand-vars -f training_config.yaml')
# ,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD2-0,ComQA,DROP,HotpotQA


