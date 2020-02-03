import os

os.system("export export TRAIN_DATASET=SQuAD1-1")
os.system('beaker experiment create --expand-vars -f training_config.yaml')
# ,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD2-0,ComQA,DROP,HotpotQA,NaturalQuestions



