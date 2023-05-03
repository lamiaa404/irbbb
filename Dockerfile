FROM webis/tira-ir-datasets-starter:0.0.54

COPY iranthology-irbbb.jsonl  ir_anthology.py  ir_anthology_topics.xml  irbbb.ipynb /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]
