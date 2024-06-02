class DataStream:
    def __init__(self):
        self.data_dict = {}
        self.output = []

    def should_output_data_str(self, timestamp: int, data_string: str):
        if data_string in self.data_dict:
            last_timestamp = self.data_dict[data_string]
            if timestamp < last_timestamp + 5:
                self.output.append(False)
        self.data_dict[data_string] = timestamp
        self.output.append(True)

# Input
data_stream = DataStream()
data_stream.should_output_data_str(timestamp=0, data_string="hello")
data_stream.should_output_data_str(timestamp=1, data_string="world")
data_stream.should_output_data_str(timestamp=6, data_string="hello")
data_stream.should_output_data_str(timestamp=7, data_string="hello")
data_stream.should_output_data_str(timestamp=8, data_string="world")

print(data_stream.output)