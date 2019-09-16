import pytest
from rdkit.Chem import Mol
from hashlib import sha1
from rp3_dcache.Utils import default_config, make_document_id, as_document, rdmols_from_document


def test_config_1():    
    cfg = default_config()
    assert cfg['db']


def test_make_document_id():
    doc_id = make_document_id("rid", "sid")
    assert isinstance(doc_id, str)


def test_as_document():
    document = as_document(rule_id="rid", substrate_id="sid", list_list_inchikeys=[], list_list_inchis=[],
                           list_list_smiles=[], list_stoechiometry=[])
    assert sha1(str(document).encode()).hexdigest() == '893f1a213b6d60ea4d2b796c55fbfe3475bdeb8d'


def test_rdmols_from_document():
    document = {
        "_id": "RR-01-1a456abbc0d8-12-F_OENHQHLEOONYIE-UHFFFAOYSA-N",
        "rule_id": "RR-01-1a456abbc0d8-12-F",
        "substrate_id": "OENHQHLEOONYIE-UHFFFAOYSA-N",
        "list_list_inchikeys": [
            [
                "HRQKOYFGHJYEFS-UHFFFAOYSA-N"
            ]
        ],
        "list_list_inchis": [
            [
                "InChI=1S/C40H56/c1-32(2)18-13-21-35(5)24-15-26-36(6)25-14-22-33(3)19-11-12-20-34(4)23-16-27-37(7)29-30-39-38(8)28-17-31-40(39,9)10/h11-12,14-16,18-20,22-27,29-30H,13,17,21,28,31H2,1-10H3"
            ]
        ],
        "list_list_smiles": [
            [
                "[H]C(=C([H])C([H])=C(C([H])=C([H])C([H])=C(C([H])=C([H])C1=C(C([H])([H])[H])C([H])([H])C([H])([H])C([H])([H])C1(C([H])([H])[H])C([H])([H])[H])C([H])([H])[H])C([H])([H])[H])C([H])=C(C([H])=C([H])C([H])=C(C([H])=C([H])C([H])=C(C([H])([H])[H])C([H])([H])C([H])([H])C([H])=C(C([H])([H])[H])C([H])([H])[H])C([H])([H])[H])C([H])([H])[H]"
            ]
        ],
        "list_stoechiometry": [
            {
                "HRQKOYFGHJYEFS-UHFFFAOYSA-N": 1
            }
        ]
    }
    rdmols, coefficients = rdmols_from_document(document)
    assert rdmols is not None
    assert len(rdmols) == 1
    assert len(rdmols[0]) == 1
    assert isinstance(rdmols[0][0], Mol)
