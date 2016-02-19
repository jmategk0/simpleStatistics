# author jmategk0
# Goals:
# 1. Produce an intermediate level python library with more features than the built-in stats module in
# python 3.4+ but with a simplified interface and syntax compared with more robust libraries like pandas.
# 2. The code will by compatible with python 2.7 and python 3.5
# 3. Library has no dependencies outside the standard python library
# 4. Code organisation and syntax will make sense intuitively to anyone who passed undergraduate level statistics
# 5. Code usability is targeted to be "self documenting" and descriptive enough to be used by python novices, including
# people without formal training in software development
# Note: This is not a good library if you need high performance, this is good library if you want basic features with a
# low learning curve

import math


class DescriptiveStatistics(object):

    def the_sum_of_scores_from_list(self, list_of_values):
        # SigmaX
        my_sum = sum(list_of_values)
        return my_sum

    def square_all_values_in_list(self, list_of_values):
        # X^2
        squared_list = [X ** 2 for X in list_of_values]
        # squaredList = map(lambda X: X ** 2, list_of_values)
        return squared_list

    def the_sum_of_squares(self, list_of_values):
        # SigmaX^2
        squared_list = self.square_all_values_in_list(list_of_values)
        sum_of_squares = self.the_sum_of_scores_from_list(squared_list)
        return sum_of_squares

    def the_square_of_the_sum(self, list_of_values):
        # (SigmaX)^2
        sum_of_list = self.the_sum_of_scores_from_list(list_of_values)
        square_of_summed_values = sum_of_list ** 2
        return square_of_summed_values

    def subtract_amount_from_all_items_in_list(self, list_of_values, amount=1):
        # (x-1)
        new_list = [X - amount for X in list_of_values]
        return new_list

    def subtract_amount_and_square_all_items_in_list(self, list_of_values, amount=1):
        # (x-1) ^2
        subtracted_list = self.subtract_amount_from_all_items_in_list(list_of_values, amount)
        squared_list = self.square_all_values_in_list(subtracted_list)
        return squared_list

    def the_sum_of_subtracting_amount_from_all_items_in_list(self, list_of_values, amount=1):
        # Sigma(x-1)
        subtracted_list = self.subtract_amount_from_all_items_in_list(list_of_values, amount)
        sum_of_subtracted_values_in_list = self.the_sum_of_scores_from_list(subtracted_list)
        return sum_of_subtracted_values_in_list

    def the_sum_of_subtracting_an_amount_and_squaring_result_for_all_items_in_list(self, list_of_values, amount=1):
        # Sigma(X-1)^2
        subtracted_squared_list = self.subtract_amount_and_square_all_items_in_list(list_of_values, amount)
        summed_list = self.the_sum_of_scores_from_list(subtracted_squared_list)
        return summed_list

    def minimum(self, list_of_values):
        return min(list_of_values)

    def maximum(self, list_of_values):
        return max(list_of_values)

    def get_range_of_list_values(self, list_of_values):
        max_value = max(list_of_values)
        min_value = min(list_of_values)
        my_range = (max_value - min_value)
        return my_range

    def range(self, max_value, min_value):
        my_range = (max_value - min_value)
        return my_range

    def count_occurrences_of_value(self, list_of_values, search_term):
        return list_of_values.count(search_term)

    def get_unique_values_from_list(self, list_of_values):
            list_as_set = set(list_of_values)
            list_of_unique_values = list(list_as_set)
            return list_of_unique_values

    def get_proportion_of_value(self, frequency, total_number):
        # p=f/N
        proportion = (float(frequency)/float(total_number))
        return proportion

    def get_percent_from_proportion(self, proportion):
        # percent=proportion *100 or p=(f/N)*100
        percent = (proportion * 100)
        return percent

    def midpoint(self, min_value, max_value):
        midpoint = ((min_value+max_value)/2)
        return midpoint

    def mean(self, list_of_values):
        # M = sigmaX / n
        sigma_x = self.the_sum_of_scores_from_list(list_of_values)
        population_mean = (float(sigma_x)/float(len(list_of_values)))
        return population_mean

    def weighted_mean(self, list_of_lists):
        #  overall mean = sigmaX1 + sigmaX2 / n1 + n2
        sigma_combined_group = 0
        total_number_combined_group = 0
        for singleList in list_of_lists:
            sigma_combined_group += sum(singleList)
            total_number_combined_group += len(singleList)
        overall_mean = float(sigma_combined_group)/float(total_number_combined_group)
        return overall_mean

    def median(self, list_of_values):
        if (len(list_of_values) % 2) == 0:
            median_slot = (len(list_of_values) / 2) - 1
            low_midpoint = median_slot
            high_midpoint = median_slot+1
            median = (float(list_of_values[high_midpoint]) + float(list_of_values[low_midpoint])) / 2
            return median
        else:
            median_slot = len(list_of_values) / 2
            median = float(list_of_values[median_slot])
            return median

    def mode(self, list_of_values):
        frequency_distribution_table = self.make_simple_frequency_distribution_table(list_of_values)
        mode = 0
        mode_frequency = 0
        for value in frequency_distribution_table:
            if frequency_distribution_table[value] >= mode:
                mode_frequency = frequency_distribution_table[value]
                # mode = frequencyDistributionTable[value]
                mode = value
            else:
                pass
        if mode_frequency >= 2:
            return mode
        else:
            mode = None
            return mode

    def deviation(self, mean, score):
        # deviationScore =X - mew
        deviation_score = (score - mean)
        return deviation_score

    def sum_of_deviation_scores(self, list_of_values):
        # Sigma(X - mew)
        sum_scores = 0
        mean = self.mean(list_of_values)
        for item in list_of_values:
            sum_scores += self.deviation(mean, item)
        return sum_scores

    def variance(self, list_of_values, is_population=True):
        sum_scores = 0
        mean = self.mean(list_of_values)
        for item in list_of_values:
            deviation = self.deviation(mean, item)
            sum_scores += abs(deviation **2)
        if is_population == True:
            variance = sum_scores / len(list_of_values)
        else:
            variance = sum_scores / (len(list_of_values) - 1)  # sample variance uses degrees of freedom (df)
        return variance

    def standard_deviation(self, list_of_values, is_population=True, round_value=False, degree_of_precision=2):
        # page 94, start from here next time
        variance = self.variance(list_of_values, is_population)
        standard_deviation = math.sqrt(variance)
        if round_value == False:
            pass
        else:
            standard_deviation = round(standard_deviation, degree_of_precision)
        return standard_deviation

    def sum_of_squared_deviations(self, list_of_values):
        # SS = sigma(X-mew)^2
        sum_of_scores = self.the_sum_of_scores_from_list(list_of_values)
        squared_scores = self.square_all_values_in_list(list_of_values)
        sum_of_squared_scores = sum(squared_scores)
        number_of_scores = len(list_of_values)
        squared_sum_of_scores = (sum_of_scores ** 2)
        sum_of_squared_deviations = sum_of_squared_scores - (squared_sum_of_scores/number_of_scores)
        return sum_of_squared_deviations

    def make_class_intervals(self, min_value, max_value, interval):
        counter = 0
        stop_flag = False
        class_interval_list = []
        interval_start = min_value - interval
        interval_end = interval_start + interval
        number_of_intervals = ((max_value/interval) - (min_value/interval))

        while stop_flag == False:
            if counter <= number_of_intervals-1:
                interval_start += interval
                interval_end += interval
                interval_end_cleaned = interval_end-1

                class_interval = (str(interval_start) + "-" + str(interval_end_cleaned))
                class_interval_list.append(class_interval)
                counter += 1
            else:
                stop_flag = True
                counter += 1
        return class_interval_list

    def make_simple_frequency_distribution_table(self, list_of_values):
        frequency_distribution_table = {}
        unique_list_values = self.get_unique_values_from_list(list_of_values)
        for value in unique_list_values:
            number_of_values = self.count_occurrences_of_value(list_of_values, value)
            frequency_distribution_table[value] = number_of_values
        return frequency_distribution_table

    def make_full_frequency_distribution_table(self, list_of_values):
        # change to inset in to deict with count = key to keep order? Needed? Make option for returnType?
        frequency_distribution_table = []
        unique_list_values = self.get_unique_values_from_list(list_of_values)
        total_number_of_values = len(list_of_values)
        for value in unique_list_values:
            table_row_dictionary = {}
            table_row_dictionary["value"] = value
            table_row_dictionary["frequency"] = self.count_occurrences_of_value(list_of_values, value)
            table_row_dictionary["proportion"] = self.get_proportion_of_value(table_row_dictionary["frequency"], total_number_of_values)
            table_row_dictionary["percent"] = self.get_percent_from_proportion(table_row_dictionary["proportion"])
            frequency_distribution_table.append(table_row_dictionary)
        return frequency_distribution_table

    def make_full_grouped_frequency_distribution_table(self, list_of_values, start_interval, max_interval_value, interval_width):
        frequency_distribution_table = []
        class_interval_list = self.make_class_intervals(start_interval, max_interval_value, interval_width)

        total_number_of_values = len(list_of_values)
        for value in class_interval_list:
            table_row_dictionary = {}
            class_interval_values = value.split("-")
            lower_interval = int(class_interval_values[0])
            higher_interval = int(class_interval_values[1])
            counter = lower_interval
            class_interval_frequency = 0
            while counter <= higher_interval:
                interval_frequency = self.count_occurrences_of_value(list_of_values, counter)
                class_interval_frequency += interval_frequency
                counter += 1

            table_row_dictionary["value"] = value
            table_row_dictionary["frequency"] = class_interval_frequency
            table_row_dictionary["proportion"] = self.get_proportion_of_value(table_row_dictionary["frequency"], total_number_of_values)
            table_row_dictionary["percent"] = self.get_percent_from_proportion(table_row_dictionary["proportion"])
            frequency_distribution_table.append(table_row_dictionary)
        return frequency_distribution_table

    def make_simple_grouped_frequency_distribution_table(self, list_of_values, start_interval, max_interval_value, interval_width):
        frequency_distribution_table = {}
        class_interval_list = self.make_class_intervals(start_interval, max_interval_value, interval_width)

        for value in class_interval_list:
            class_interval_values = value.split("-")
            lower_interval = int(class_interval_values[0])
            higher_interval = int(class_interval_values[1])
            counter = lower_interval
            class_interval_frequency = 0

            while counter <= higher_interval:
                interval_frequency = self.count_occurrences_of_value(list_of_values, counter)
                class_interval_frequency += interval_frequency
                counter += 1
            frequency_distribution_table[value] = class_interval_frequency
        return frequency_distribution_table

    def the_sum_of_simple_frequency_distribution_table(self, frequency_distribution_table):
        # sigmafX
        sum_of_table = 0
        for table_key in frequency_distribution_table:
            table_x_value = table_key
            table_f_value = frequency_distribution_table[table_key]
            sum_of_table += (table_f_value * table_x_value)
        return sum_of_table

    def summarise_descriptive_statistics(self, list_of_values, is_population=False):
        summary_data = {}
        summary_data["mean"] = self.mean(list_of_values)
        summary_data["median"] = self.median(list_of_values)
        summary_data["mode"] = self.mode(list_of_values)
        summary_data["number"] = len(list_of_values)
        summary_data["minimum"] = self.minimum(list_of_values)
        summary_data["maximum"] = self.maximum(list_of_values)
        summary_data["range"] = self.range(summary_data["minimum"], summary_data["maximum"])
        summary_data["standard_deviation"] = self.standard_deviation(list_of_values, is_population)
        return summary_data


