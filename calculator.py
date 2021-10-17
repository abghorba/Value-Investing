from formulas import *

def main():
    current_revenue = 419130
    revenue_growth = 20
    shares_outstanding = 504
    shares_growth = 0.5
    profit_margin = 8
    free_cash_flow_margin = 7
    price_earnings_ratio = 17
    price_free_cash_flow_ratio = 17
    desired_annual_return = 10
    time_in_years = 7

    multiple_of_earnings = calculate_intrinsic_value(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        margin_of_revenue=profit_margin,
        discounted_rate=desired_annual_return,
        terminal_ratio=price_earnings_ratio,
        time=time_in_years
    )
    print(multiple_of_earnings)

    discounted_cash_flow = calculate_intrinsic_value(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        margin_of_revenue=free_cash_flow_margin,
        discounted_rate=desired_annual_return,
        terminal_ratio=price_free_cash_flow_ratio,
        time=time_in_years
    )
    print(discounted_cash_flow)

    
if __name__ == "__main__":
    main()