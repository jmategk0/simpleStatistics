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

    def test_standard_deviation_001(self):
        # arrange
        sd_data = self.test_dataset1

        # act
        sd_result = self.descriptive_statistics.standard_deviation(sd_data, round_value=True)

        # assert
        self.assertEqual(sd_result, 3.01)

    def test_standard_deviation_002(self):
        # arrange
        sd_data = [1, 0, 6, 1]

        # act
        sd_result = self.descriptive_statistics.standard_deviation(sd_data, round_value=True)

        # assert
        self.assertEqual(sd_result, 2.35)

    def test_sum_of_squared_deviations_001(self):
        # arrange
        sd_data = [1, 0, 6, 1]

        # act
        sd_result = self.descriptive_statistics.sum_of_squared_deviations(sd_data)

        # assert
        self.assertEqual(sd_result, 22)

'''
class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)
'''


suite = unittest.TestLoader().loadTestsFromTestCase(TestDescriptiveStatisticsMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
