class TestASDF:
    def __init__(self, input):
        self.id = self._parse_id(input)
        self.whatever = self._parse_whatever(input)
        print("ID is: {}".format(self.id))
        print("whatever is: {}".format(self.whatever))

    def _parse_id(self, input):
        return input['id']

    def _parse_whatever(self, input):
        return input['whatever']


a = TestASDF({"id":"jimmy", "whatever":"bleh"})