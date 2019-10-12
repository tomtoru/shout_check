from app.recorder import Recoder

import unittest
import logging
import datetime


class TestRecoder(unittest.TestCase):
    logging.basicConfig(level=logging.DEBUG)

    def setUp(self):
        pass

    def test_run(selfs):
        channels = 2
        rate = 44100
        chunk = 1024
        record_time = 5
        model = Recoder(channels, rate, chunk,record_time)

        output_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_test_record.wav"
        model.recode(output_name)


if __name__ == "__main__":
    unittest.main()