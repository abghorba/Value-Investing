from formulas import *
import pytest

class TestFormulas():

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
        ]
    )
    def test_calculate_compound_interest(self, principal, interest_rate, time, expected):
        assert calculate_compound_interest(principal, interest_rate, time) == expected


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
            (1000, 5, 500, -100, 15, 0)
        ]
    )
    def test_calculate_future_revenue_per_share(
        self, current_revenue, revenue_growth,
        shares_outstanding, shares_growth, time, expected):
        assert calculate_future_revenue_per_share(
            current_revenue, revenue_growth,
            shares_outstanding, shares_growth,
            time
        ) == expected


    @pytest.mark.parametrize(
        "revenue_per_share,margin,expected",
        [
            (5.00, 20, 1.00),
            (5.00, 100, 5.00),
            (5.00, 0, 0.00),
            (0.00, 25, 0.00),
            (5.00, -0.01, 0.00),
            (5.00, 100.01, 0.00),
        ]
    )
    def test_calculate_margin_of_revenue(self, revenue_per_share, margin, expected):
        assert calculate_margin_of_revenue(revenue_per_share, margin) == expected


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
        ]
    )
    def test_multiply_terminal_ratio(
        self, valuation_metric, 
        terminal_ratio, expected):
        assert multiply_terminal_ratio(valuation_metric, terminal_ratio) == expected


    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,free_cash_flow_margin,time,expected",
        [
            (1000, 5, 500, -2, 15, 10, 0.60), #3.99 revenue per share
            (0, 5, 500, 2, 15, 10, 0.00), #0.00 revenue per share
            (1000, 0, 500, 2, 15, 15, 0.22), #1.49 revenue per share
            (1000, 5, 0, 1, 15, 10, 0.00), #0 revenue per share
            (1000, 5, 500, 0, 20, 15, 0.83), #4.16 revenue per share
            (1000, 5, 500, -2, 20, 0, 0.40), #2 revenue per share
            (1000, -100, 500, -2, 20, 15, 0), #0 revenue per share
            (1000, 5, 500, -100, 20, 15, 0), #0 revenue per share
        ]
    )
    def test_calculate_future_free_cash_flow(self, current_revenue, revenue_growth, shares_outstanding, shares_growth, free_cash_flow_margin, time, expected):
        assert calculate_future_free_cash_flow(
            current_revenue=current_revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=shares_growth,
            free_cash_flow_margin=free_cash_flow_margin,
            time=time
        ) == expected


    @pytest.mark.parametrize(
        "current_revenue,revenue_growth,shares_outstanding,shares_growth,free_cash_flow_margin,discounted_rate,time,expected",
        [
            (1000, 5, 500, -2, 15, 12, 10, 0.19), #0.60 FCF
            (0, 5, 500, 2, 15, 10, 12, 0.00), #0.00 FCF
            (1000, 0, 500, 2, 15, 12, 15, 0.04), #0.22 FCF
            (1000, 5, 0, 1, 15, 12, 10, 0.00), #0 FCF
            (1000, 5, 500, 0, 20, 15, 15, 0.10), #0.83 FCF
            (1000, 5, 500, -2, 20, 15, 0, 0.40), #0.40 FCF
            (1000, -100, 500, -2, 15, 20, 15, 0), #0 FCF
            (1000, 5, 500, -100, 15, 20, 15, 0), #0 FCF
        ]
    )
    def test_calculate_discounted_free_cash_flow(self, current_revenue, revenue_growth, shares_outstanding, shares_growth, free_cash_flow_margin, discounted_rate, time, expected):
        assert calculate_discounted_free_cash_flow(
            current_revenue=current_revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=shares_growth,
            free_cash_flow_margin=free_cash_flow_margin,
            discounted_rate=discounted_rate,
            time=time
        ) == expected

    