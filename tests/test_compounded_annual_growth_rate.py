from random import randint

import pytest

from src.compounded_annual_growth_rate import CompoundedAnnualGrowthRate


class TestCompoundedAnnualGrowthRate:
    def test_cagr_object_initializes_with_valid_params(self):
        """Tests that the CAGR object initializes successfully."""

        number_of_iterations = 100

        for iteration in range(number_of_iterations):
            starting_value = randint(1, 10000)
            ending_value = randint(0, 10000)
            time_in_years = randint(1, 10000)

            cagr_object = CompoundedAnnualGrowthRate(
                starting_value=starting_value, ending_value=ending_value, time_in_years=time_in_years
            )

            assert isinstance(cagr_object, CompoundedAnnualGrowthRate)
            assert cagr_object.starting_value == starting_value
            assert cagr_object.ending_value == ending_value
            assert cagr_object.time_in_years == time_in_years

    def test_cagr_object_does_not_initialize_invalid_params(self):
        """Tests that the CAGR object does not initialize successfully."""

        with pytest.raises(AssertionError, match="starting_value must be greater than 0"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value=0, ending_value=100, time_in_years=10)

            assert isinstance(cagr_object, type(None))

            cagr_object = CompoundedAnnualGrowthRate(starting_value=-1, ending_value=100, time_in_years=10)

            assert isinstance(cagr_object, type(None))

        with pytest.raises(AssertionError, match="ending_value must be greater than or equal to 0"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value=100, ending_value=-100, time_in_years=10)

            assert isinstance(cagr_object, type(None))

        with pytest.raises(AssertionError, match="time_in_years must be greater than 0"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value=100, ending_value=100, time_in_years=0)

            assert isinstance(cagr_object, type(None))

            cagr_object = CompoundedAnnualGrowthRate(starting_value=100, ending_value=100, time_in_years=-1)

            assert isinstance(cagr_object, type(None))

        with pytest.raises(AssertionError, match="starting_value must be of type int or float"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value="100", ending_value=100, time_in_years=10)

            assert isinstance(cagr_object, type(None))

        with pytest.raises(AssertionError, match="ending_value must be of type int or float"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value=100, ending_value="100", time_in_years=10)

            assert isinstance(cagr_object, type(None))

        with pytest.raises(AssertionError, match="time_in_years must be of type int"):
            cagr_object = CompoundedAnnualGrowthRate(starting_value=100, ending_value=100, time_in_years="10")

            assert isinstance(cagr_object, type(None))

    @pytest.mark.parametrize(
        "starting_value,ending_value,time_in_years,expected_cagr",
        [(100, 200, 1, 100), (100, 200, 5, 14.87), (100, 200, 10, 7.18)],
    )
    def test_calculate_positive_cagr_result(self, starting_value, ending_value, time_in_years, expected_cagr):
        """Tests CompoundedAnnualGrowthRate.calculate() returns a positive CAGR if starting_value < ending_value."""

        cagr_object = CompoundedAnnualGrowthRate(
            starting_value=starting_value, ending_value=ending_value, time_in_years=time_in_years
        )

        cagr_value = cagr_object.calculate()

        assert cagr_value > 0
        assert cagr_value == expected_cagr

    @pytest.mark.parametrize(
        "starting_value,ending_value,time_in_years,expected_cagr",
        [(100, 50, 1, -50), (100, 50, 5, -12.94), (100, 50, 10, -6.70)],
    )
    def test_calculate_negative_cagr_result(self, starting_value, ending_value, time_in_years, expected_cagr):
        """Tests CompoundedAnnualGrowthRate.calculate() returns a negative CAGR if starting_value > ending_value."""

        cagr_object = CompoundedAnnualGrowthRate(
            starting_value=starting_value, ending_value=ending_value, time_in_years=time_in_years
        )

        cagr_value = cagr_object.calculate()

        assert cagr_value < 0
        assert cagr_value == expected_cagr

    @pytest.mark.parametrize(
        "starting_value,ending_value,time_in_years",
        [(10, 10, 1), (100, 100, 10), (1000, 1000, 100)],
    )
    def test_calculate_zero_cagr_result(self, starting_value, ending_value, time_in_years):
        """Tests CompoundedAnnualGrowthRate.calculate() returns a zero CAGR if starting_value == ending_value."""

        cagr_object = CompoundedAnnualGrowthRate(
            starting_value=starting_value, ending_value=ending_value, time_in_years=time_in_years
        )

        cagr_value = cagr_object.calculate()

        assert cagr_value == 0

    def test_calculate_when_ending_value_is_zero(self):
        """Tests CompoundedAnnualGrowthRate.calculate() returns -100% CAGR if ending_value == 0."""

        for starting_value in [100, 1000, 10000]:
            for time_in_years in [1, 5, 10]:
                cagr_object = CompoundedAnnualGrowthRate(
                    starting_value=starting_value, ending_value=0, time_in_years=time_in_years
                )

                cagr_value = cagr_object.calculate()

                assert cagr_value == -100
