class Compound(object):
    """
    A `Compound` is a chemical; it has a name/id, a structure, and a formula.
    """
    def __init__(self, name, formula, fw):
        self.name = name
        self.formula = formula
        self.fw = fw

class Sample(Compound):
    """
    A `Sample` is a (physical) instance of a `Compound` which undergoes testing.
    """

    def __init__(self, name, formula, fw, label, ms_file, rt=None):
        super(Sample, self).__init__(name, formula, fw)
        self.label = label
        self.ms_file = ms_file
        self.rt = rt
        self.result = None
