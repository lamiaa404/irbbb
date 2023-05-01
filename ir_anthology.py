import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.datasets.base import Dataset

class AnthologyDocument(NamedTuple):
    doc_id: str
    text: str
    
    def default_text(self):
        return str(self.text)

ir_datasets.registry.register('iranthology-irbbb', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir_anthology.jsonl'), doc_cls=AnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir_anthology_topics.xml'), lang='en')
))
