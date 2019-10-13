from app.analyzer import Analyzer

import unittest
import logging


class TestRecoder(unittest.TestCase):
    logging.basicConfig(level=logging.DEBUG)

    def setUp(self):
        self.test_data_dir = './tests/data/'

    def test_waveform(self):
        chunk = 1024
        model = Analyzer(chunk, self.test_data_dir)

        model.waveform("click.wav")


if __name__ == "__main__":
    unittest.main()


