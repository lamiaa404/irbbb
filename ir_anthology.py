import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset

DATASET_URL = 'https://github.com/lamiaa404/irbbb'

class AnthologyDocument(NamedTuple):
    doc_id: str
    text: str
    
    def default_text(self):
        return self.text

ir_datasets.registry.register('iranthology-irbbb', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'ir_anthology.jsonl')], expected_md5='f574d99c0dd0724b05f18df680a9a48d'),doc_cls=AnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'ir_anthology_topics.xml')], expected_md5='b12f4c4361c3c0be0562e214b06038c4'), lang='en')
))
