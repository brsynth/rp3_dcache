"""
Handful methods... .. .
"""

import os
import yaml
from rdkit.Chem import MolFromSmiles, MolFromInchi, AddHs


def default_config():
    """
    Return the default configuration as a dictionnary.
    """
    path = os.path.join(os.path.dirname(__file__), "conf", "default.yaml")
    with open(path, 'r') as fh:
        cfg = yaml.load(fh, Loader=yaml.Loader)
    return cfg


def make_document_id(rule_id, substrate_id):
    """
    Generate a document ID
    """
    return rule_id + "_" + substrate_id


def as_document(rule_id, substrate_id, list_list_inchikeys=[], list_list_inchis=[], list_list_smiles=[],
                list_stoechiometry=[]):
    """
    Format data to be inserted into the cache DB.

    Targeted DB is Mongo.

    :param  rule_id:                unique ID for the rule
    :param  substrate_id:           unique ID for the substrate
    :param  list_list_inchikeys:    list of list of InchiKeys
    :param  list_list_inchis:       list of list of Inchis
    :param  list_list_smiles:       list of list of SMILES
    :param  list_stoechiometry:     list of dict of stoechiometric coefficients
    :return document: ready-to-be-inserted document
    """
    return {
        "_id": make_document_id(rule_id, substrate_id),
        "rule_id": rule_id,
        "substrate_id": substrate_id,
        "list_list_inchikeys": list_list_inchikeys,
        "list_list_inchis": list_list_inchis,
        "list_list_smiles": list_list_smiles,
        "list_stoechiometry": list_stoechiometry
    }


def rdmols_from_document(document, build_from="inchi", add_hs=True):
    """
    Convert back a document to a set of rdmols. This method is a companion of "as_document".

    :param document: a document produced by the "as_mongo_document" method, dict
    :param build_from: the type of depiction to be used to build back the rdmols, str in ["inchi", "smiles"]
    :param add_hs: add Hs to RDKit mol object, default is True
    :returns list_list_rdmols: list of list of rdmols
    """
    assert build_from in ["inchi", "smiles"]
    assert add_hs in [True, False]

    list_list_rdmols = list()
    list_stoechiometry = document['list_stoechiometry']
    if build_from == 'inchi':
        for list_inchis in document['list_list_inchis']:
            list_rdmols = list()
            for inchi in list_inchis:
                rd_mol = MolFromInchi(inchi, sanitize=True)
                if add_hs:
                    rd_mol = AddHs(rd_mol)
                list_rdmols.append(rd_mol)
            list_list_rdmols.append(list_rdmols)
    elif build_from == 'smiles':
        for list_smiles in document['list_list_smiles']:
            list_rdmols = list()
            for smiles in list_smiles:
                rd_mol = MolFromSmiles(smiles, sanitize=True)
                if add_hs:
                    rd_mol = AddHs(rd_mol)
                list_rdmols.append(rd_mol)
            list_list_rdmols.append(list_rdmols)
    else:
        raise NotImplementedError()

    return list_list_rdmols, list_stoechiometry
