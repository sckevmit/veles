"""
Created on Jan 28, 2014

Copyright (c) 2013 Samsung Electronics Co., Ltd.
"""
import logging
import unittest

import veles.opencl as opencl
import veles.opencl_units as opencl_units


class Test(unittest.TestCase):
    def add_ref(self, unit):
        pass

    def testBenchmark(self):
        logging.basicConfig(level=logging.DEBUG)
        self.bench = opencl_units.OpenCLBenchmark(self, device=opencl.Device())
        logging.info("Result: %d points", self.bench.estimate())


if __name__ == "__main__":
    unittest.main()
