NUMBER_OF_CPU = "MAX"

FILE_RELEVANCE_PREDICTIONS = "data/relevance_predictionsTest.txt"
INPUT_FIELD_SEPARATOR = '\t'

TAG_WEIGHTED = True

FILE_TAG_WEIGHTS = "data/tagWeights.txt"
FILE_NEIGHBORS = "data/neighbors.txt"

NEIGHBORHOOD_SIZE = 250

LOG_NAME = "logs/load_neighbors.log"

ITEM1_COLUMN_NO = 0
ITEM2_COLUMN_NO = 1
RELEVANCE_SCORE_COLUMN_NO = 2


OVERRIDE_TEST = True
OVERRIDE_LOCAL = True
if OVERRIDE_TEST:
    from testconf import *
if OVERRIDE_LOCAL:
    from localconf import *