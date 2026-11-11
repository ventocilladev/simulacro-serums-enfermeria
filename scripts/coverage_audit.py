"""Manual mapping of all 92 headings in the supplied SERUMS 2026-II outline.

Each number is an independently authored focal concept from the source bank.
The advanced bank must contain every mapped concept at least once.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = {
    'SP1': [0,4,50,51,117,10,7,115,9,55,128,129,136],
    'SP2': [18,147,3,14,16,162,62,67,20,58,59,22,66,17],
    'SP3': [2,63,61,23],
    'CI1': [28,139,24,76,70],
    'CI2': [74,190,29,77,227,78,31,143,154,34,32,81,256,270,83,103,179,185,199,102,232,239,241],
    'ET1': [37,258,36],
    'ET2': [38,39,261,86,87,266],
    'IN1': [267,40,91],
    'IN2': [42,92],
    'IN3': [280,93],
    'GE1': [123,46,44],
    'GE2': [94,48,95,254,106,96,97],
    'GE3': [49,47,162,121,122],
    'GE4': [98,298],
}
EXPECTED = {'SP1':13,'SP2':14,'SP3':4,'CI1':5,'CI2':23,'ET1':3,'ET2':6,
            'IN1':3,'IN2':2,'IN3':2,'GE1':3,'GE2':7,'GE3':5,'GE4':2}
assert {key:len(value) for key,value in MAPPING.items()} == EXPECTED
assert sum(map(len,MAPPING.values())) == 92
payload = (ROOT / 'questions-master.js').read_text(encoding='utf-8')
questions = json.loads(payload.removeprefix('window.QUESTIONS = ').removesuffix(';\n'))
focal = {q[5] for q in questions}
missing = [(block, index+1, concept) for block, concepts in MAPPING.items()
           for index, concept in enumerate(concepts) if concept not in focal]
assert not missing, missing
assert len(questions) == 1000
print('92/92 syllabus headings represented in the 1000-question bank')
