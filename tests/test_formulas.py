import pytest

from src.formulas import *


class TestFormulas:
    @pytest.mark.parametrize(
        "principal,interest_rate,time,expected",
        [
            (1000.00, 5, 10, 1628.89),
            (1000.00, -5, 10, 598.74),
            (649.73, 25, 7, 3098.15),
            (649.73, -25, 7, 86.73),
            (1000.00, 0, 20, 1000.00),
            (1000.00, 10, 0, 1000.00),
            (1000.00, -100, 10, 0),
            (1000.00, 100, 1, 2000.00),
            (0, -6, 30, 0),
        ],
    )
    def test_calculate_compound_interest(self, principal, interest_rate, time, expected):
        compound_interest = calculate_compound_interest(principal, interest_rate, time)
        assert round(compound_interest, 2) == expected

    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,time,expected",
        [
            (1000, 5, 500, -2, 10, 3.99),
            (0, 5, 500, 2, 10, 0.00),
            (1000, 0, 500, 2, 15, 1.49),
            (1000, 5, 0, 1, 10, 0.00),
            (1000, 5, 500, 0, 15, 4.16),
            (1000, 5, 500, -2, 0, 2),
            (1000, -100, 500, -2, 15, 0),
            (1000, 5, 500, -100, 15, 0),
        ],
    )
    def test_calculate_future_revenue_per_share(
        self,
        current_revenue,
        revenue_growth,
        shares_outstanding,
        shares_growth,
        time,
        expected,
    ):
        revenue_per_share = calculate_future_revenue_per_share(
            current_revenue, revenue_growth, shares_outstanding, shares_growth, time
        )
        assert round(revenue_per_share, 2) == expected

    @pytest.mark.parametrize(
        "revenue_per_share,margin_of_revenue,expected",
        [
            (5.00, 20, 1.00),
            (5.00, 100, 5.00),
            (5.00, 0, 0.00),
            (0.00, 25, 0.00),
            (5.00, -0.01, 0.00),
            (5.00, 100.01, 0.00),
        ],
    )
    def test_calculate_margin_of_revenue(self, revenue_per_share, margin_of_revenue, expected):
        marginal_value = calculate_margin_of_revenue(revenue_per_share, margin_of_revenue)
        assert round(marginal_value, 2) == expected

    @pytest.mark.parametrize(
        "valuation_metric,terminal_ratio,expected",
        [
            (15, 2.30, 34.50),
            (75, 2.43, 182.25),
            (0, 2.50, 0.00),
            (11.5, 2.00, 23),
            (10, 0.00, 0.00),
            (-5, 10, 0.00),
            (8, -0.42, 0.00),
            (-5, -0.49, 0.00),
        ],
    )
    def test_calculate_terminal_value(self, valuation_metric, terminal_ratio, expected):
        terminal_value = calculate_terminal_value(valuation_metric, terminal_ratio)
        assert round(terminal_value, 2) == expected

    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,margin_of_revenue,time,expected",
        [
            (1000, 5, 500, -2, 15, 10, 0.60),  # 3.99 revenue per share
            (0, 5, 500, 2, 15, 10, 0.00),  # 0.00 revenue per share
            (1000, 0, 500, 2, 15, 15, 0.22),  # 1.49 revenue per share
            (1000, 5, 0, 1, 15, 10, 0.00),  # 0 revenue per share
            (1000, 5, 500, 0, 20, 15, 0.83),  # 4.16 revenue per share
            (1000, 5, 500, -2, 20, 0, 0.40),  # 2 revenue per share
            (1000, -100, 500, -2, 20, 15, 0),  # 0 revenue per share
            (1000, 5, 500, -100, 20, 15, 0),  # 0 revenue per share
        ],
    )
    def test_calculate_future_free_cash_flow(
        self,
        current_revenue,
        revenue_growth,
        shares_outstanding,
        shares_growth,
        margin_of_revenue,
        time,
        expected,
    ):
        future_value = calculate_future_value(
            current_revenue,
            revenue_growth,
            shares_outstanding,
            shares_growth,
            margin_of_revenue,
            time,
        )
        assert round(future_value, 2) == expected

    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,margin_of_revenue,discounted_rate,time,expected",
        [
            (1000, 5, 500, -2, 15, 12, 10, 0.19),  # 0.60 FCF
            (0, 5, 500, 2, 15, 10, 12, 0.00),  # 0.00 FCF
            (1000, 0, 500, 2, 15, 12, 15, 0.04),  # 0.22 FCF
            (1000, 5, 0, 1, 15, 12, 10, 0.00),  # 0 FCF
            (1000, 5, 500, 0, 20, 15, 15, 0.10),  # 0.83 FCF
            (1000, 5, 500, -2, 20, 15, 0, 0.40),  # 0.40 FCF
            (1000, -100, 500, -2, 15, 20, 15, 0),  # 0 FCF
            (1000, 5, 500, -100, 15, 20, 15, 0),  # 0 FCF
        ],
    )
    def test_calculate_discounted_value(
        self,
        current_revenue,
        revenue_growth,
        shares_outstanding,
        shares_growth,
        margin_of_revenue,
        discounted_rate,
        time,
        expected,
    ):
        discounted_value = calculate_discounted_value(
            current_revenue,
            revenue_growth,
            shares_outstanding,
            shares_growth,
            margin_of_revenue,
            discounted_rate,
            time,
        )
        assert round(discounted_value, 2) == expected

    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,margin_of_revenue,discounted_rate,terminal_ratio,time,expected",
        [
            (0, 10, 200, -2, 20, 10, 15, 7, 0),
            (419130, 10, 504, 1.5, 5, 15, 13, 7, 585.87),
            (419130, 15, 504, 1, 6, 12.5, 15, 7, 1181.95),
            (419130, 20, 504, 0.5, 7, 10, 17, 7, 2334.62),
            (77610, -1, 4050, -1, 20, 15, 12, 7, 33.49),
            (77610, 2, 4050, -2.5, 22, 12.5, 15, 7, 60.76),
            (77610, 5, 4050, -3.5, 24, 10, 18, 7, 107.30),
            (118970, 20, 2720, 2.5, 18, 15, 14, 7, 184.52),
            (118970, 25, 2720, 1.5, 20, 12.5, 16, 7, 354.86),
            (118970, 30, 2720, 0.5, 22, 10, 18, 7, 676.15),
        ],
    )
    def test_calculate_intrinsic_value(
        self,
        current_revenue,
        revenue_growth,
        shares_outstanding,
        shares_growth,
        margin_of_revenue,
        discounted_rate,
        terminal_ratio,
        time,
        expected,
    ):
        intrinsic_value = calculate_intrinsic_value(
            current_revenue,
            revenue_growth,
            shares_outstanding,
            shares_growth,
            margin_of_revenue,
            discounted_rate,
            terminal_ratio,
            time,
        )
        margin_of_error = abs(intrinsic_value - expected) / expected if expected != 0 else 0
        assert margin_of_error < 0.01
