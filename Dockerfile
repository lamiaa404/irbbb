FROM webis/tira-ir-datasets-starter:0.0.54

COPY ir_anthology.py 

ENTRYPOINT [ "/irds_cli.sh" ]
