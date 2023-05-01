# irbbb
information retrieval project 

## Build the image

```
docker build -t registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-irbbb/iranthology:0.0.1 .
```

# Test that dataset creation works

```
tira-run \
    --output-directory ${PWD}/iranthology-dataset-tira \
    --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-irbbb/iranthology:0.0.1 \
    --allow-network true \
    --command '/irds_cli.sh --ir_datasets_id iranthology-irbbb --output_dataset_path $outputDir'
```

# Test that retrieval works

```
tira-run \
    --input-directory ${PWD}/iranthology-dataset-tira \
    --image webis/tira-ir-starter-pyterrier:0.0.1-base \
    --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/full-rank-pipeline.ipynb'
```
