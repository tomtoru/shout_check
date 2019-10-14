from app.recorder import Recoder

import unittest
import logging
import datetime
import os


class TestRecoder(unittest.TestCase):
    logging.basicConfig(level=logging.DEBUG)

    def setUp(self):
        self.recode_dir = './recode_data/'

    def test_recode(self):
        channels = 2
        rate = 44100
        chunk = 1024
        record_time = 5
        model = Recoder(channels, rate, chunk, record_time)

        output_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_test_record.wav"
        model.recode(output_name)

        assert os.path.exists(self.recode_dir + output_name), "ERROR::Failed to make recode file"

        os.remove(self.recode_dir + output_name)

    def test_auto_recode(self):
        channels = 2
        rate = 44100
        chunk = 1024
        record_time = 5
        model = Recoder(channels, rate, chunk, record_time)

        threhold = 0.01
        output_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_test_auto_record.wav"
        model.auto_recode(threhold, output_name)

        assert os.path.exists(self.recode_dir + output_name), "ERROR::Failed to make auto recode file"

        os.remove(self.recode_dir + output_name)


if __name__ == "__main__":
    unittest.main()
