from formulas import *

def main():
    current_revenue = 419130
    revenue_growth = 15
    shares_outstanding = 504
    shares_growth = 1
    profit_margin = 6.5
    free_cash_flow_margin = 6
    price_earnings_ratio = 15
    price_free_cash_flow_ratio = 15
    desired_annual_return = 12.5
    time_in_years = 7

    multiple_of_earnings = calculate_multiple_of_earnings_intrinsic_value(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        profit_margin=profit_margin,
        price_earnings_ratio=price_earnings_ratio,
        time=time_in_years
    )
    print(multiple_of_earnings)

    discounted_cash_flow = calculate_discounted_free_cash_flow_intrinsic_value(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        free_cash_flow_margin=free_cash_flow_margin,
        discounted_rate=desired_annual_return,
        price_free_cash_flow_ratio=price_free_cash_flow_ratio,
        time=time_in_years
    )
    print(discounted_cash_flow)

    
if __name__ == "__main__":
    main()