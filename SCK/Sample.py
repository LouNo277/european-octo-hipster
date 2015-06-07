class Compound(object):
    """
    A `Compound` is a chemical; it has an id (csn), a chemical formula with fw.
    """

    def __init__(self, csn, formula, fw):
        """

        """
        self.csn = csn
        self.formula = formula
        self.fw = fw


class Sample(Compound):
    """
    A `Sample` is a (physical) instance of a `Compound` which undergoes testing.
    """

    def __init__(self, csn, formula, fw, isn):
        super(Sample, self).__init__(csn, formula, fw)
        self.isn = isn
        self.label = ''
        self.ms_file = ''
        self.rt = ''
        self.result = None # To be replaced by an instance of 'Result()'

    def set_label(self, label):
        self.label = label

    def set_ms_file(self, ms_file):
        self.ms_file = ms_file

    def set_rt(self, rt):
        self.rt = rt
