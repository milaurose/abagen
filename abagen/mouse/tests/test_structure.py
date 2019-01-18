import pytest
from ..structure import (check_structure_validity,
                         get_structure_info,
                         get_structure_coordinates)
import random
from ..io import read_all_structures

# number of tests to make
TEST_COUNT = 10
STRUCTURES_LIST_ACRONYM = read_all_structures(entry_type='acronym')
STRUCTURES_LIST_ID = read_all_structures(entry_type='id')
STRUCTURES_LIST_NAME = read_all_structures(entry_type='name')
RANDOM_STRING = 'random_string'
RANDOM_ID = 000000000

TEST_COOR_STRUCTURE_ID = 1018
COOR_ID = [(7800, 3400, 1050), (7800, 3400, 10350)]

TEST_COOR_STRUCTURE_ACRONYM = 'SSp'
COOR_ACRONYM = [(5740, 2060, 2730), (5740, 2060, 8670)]

# sample 10 structures
TEST_SAMPLES = random.sample(
    range(len(STRUCTURES_LIST_ACRONYM)), TEST_COUNT
)


def test_check_structure_validity():
    for sample in TEST_SAMPLES:
        # acronym is given
        validity, root1, root2 = check_structure_validity(
            structure_acronym=STRUCTURES_LIST_ACRONYM[sample]
        )
        assert validity is True
        # structure id is given
        validity, root1, root2 = check_structure_validity(
            structure_id=STRUCTURES_LIST_ID[sample]
        )
        assert validity is True
        # structure name is given
        # sometimes may fail as the string may contain white spaces
        # ... not recommended
        # validity, root1, root2 = check_structure_validity(
        #    structure_name=STRUCTURES_LIST_NAME[sample]
        # )
        assert validity is True

    # structure id is invalid
    validity, _, _ = check_structure_validity(
        structure_id=RANDOM_ID
    )
    assert validity is False
    validity, _, _ = check_structure_validity(
        structure_acronym=RANDOM_STRING
    )
    assert validity is False

    # exceptions
    with pytest.raises(TypeError):
        check_structure_validity()


def test_get_structure_info():
    for sample in TEST_SAMPLES:
        # single attribute
        structure_info = get_structure_info(
            structure_id=STRUCTURES_LIST_ID[sample],
            attributes='acronym'
        )
        # structure_info is str
        assert structure_info[0] == STRUCTURES_LIST_ACRONYM[sample]
        structure_info = get_structure_info(
            structure_acronym=STRUCTURES_LIST_ACRONYM[sample],
            attributes='id'
        )
        # structure_info is list of int
        # acronym is not unique
        assert STRUCTURES_LIST_ID[sample] in structure_info
        structure_info = get_structure_info(
            structure_id=STRUCTURES_LIST_ID[sample],
            attributes='name'
        )
        # structure_info is str
        assert structure_info[0] == STRUCTURES_LIST_NAME[sample]
        # no such attribute, return an empty structure_info
        structure_info = get_structure_info(
            structure_id=STRUCTURES_LIST_ID[sample],
            attributes=RANDOM_STRING
        )
        # structure_info is str
        assert not structure_info
        structure_info = get_structure_info(
            structure_acronym=STRUCTURES_LIST_ACRONYM[sample],
            attributes=RANDOM_STRING
        )
        # structure_info is str
        assert not structure_info
        # multiple attributes
        # attributes = 'all'
        structure_info = get_structure_info(
            structure_id=STRUCTURES_LIST_ID[sample],
        )
        assert structure_info['acronym'][0] == STRUCTURES_LIST_ACRONYM[sample]
        structure_info = get_structure_info(
            structure_acronym=STRUCTURES_LIST_ACRONYM[sample],
            attributes=['id', 'name', RANDOM_STRING]
        )
        assert RANDOM_STRING not in structure_info
        assert STRUCTURES_LIST_ID[sample] in structure_info['id']

    # exceptions: structure is invalid
    with pytest.raises(ValueError):
        get_structure_info(
            structure_id=RANDOM_ID
        )
    with pytest.raises(ValueError):
        get_structure_info(
            structure_acronym=RANDOM_STRING,
            attributes=['id', 'name']
        )


def test_get_structure_center():
    coor = get_structure_coordinates(
        structure_id=TEST_COOR_STRUCTURE_ID
    )
    # coor is a dict, coor[10] (right) or coor[9] (left) is a list
    assert coor[10][0] == COOR_ID[0] and coor[9][0] == COOR_ID[1]

    coor = get_structure_coordinates(
        structure_acronym='SSp',
    )
    assert coor[10][0] == COOR_ACRONYM[0] and coor[9][0] == COOR_ACRONYM[1]

    # exception: structure is invalid
    with pytest.raises(ValueError):
        get_structure_coordinates(
            structure_id=RANDOM_ID,
        )
    with pytest.raises(ValueError):
        get_structure_coordinates(
            structure_acronym=RANDOM_STRING
        )
