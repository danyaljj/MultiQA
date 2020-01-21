
# python multiqa.py train --datasets SQuAD1-1  --cuda_device 0,1

# newsqa 
# python multiqa.py train --datasets NewsQA  --cuda_device 0,1
# python multiqa.py train --datasets SQuAD1-1,NewsQA  --cuda_device 0,1

# searchqa 
# python multiqa.py train --datasets SearchQA  --cuda_device 0,1
# python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA  --cuda_device 0,1


# TriviaQA_wiki (05/17)
# python multiqa.py train --datasets TriviaQA_wiki  --cuda_device 0,1
# python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki  --cuda_device 0,1


# WikiHop (10/17)
# python multiqa.py train --datasets WikiHop  --cuda_device 0,1
# python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop  --cuda_device 0,1

# ComplexWebQuestions (03/18)
# python multiqa.py train --datasets ComplexWebQuestions  --cuda_device 0,1
# python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions  --cuda_device 0,1


# DuoRC_Paraphrase (04/18)
python multiqa.py train --datasets DuoRC_Paraphrase  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase  --cuda_device 0,1


# SQuAD-2.0 (06/18)
python multiqa.py train --datasets SQuAD-2.0  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0  --cuda_device 0,1


# ComQA (09/18)
python multiqa.py train --datasets ComQA  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0,ComQA  --cuda_device 0,1


# DROP (03/19)
python multiqa.py train --datasets DROP  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0,ComQA,DROP  --cuda_device 0,1


# HotpotQA (09/18)
python multiqa.py train --datasets HotpotQA  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0,ComQA,DROP,HotpotQA  --cuda_device 0,1


# Natural Questions (?/19)
python multiqa.py train --datasets NaturalQuestions  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0,ComQA,DROP,HotpotQA,NaturalQuestions  --cuda_device 0,1

# BoolQ (05/19)
python multiqa.py train --datasets BoolQ  --cuda_device 0,1
python multiqa.py train --datasets SQuAD1-1,NewsQA,SearchQA,TriviaQA_wiki,WikiHop,ComplexWebQuestions,DuoRC_Paraphrase,SQuAD-2.0,ComQA,DROP,HotpotQA,NaturalQuestions,BoolQ  --cuda_device 0,1
