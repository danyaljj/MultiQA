import json
import os
import sys
import subprocess


def main():
    other_options = ""
    if len(sys.argv) > 3:
        other_options = " ".join(sys.argv[3:])

    # first, train models with different hyperparameters
    for batch_size in [16, 32]:
        for num_epochs in [3, 4]:
            for lr in [0.00002, 0.00003, 0.00005]:
    # lr = 0.00002
    # num_epochs = 3
    # batch_size = 16
                command = f"python multiqa.py train --datasets {sys.argv[1]} --batch_size {batch_size} --num_epochs {num_epochs} --lr {lr} {other_options}"
                print(f" >>>>>>> Training with command {command}")
                os.system(command)
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                process.communicate()
                if process.returncode:
                    raise Exception('program returned error code {0}'.format(process.returncode))

    # choose the best model
    top_model = ""
    top_score = -1
    subfolders = [f.path for f in os.scandir("models/") if f.is_dir()]
    for folder in subfolders:
        if "batch_size" not in folder:
            continue
        print(f" >>>>> reading from folder: {folder}")
        with open(f"{folder}/metrics.json") as f:
            metrics = json.load(f)
            if metrics['validation_f1'] > top_score:
                top_model = folder
                top_score = metrics['validation_f1']

    print(f" >>>>>>> top model: {top_model} with score {top_score}")

    # evaluate the best model on all the datasets
    # --data_dir /Users/danielk/ideaProjects/MultiQA/samples/
    # command = f"python multiqa.py evaluate --model model --datasets {sys.argv[2]} --models_dir {top_model}/  {other_options}"
    # print(f" >>>>>>> evaluating with command: {command}")
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # process.communicate()
    # if process.returncode:
    #     print(process.stderr)
    #     print(process.stdout)
    #     raise Exception('program returned error code {0}'.format(process.returncode))

    evaluation_datasets = sys.argv[2]
    for eval_dataset in evaluation_datasets.split(","):
        command = f"python multiqa.py evaluate --model model --datasets {eval_dataset} --models_dir {top_model}/  {other_options}"
        print(f" >>>>>>> evaluating with command: {command}")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process.communicate()
        if process.returncode:
            print(process.stderr)
            print(process.stdout)
            raise Exception('program returned error code {0}'.format(process.returncode))

    # collect the results in a file
    print(f" >>>>>>> collecting the numbers")
    output_metrics = {
        "selected_validation_f1": top_score,
        "selected_model_name": top_model
    }
    for filename in os.listdir("results/eval"):
        if filename.endswith(".json"):
            dataset = "_".join(filename.split("_")[3:]).replace(".json", "") + "-"
            with open(f"results/eval/{filename}") as f:
                metrics = json.load(f)
                output_metrics[dataset + 'EM'] = metrics['EM']
                output_metrics[dataset + 'f1'] = metrics['f1']
                output_metrics[dataset + 'loss'] = metrics['loss']


    with open('/output/metrics.json', 'w') as f:
        json.dump(output_metrics, f)

    command = f"ls -lha"
    os.system(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    process.communicate()

    command = f"ls -lha /output/"
    os.system(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    process.communicate()

    with open("/output/metrics.json", 'r') as fin:
        print(fin.read())

if __name__ == "__main__":
    main()
