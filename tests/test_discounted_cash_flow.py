from random import randint

import pytest

from src.discounted_cash_flow import DiscountedCashFlow


class TestDiscountedCashFlow:
    def test_dcf_object_initializes_with_valid_params(self):
        """Tests that the DCF object initializes successfully."""

        number_of_iterations = 100

        for iteration in range(number_of_iterations):
            revenue = randint(0, 1_000_000)
            revenue_growth_rate = randint(-100, 100)
            time_in_years = randint(1, 100)
            fcf_margin = randint(0, 100)
            desired_annual_return = randint(0, 100)
            terminal_multiple = randint(0, 100)

            dcf_object = DiscountedCashFlow(
                revenue=revenue,
                revenue_growth_rate=revenue_growth_rate,
                time_in_years=time_in_years,
                fcf_margin=fcf_margin,
                desired_annual_return=desired_annual_return,
                terminal_multiple=terminal_multiple,
            )

            assert isinstance(dcf_object, DiscountedCashFlow)
            assert dcf_object.revenue == revenue
            assert dcf_object.revenue_growth_rate == revenue_growth_rate / 100
            assert dcf_object.time_in_years == time_in_years
            assert dcf_object.fcf_margin == fcf_margin / 100
            assert dcf_object.desired_annual_return == desired_annual_return / 100
            assert dcf_object.terminal_multiple == terminal_multiple

    def test_dcf_object_does_not_initialize_with_invalid_params(self):
        """Tests that the CAGR object does not initialize successfully."""

        with pytest.raises(AssertionError, match="revenue must be of type int or float"):
            dcf_object = DiscountedCashFlow(
                revenue="10",
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="revenue must be greater than or equal to 0"):
            dcf_object = DiscountedCashFlow(
                revenue=-1,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="revenue_growth_rate must be of type int or float"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate="10",
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="revenue_growth_rate must be greater than or equal to -100"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=-101,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="time_in_years must be of type int"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years="10",
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="time_in_years must be greater than 0"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=0,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=-1,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="fcf_margin must be of type int or float"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin="10",
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="fcf_margin must be greater than or equal to 0"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=-1,
                desired_annual_return=10,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="desired_annual_return must be of type int or float"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return="10",
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="desired_annual_return must be greater than or equal to 0"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=-1,
                terminal_multiple=10,
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="terminal_multiple must be of type int or float"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple="10",
            )

            assert isinstance(dcf_object, type(None))

        with pytest.raises(AssertionError, match="terminal_multiple must be greater than or equal to 0"):
            dcf_object = DiscountedCashFlow(
                revenue=10,
                revenue_growth_rate=10,
                time_in_years=10,
                fcf_margin=10,
                desired_annual_return=10,
                terminal_multiple=-1,
            )

            assert isinstance(dcf_object, type(None))

    def test_get_cash_flow_at_invalid_times(self):
        """Tests DCF.get_cash_flow() with invalid time parameter raises the correct errors."""

        revenue = randint(0, 1_000_000)
        revenue_growth_rate = randint(-100, 100)
        time_in_years = randint(1, 100)
        fcf_margin = randint(0, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        with pytest.raises(AssertionError, match="time must be of type int or float"):
            dcf_object.get_cash_flow(time="1")

        with pytest.raises(AssertionError, match="time must be greater than or equal to 0"):
            dcf_object.get_cash_flow(time=-1)

    def test_get_cash_flow_at_time_zero(self):
        """Tests DCF.get_cash_flow() returns (revenue * fcf_margin) / 100 when time == 0."""

        revenue = randint(0, 1_000_000)
        revenue_growth_rate = randint(-100, 100)
        time_in_years = randint(1, 100)
        fcf_margin = randint(0, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        cash_flow = dcf_object.get_cash_flow(time=0)
        assert cash_flow == (revenue * fcf_margin) / 100

        dcf_object.revenue_growth_rate = 0
        cash_flow = dcf_object.get_cash_flow(time=0)
        assert cash_flow == (revenue * fcf_margin) / 100

        dcf_object.revenue_growth_rate = randint(-100, -1)
        cash_flow = dcf_object.get_cash_flow(time=0)
        assert cash_flow == (revenue * fcf_margin) / 100

    def test_get_cash_flow_at_nonzero_times_with_positive_revenue_growth_rate(self):
        """Tests DCF.get_cash_flow() returns expected values with revenue_growth_rate > 0."""

        revenue = 1_000_000
        revenue_growth_rate = 5
        time_in_years = 10
        fcf_margin = 10
        desired_annual_return = 10
        terminal_multiple = 10

        times = [1, 5, 15, 30, 50]
        solutions = [105_000, 127_628.16, 207_892.82, 432_194.24, 1_146_739.98]

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for index, time in enumerate(times):
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == solutions[index]

    def test_get_cash_flow_at_nonzero_times_with_negative_revenue_growth_rate(self):
        """Tests DCF.get_cash_flow() returns expected values with revenue_growth_rate < 0."""

        revenue = 1_000_000
        revenue_growth_rate = -5
        time_in_years = 10
        fcf_margin = 10
        desired_annual_return = 10
        terminal_multiple = 10

        times = [1, 5, 15, 30, 50]
        solutions = [95_000, 77_378.09, 46_329.12, 21_463.88, 7_694.50]

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for index, time in enumerate(times):
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == solutions[index]

    def test_get_cash_flow_at_nonzero_times_with_zero_revenue_growth_rate(self):
        """Tests DCF.get_cash_flow() returns (revenue * fcf_margin) / 100 with revenue_growth_rate == 0."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = 0
        time_in_years = randint(1, 100)
        fcf_margin = randint(1, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        times = [1, 5, 15, 30, 50]

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for time in times:
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == (revenue * fcf_margin) / 100

    def test_get_cash_flow_with_positive_revenue_growth_increases_over_time(self):
        """Tests DCF.get_cash_flow() with revenue_growth_rate > 0 increases as the time parameter increases."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = randint(1, 100)
        time_in_years = randint(1, 100)
        fcf_margin = randint(1, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        previous_cash_flow_value = dcf_object.get_cash_flow(time=0)

        for time in range(1, 100):
            current_cash_flow = dcf_object.get_cash_flow(time=time)
            assert current_cash_flow >= previous_cash_flow_value
            previous_cash_flow_value = current_cash_flow

    def test_get_cash_flow_with_negative_revenue_growth_decreases_over_time(self):
        """Tests DCF.get_cash_flow() with revenue_growth_rate < 0 decreases as the time parameter increases."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = randint(-100, -1)
        time_in_years = randint(1, 100)
        fcf_margin = randint(1, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        previous_cash_flow_value = dcf_object.get_cash_flow(time=0)

        for time in range(1, 100):
            current_cash_flow = dcf_object.get_cash_flow(time=time)
            assert current_cash_flow <= previous_cash_flow_value
            previous_cash_flow_value = current_cash_flow

    def test_get_cash_flow_with_zero_revenue_growth_does_not_change_over_time(self):
        """Tests DCF.get_cash_flow() with revenue_growth_rate == 0 does not change as the time parameter increases."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = 0
        time_in_years = randint(1, 100)
        fcf_margin = randint(1, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        previous_cash_flow_value = dcf_object.get_cash_flow(time=0)

        for time in range(1, 100):
            current_cash_flow = dcf_object.get_cash_flow(time=time)
            assert current_cash_flow == previous_cash_flow_value
            previous_cash_flow_value = current_cash_flow

    def test_get_cash_flow_at_nonzero_times_with_minimum_revenue_growth_is_zero(self):
        """Tests DCF.get_cash_flow() returns 0 with revenue_growth_rate == -100 for time >= 1."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = -100
        time_in_years = randint(1, 100)
        fcf_margin = randint(1, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for time in range(1, 100):
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == 0

    def test_get_cash_flow_with_zero_fcf_margin_is_always_zero(self):
        """Tests DCF.get_cash_flow() returns 0 with fcf_margin == 0."""

        revenue = randint(1, 1_000_000)
        revenue_growth_rate = randint(-100, 100)
        time_in_years = randint(1, 100)
        fcf_margin = 0
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for time in range(100):
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == 0

    def test_get_cash_flow_with_zero_revenue_is_always_zero(self):
        """Tests DCF.get_cash_flow() returns 0 with revenue == 0."""

        revenue = 0
        revenue_growth_rate = randint(-100, 100)
        time_in_years = randint(1, 100)
        fcf_margin = randint(0, 100)
        desired_annual_return = randint(0, 100)
        terminal_multiple = randint(0, 100)

        dcf_object = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=terminal_multiple,
        )

        for time in range(100):
            cash_flow = dcf_object.get_cash_flow(time=time)
            assert cash_flow == 0
