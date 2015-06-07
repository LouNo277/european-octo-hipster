"""
The starting point of all SCK actions is to import initial data and from this
create `Samples`. Future activities will all use and manipulate those `Samples`.
"""
import os
from xlwings import Workbook, Range
from SCK import Sample
from SCK.constants import WORKBOOK_DIR, WORKBOOK_FILE, WORKBOOK_SHEET

def get_file_name():
    current = raw_input('Please enter a filename ...')
    filename = os.path.join(WORKBOOK_DIR, current)
    return filename


def get_sample_list(workbook=WORKBOOK_FILE):
    """
    Gets sample details from excel spreadsheet (one row per sample).
    :returns: A list in which the data of each row is stored as a separate list.
    """
    wb = Workbook(workbook)
    sample_list = Range(WORKBOOK_SHEET, 'L3:Q130').value
    # TODO: Add a function which determines the correct data range.

    print 'Getting Data from ' + str(WORKBOOK_SHEET)
    wb.close()

    # TODO: Add function which converts lists into dicts with appropriate keys.
    return sample_list


def create_samples(sample_list):
    """
    This function uses a list of lists for which `Sample` objects are created.
    :param sample_list: A list of lists which is returned from `get_sample_list`
    :returns: A list which contains instances of `Sample()`.
    """
    sample_objects = []
    print 'Creating "Sample" objects ... '
    for li in sample_list:
        sample_objects.append(Sample(li[0], li[1], li[2], li[3])
        print li[3]

    print str(len(sample_objects)) + ' Samples imported successfully.'
    return sample_objects


if __name__ == '__main__':
    WORKBOOK_FILE = get_file_name()
    sl = get_sample_list(WORKBOOK_FILE)
    sobjs = create_samples(sl)