class InferentialStatistics(object):

    def z_score_calculate(self, score_value, mean, standard_division, round_value=False, degree_of_precision=2):
        z_score = (score_value - mean) / standard_division
        if round_value == False:
            pass
        else:
            z_score = round(z_score, degree_of_precision)
        return z_score

    def z_score_calculate_from_list(self, score_value, list_of_values, is_population, round_value=False, degree_of_precision=2):
        descriptive_statistics = DescriptiveStatistics()
        mean = descriptive_statistics.mean(list_of_values)
        standard_deviation = descriptive_statistics.standard_deviation(list_of_values, is_population)
        z_score = self.z_score_calculate(score_value, mean, standard_deviation, round_value, degree_of_precision)
        return z_score

    def score_value_from_z_score(self, mean, standard_division, z_score):
        score_value = mean + (z_score * standard_division)
        return score_value

    def z_score_transformation(self, list_of_values, is_population=True, round_value=False, degree_of_precision=2):
        descriptive_statistics = DescriptiveStatistics()
        mean = descriptive_statistics.mean(list_of_values)
        standard_deviation = descriptive_statistics.standard_deviation(list_of_values, is_population, round_value, degree_of_precision)
        z_score_list = []
        for item in list_of_values:
            z_score = self.z_score_calculate(item, mean, standard_deviation)
            z_score_list.append(z_score)
        return z_score_list

    def z_score_from_list(self, score_value, list_of_values, is_population=True, round_value=False, degree_of_precision=2):
        descriptive_statistics = DescriptiveStatistics()
        mean = descriptive_statistics.mean(list_of_values)
        standard_deviation = descriptive_statistics.standard_deviation(list_of_values,is_population, round_value, degree_of_precision)
        z_score = self.z_score_calculate(score_value, mean, standard_deviation)
        return z_score

    def probability(self, number_of_outcomes, total_number_of_possible_outcomes):
        probability_value = number_of_outcomes / total_number_of_possible_outcomes
        return probability_value


class HypothesisTests(object):
    pass


class AnalysisOfVariance(object):
    pass


class CorrelationAndNonparametricTests(object):
    pass
