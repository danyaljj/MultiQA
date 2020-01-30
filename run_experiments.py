import json
import os
import sys

def main():
    other_options = ""
    if len(sys.argv) > 3:
        other_options = " ".join(sys.argv[3:])


    # first, train models with different hyperparameters
    for batch_size in [16,32]:
        for num_epochs in [3,4]:
            for lr in [0.00002,0.00003,0.00005]:
                command = f"python multiqa.py train --datasets {sys.argv[1]} --batch_size {batch_size} --num_epochs {num_epochs} --lr {lr} {other_options}"
                print(command)
                os.system(command)


    # choose the best model
    top_model = ""
    top_score = -1
    for folder in os.walk("models/"):
        with open(f"models/{folder}/metrics.json") as f:
            metrics = json.load(f)
            if metrics['validation_f1'] > top_score:
                top_model = folder
                top_score = metrics['validation_f1']

    print(f" >>>> top model: {top_model} with score {top_score}")


    # evaluate the best model on all the datasets
    command = f"python multiqa.py evaluate --model model --datasets {sys.argv[2]} --models_dir  'models/{top_model}/' {other_options}"
    print(command)
    os.system(command)

    # collect the results in a file
    output_metrics = {
        "selected_validation_f1": top_score,
        "selected_model_name": top_model
    }
    for filename in os.listdir("results/eval"):
        if filename.endswith(".json"):
            dataset = "_".join(filename.split("_")[3:])
            with open(f"results/eval/{filename}") as f:
                metrics = json.load(f)
                output_metrics[dataset + 'EM'] = metrics['EM']
                output_metrics[dataset + 'f1'] = metrics['f1']
                output_metrics[dataset + 'loss'] = metrics['loss']

    with open('metrics.json', 'w') as f:
        json.dump(output_metrics, f)

if __name__ == "__main__":
    main()

