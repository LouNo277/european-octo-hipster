# TODO: reduce this file to a minimal working example of usage for sck.


def get_file_name():
    current = raw_input('Please enter a filename ...')
    filename = os.path.join(WORKBOOK_DIR, current)
    return filename


def get_sample_list(workbook=WORKBOOK_FILE):
    """
    gets the relevant data for building Samples
    """
    wb = Workbook(workbook)
    sample_list = Range('Plate', 'L3:Q130').value
    print 'Getting Data from ' + str(WORKBOOK_SHEET)
    return sample_list


def create_samples(sample_list):
    sample_objects = []
    print 'Creating "Sample" objects ... '
    for li in sample_list:
        sample_objects.append(Sample(li[0], li[1], li[2], li[3], li[4], li[5]))
        print li[3]

    print str(len(sample_objects)) + ' Samples imported successfully.'
    return sample_objects


if __name__ == '__main__':
    WORKBOOK_FILE = get_file_name()
    sl = get_sample_list(WORKBOOK_FILE)
    sobjs = create_samples(sl)
