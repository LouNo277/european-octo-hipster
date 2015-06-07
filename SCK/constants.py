# TODO: Content of file to be reduced to nothing.
# TODO: Constants should be provided as user defined parameters / arguments.

import os

# main excel workbook which contains the initial set of data
WORKBOOK_DIR = os.curdir
WORKBOOK_FILE = os.path.join(WORKBOOK_DIR, 'default_input.xlsm')
WORKBOOK_SHEET = 'Plate'

# xml_factory
TARGETS_TEMPLATE = 'TARGET_TEMPLATE.xml'

# obtain_hts_results
RESULTS_FILE = 'INTTARG_RESULT.xls'
PEAK_LIST = 'PEAKTAB_RESULT.xls'

# get_water
FILENAME_WATER = 'water.txt'
FILENAME_DMSO = 'dmso.txt'
DMSO_CONCENTRATION = 84465