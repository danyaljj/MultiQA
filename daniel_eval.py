models = ['SQuAD1-1', 'NewsQA', 'SearchQA', 'TriviaQA_wiki', 'WikiHop', 'ComplexWebQuestions', 'DuoRC']

import subprocess

for i, train_m in enumerate(models): 
	for j, eval_m in enumerate(models): 
		# print(" * * * * * * * * * * * ")
		# command = f"python multiqa.py evaluate --model model --datasets {eval_m} --cuda_device 0  --models_dir  '/net/nfs.corp/aristo/danielk/MultiQA/models/{train_m}/'"
		# outfile_name=f'eval_train:{train_m}_eval:{eval_m}.txt'
		# print(command)
		# process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.STDOUT, shell = True)

		# file = open(outfile_name, "w")
		# for line in process.stdout:
		# 	file.write(line.decode('utf-8'))
		# process.wait()
		# file.close()


		if i == 0: 
			continue 
		print(" * * * * * * * * * * * ")
		extended_train_models = "_".join(models[:i+1])
		command = f"python multiqa.py evaluate --model model --datasets {eval_m} --cuda_device 0  --models_dir  '/net/nfs.corp/aristo/danielk/MultiQA/models/{extended_train_models}/' "
		outfile_name=f'eval_train:{extended_train_models}_eval:{eval_m}.txt'
		print(command)
		print(outfile_name)
		# with open(outfile_name, "w") as outfile:
		# 	subprocess.call(command, stdout=outfile, shell=True)
		process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.STDOUT, shell = True)
		# (process_output,  error) = process.communicate()
		file = open(outfile_name, "w")
		# file.write(str(process_output))
		for line in process.stdout:
			file.write(line.decode('utf-8'))
		process.wait()
		file.close()

