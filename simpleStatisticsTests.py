__author__ = 'jmategk0'
import unittest
import simpleStatistics


class TestDescriptiveStatisticsMethods(unittest.TestCase):

    def setUp(self):
        self.descriptive_statistics = simpleStatistics.DescriptiveStatistics()
        self.test_dataset1 = [3, 5, 8, 10, 11]  # 8
        self.test_dataset2 = [3, 3, 4, 5, 7, 8]  # 4.5
        self.test_dataset3 = [1, 2, 3, 3, 3, 4]  # 3
        self.test_dataset4 = [1, 9, 8, 5, 8, 7]
        self.test_dataset5 = [1, 0, 6, 1]
        self.test_dataset6 = [1, 6, 4, 3, 8, 7, 6]

    def test_mode_with_valid_data_001(self):
        # arrange
        mode_data = self.test_dataset4

        # act
        mode_result = self.descriptive_statistics.mode(mode_data)

        # assert
        self.assertEqual(mode_result, 8)

    def test_mode_with_valid_data_002(self):
        # arrange
        mode_data = self.test_dataset3

        # act
        mode_result = self.descriptive_statistics.mode(mode_data)

        # assert
        self.assertEqual(mode_result, 3)

    def test_mode_with_invalid_data_001(self):
        # arrange
        mode_data = self.test_dataset1

        # act
        mode_result = self.descriptive_statistics.mode(mode_data)

        # assert
        self.assertEqual(mode_result, None)

    def test_mean_001(self):
        # arrange
        mean_data = self.test_dataset1

        # act
        mean_result = self.descriptive_statistics.mean(mean_data)

        # assert
        self.assertEqual(mean_result, 7.4)

    def test_median_001(self):
        # arrange
        median_data = self.test_dataset1

        # act
        median_result = self.descriptive_statistics.median(median_data)

        # assert
        self.assertEqual(median_result, 8)

    def test_variance_001(self):
        # arrange
        variance_data = self.test_dataset5

        # act
        variance_result = self.descriptive_statistics.variance(variance_data)

        # assert
        self.assertEqual(variance_result, 5.50)

    def test_standard_deviation_001(self):
        # arrange
        sd_data = self.test_dataset1

        # act
        sd_result = self.descriptive_statistics.standard_deviation(sd_data, round_value=True)

        # assert
        self.assertEqual(sd_result, 3.01)

    def test_standard_deviation_002(self):
        # arrange
        sd_data = self.test_dataset5

        # act
        sd_result = self.descriptive_statistics.standard_deviation(sd_data, round_value=True)

        # assert
        self.assertEqual(sd_result, 2.35)

    def test_standard_deviation_003(self):
        # arrange
        sd_data = self.test_dataset6

        # act
        sd_result = self.descriptive_statistics.standard_deviation(sd_data, is_population=False, round_value=True)

        # assert
        self.assertEqual(sd_result, 2.45)

    def test_sum_of_squared_deviations_001(self):
        # arrange: SS
        ss_data = self.test_dataset5

        # act
        ss_result = self.descriptive_statistics.sum_of_squared_deviations(ss_data)

        # assert
        self.assertEqual(ss_result, 22)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDescriptiveStatisticsMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
