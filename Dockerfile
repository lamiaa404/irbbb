FROM webis/tira-ir-datasets-starter:0.0.54

COPY ir_anthology.py /Users/lh/Documents/Projects/irbbb/

ENTRYPOINT [ "/irds_cli.sh" ]
