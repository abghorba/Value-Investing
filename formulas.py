def calculate_compound_interest(principal, interest_rate, time):
    """
    Calculates the compound interest over time in years.
    
    Parameters
    ----------
    principal : float 
        Principal amount.
    interest_rate : float
        Annual nominal interest rate as a percent.
    time : int
        Time in decimal years.

    Returns
    -------
    accrued_amount : float
        The principal + interest over time.
    """
    accrued_amount = principal*(1 + interest_rate/100)**time
    accrued_amount = round(accrued_amount, 2)

    return accrued_amount


def calculate_future_revenue_per_share(current_revenue, revenue_growth, shares_outstanding, shares_growth, time):
    """
    Calculates the future revenue per share at a specified
    time in years.

    Parameters
    ----------
    current_revenue : float 
        Most current revenue in millions.
    revenue_growth : float
        Annual nominal rate of revenue growth as a percent.
    shares_outstanding : float 
        Most current number of shares in millions.
    shares_growth : float
        Annual nominal rate of share growth as a percent. 
    time : int
        Time in decimal years.

    Returns
    -------
    revenue_per_share : float
        The calculated future revenue per share
    
    """
    if shares_outstanding == 0 or shares_growth == -100:
        return 0

    future_revenue = calculate_compound_interest(
        current_revenue, revenue_growth, time
    )
    future_shares = calculate_compound_interest(
        shares_outstanding, shares_growth, time
    )
    revenue_per_share = round(future_revenue/future_shares, 2)

    return revenue_per_share


def calculate_margin_of_revenue(revenue_per_share, margin):
    """
    Calculates a given margin of the revenue per share.

    Parameters
    ----------
    revenue_per_share : float
        The revenue per share.
    margin : float
        The percentage that will be used as a margin.

    Returns
    -------
    float
        The value of the margin of the revenue per share.

    """
    if margin < 0 or margin > 100:
        return 0

    return round((margin/100)*revenue_per_share, 2)


def multiply_terminal_ratio(valuation_metric, terminal_ratio):
    """
    Calculates the multiple of the given valuation metric.

    Parameters
    ----------
    valuation_metric: float

    terminal_ratio : float
        The multiple of the valuation metric.

    Returns
    -------
    float
        The instrinsic value per share calculated
        by the multiple of earnings.
    """
    if valuation_metric < 0 or terminal_ratio < 0:
        return 0

    return round(valuation_metric*terminal_ratio, 2)


def calculate_future_free_cash_flow(current_revenue, revenue_growth, shares_outstanding, shares_growth, free_cash_flow_margin, time):
    """
    Calculate the free cash flow at a given time.

    Parameters
    ----------
    current_revenue : float 
        Most current revenue in millions.
    revenue_growth : float
        Annual nominal rate of revenue growth as a percent.
    shares_outstanding : float 
        Most current number of shares in millions.
    shares_growth : float
        Annual nominal rate of share growth as a percent.
    free_cash_flow_margin : float
        The percentage of revenue that is free cash flow.
    time : int
        Time in decimal years.

    Returns
    -------
    float
        The calculated free cash flow.
    """
    revenue_per_share = calculate_future_revenue_per_share(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        time=time
    )

    free_cash_flow = calculate_margin_of_revenue(
        revenue_per_share=revenue_per_share,
        margin=free_cash_flow_margin
    )

    return free_cash_flow


def calculate_discounted_free_cash_flow(current_revenue, revenue_growth, shares_outstanding, shares_growth, free_cash_flow_margin, discounted_rate, time):
    """
    Calculates the discounted free cash flow at a given time in years.

    Parameters
    ----------
    current_revenue : float 
        Most current revenue in millions.
    revenue_growth : float
        Annual nominal rate of revenue growth as a percent.
    shares_outstanding : float 
        Most current number of shares in millions.
    shares_growth : float
        Annual nominal rate of share growth as a percent.
    free_cash_flow_margin : float
        The percentage of revenue that is free cash flow.
    discounted_rate : float
        The percentage of the expected return.
    time : int
        Time in decimal years.

    Returns
    -------
    float
        The calculated discounted free cash flow.
    """
    free_cash_flow = calculate_future_free_cash_flow(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        free_cash_flow_margin=free_cash_flow_margin,
        time=time
    )

    discount = (1+discounted_rate/100)**time
    discounted_cash_flow = round(free_cash_flow/discount, 2)

    return discounted_cash_flow


def calculate_multiple_of_earnings_intrinsic_value(current_revenue, revenue_growth, shares_outstanding, shares_growth, profit_margin, price_earnings_ratio, time):
    """
    Calculates the multiple of earnings instrinsic value.

    Parameters
    ----------
    current_revenue : float 
        Most current revenue in millions.
    revenue_growth : float
        Annual nominal rate of revenue growth as a percent.
    shares_outstanding : float 
        Most current number of shares in millions.
    shares_growth : float
        Annual nominal rate of share growth as a percent.
    profit_margin : float
        The percentage of revenue that is net profit.
    price_earnings_ratio : float
        The ratio of the market cap to earnings.
        Equivalently, price per share to earnings per share.
        The historical market price to earnings ratio is about 15.
    time : int
        Time in decimal years.

    Returns
    -------
    float
        The multiple of earnings intrinsic value.

    """
    revenue_per_share = calculate_future_revenue_per_share(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        time=time)

    earnings_per_share = calculate_margin_of_revenue(
        revenue_per_share=revenue_per_share, 
        margin=profit_margin)

    multiple_of_earnings = multiply_terminal_ratio(
        terminal_ratio=price_earnings_ratio,
        valuation_metric=earnings_per_share)

    return multiple_of_earnings


def calculate_discounted_free_cash_flow_intrinsic_value(current_revenue, revenue_growth, shares_outstanding, shares_growth, free_cash_flow_margin, discounted_rate, price_free_cash_flow_ratio, time):
    """
    Calculates the discounted free cash flow instrinsic value over a given time.

    Parameters
    ----------
    current_revenue : float 
        Most current revenue in millions.
    revenue_growth : float
        Annual nominal rate of revenue growth as a percent.
    shares_outstanding : float 
        Most current number of shares in millions.
    shares_growth : float
        Annual nominal rate of share growth as a percent.
    free_cash_flow_margin : float
        The percentage of revenue that is free cash flow.
    discounted_rate : float
        The percentage of the expected return.
    time : int
        Time in decimal years.

    Returns
    -------
    float
        The discounted free cash flow intrinsic value.
    """

    discounted_cash_flow_intrinsic_value = 0
    for year in range(1, time+1):
        discounted_free_cash_flow = calculate_discounted_free_cash_flow(
            current_revenue=current_revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=shares_growth,
            free_cash_flow_margin=free_cash_flow_margin,
            discounted_rate=discounted_rate,
            time=year
        )

        print(year, discounted_free_cash_flow)

        discounted_cash_flow_intrinsic_value += discounted_free_cash_flow
    
    terminal_value = calculate_discounted_free_cash_flow(
            current_revenue=current_revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=shares_growth,
            free_cash_flow_margin=free_cash_flow_margin,
            discounted_rate=discounted_rate,
            time=time
        )

    terminal_value *= price_free_cash_flow_ratio

    return discounted_cash_flow_intrinsic_value + terminal_value