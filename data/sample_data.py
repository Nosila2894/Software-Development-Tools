class SampleData():
    def __init__(self, data=None):
        self.data = data if data else {}
        self.build_data()

    #Override this method in subclasses to build specific data
    #And to add failsafe to data when booting
    def build_data(self):
        self.data["sample_data"] = "This is some sample data for testing purposes."
        self.data["sample_list"] = [1, 2, 3, 4, 5]
        self.data["sample_dict"] = {"key1": "value1", "key2": "value2"}
        self.data["sample_boolean"] = True

