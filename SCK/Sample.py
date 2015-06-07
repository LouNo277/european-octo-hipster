class Sample(object):
    """
    A `Sample` is an instance of a chemical `Compound` which undergoes testing.
    # TODO: Write the parent `Compound` class.
    """

    def __init__(self, name, formula, fw, label, ms_file, rt=None):
        self.name = name
        self.formula = formula
        self.fw = fw
        self.label = label
        self.ms_file = ms_file
        self.rt = rt
        self.result = None
