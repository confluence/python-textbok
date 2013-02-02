import unittest
import trace, sys

from estimate import price_estimate

class TestEstimate(unittest.TestCase):
    def test_off_peak(self):
        # all these cases should fall within off-peak hours and have the same result
        test_cases = [
            ("23:59:59", "10:00", "N", "N"),
            ("00:00:00", "10:00", "N", "N"),
            ("00:00:01", "10:00", "N", "N"),
            ("05:59:59", "10:00", "N", "N"),
            ("06:00:00", "10:00", "N", "N"),
            ("06:00:01", "10:00", "N", "N"),
            ("19:00:00", "10:00", "N", "N"),
            ("19:00:01", "10:00", "N", "N"),
        ]

        for start, duration, far_away, share_call in test_cases:
            basic, op_discount, sc_discount, net, vat, total = price_estimate(start, duration, far_away, share_call)
            self.assertAlmostEqual(basic, 455.4)
            self.assertAlmostEqual(op_discount, 182.16)
            self.assertAlmostEqual(sc_discount, 0)
            self.assertAlmostEqual(net, 273.24)
            self.assertAlmostEqual(vat, 38.2536)
            self.assertAlmostEqual(total, 311.4936)

    def test_peak(self):
        # all these cases should fall within peak hours and have the same result
        test_cases = [
            ("07:00:00", "10:00", "N", "N"),
            ("07:00:01", "10:00", "N", "N"),
            ("17:59:59", "10:00", "N", "N"),
            ("18:00:00", "10:00", "N", "N"),
            ("18:00:01", "10:00", "N", "N"),
        ]

        for start, duration, far_away, share_call in test_cases:
            basic, op_discount, sc_discount, net, vat, total = price_estimate(start, duration, far_away, share_call)
            self.assertAlmostEqual(basic, 455.4)
            self.assertAlmostEqual(op_discount, 0)
            self.assertAlmostEqual(sc_discount, 0)
            self.assertAlmostEqual(net, 455.4)
            self.assertAlmostEqual(vat, 63.756)
            self.assertAlmostEqual(total, 519.156)

    def test_peak_and_off_peak(self):
        # these test cases cross the peak / off-peak boundary, and all have different results.
        test_cases = [
            ("06:59:59", "59:59", "N", "N"),
            ("07:00:00", "59:59", "N", "N"),
            ("07:00:01", "59:59", "N", "N"),

            ("18:59:59", "59:59", "N", "N"),
            ("19:00:00", "59:59", "N", "N"),
            ("19:00:01", "59:59", "N", "N"),

            ("06:30:00", "00:00", "N", "N"),
            ("06:30:00", "00:01", "N", "N"),
            ("06:30:00", "59:58", "N", "N"),
            ("06:30:00", "59:59", "N", "N"),
        ]

        expected_results = [
            (2731.641, 36.128400000000006, 0, 2695.5126, 377.371764, 3072.884364),
            (2731.641, 0.0, 0, 2731.641, 382.42974, 3114.07074),
            (2731.641, 0.0, 0, 2731.641, 382.42974, 3114.07074),

            (2731.641, 1056.528, 0, 1675.113, 234.51582, 1909.62882),
            (2731.641, 1092.6564, 0, 1638.9846, 229.457844, 1868.442444),
            (2731.641, 1092.6564, 0, 1638.9846, 229.457844, 1868.442444),

            (0.0, 0.0, 0, 59.4, 8.316, 67.716), # minimum charge
            (0.759, 0.3036, 0, 59.4, 8.316, 67.716), # minimum charge
            (2730.882, 546.48, 0, 2184.402, 305.81628, 2490.21828),
            (2731.641, 546.48, 0, 2185.161, 305.92254, 2491.08354),
        ]

        for parameters, results in zip(test_cases, expected_results):
            basic, op_discount, sc_discount, net, vat, total = price_estimate(*parameters)
            exp_basic, exp_op_discount, exp_sc_discount, exp_net, exp_vat, exp_total = results
            self.assertAlmostEqual(basic, exp_basic)
            self.assertAlmostEqual(op_discount, exp_op_discount)
            self.assertAlmostEqual(sc_discount, exp_sc_discount)
            self.assertAlmostEqual(net, exp_net)
            self.assertAlmostEqual(vat, exp_vat)
            self.assertAlmostEqual(total, exp_total)

    def test_far_destination_share_call(self):
        # now we repeat some basic test cases with a far destination and/or share-call

        test_cases = [
            # off-peak
            ("23:59:59", "10:00", "Y", "N"),
            ("23:59:59", "10:00", "Y", "Y"),
            ("23:59:59", "10:00", "N", "Y"),
            # peak
            ("07:00:00", "10:00", "Y", "N"),
            ("07:00:00", "10:00", "Y", "Y"),
            ("07:00:00", "10:00", "N", "Y"),
        ]

        expected_results = [
            (1056.6, 528.3, 0, 528.3, 73.962, 602.262),
            (1056.6, 528.3, 264.15, 264.15, 36.981, 301.131),
            (455.4, 182.16, 0.0, 273.24, 38.2536, 311.4936),

            (1056.6, 0.0, 0, 1056.6, 147.924, 1204.524),
            (1056.6, 0.0, 528.3, 528.3, 73.962, 602.262),
            (455.4, 0.0, 0.0, 455.4, 63.756, 519.156),
        ]

        for parameters, results in zip(test_cases, expected_results):
            basic, op_discount, sc_discount, net, vat, total = price_estimate(*parameters)
            exp_basic, exp_op_discount, exp_sc_discount, exp_net, exp_vat, exp_total = results
            self.assertAlmostEqual(basic, exp_basic)
            self.assertAlmostEqual(op_discount, exp_op_discount)
            self.assertAlmostEqual(sc_discount, exp_sc_discount)
            self.assertAlmostEqual(net, exp_net)
            self.assertAlmostEqual(vat, exp_vat)
            self.assertAlmostEqual(total, exp_total)

if __name__ == "__main__":
    t = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], count=1, trace=0)
    t.runfunc(unittest.main)

    r = t.results()
    r.write_results(show_missing=True)