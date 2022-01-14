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
        Time in years

    Returns
    -------
    accrued_amount : float
        The principal + interest over time.
    """
    accrued_amount = principal * (1 + interest_rate / 100) ** time
    accrued_amount = round(accrued_amount, 2)

    return accrued_amount


def calculate_future_revenue_per_share(
    current_revenue, revenue_growth, shares_outstanding, shares_growth, time
):
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
        Time in years.

    Returns
    -------
    revenue_per_share : float
        The calculated future revenue per share.

    """
    if shares_outstanding == 0 or shares_growth == -100:
        return 0

    future_revenue = calculate_compound_interest(current_revenue, revenue_growth, time)
    future_shares = calculate_compound_interest(shares_outstanding, shares_growth, time)

    revenue_per_share = future_revenue / future_shares

    return revenue_per_share


def calculate_margin_of_revenue(revenue_per_share, margin_of_revenue):
    """
    Calculates a given margin of the revenue per share.

    Parameters
    ----------
    revenue_per_share : float
        The revenue per share.
    margin_of_revenue : float
        The percentage that will be used as a margin.

    Returns
    -------
    marginal_value : float
        The value of the margin of the revenue per share.

    """
    if margin_of_revenue < 0 or margin_of_revenue > 100:
        return 0

    marginal_value = (margin_of_revenue / 100) * revenue_per_share

    return marginal_value


def calculate_terminal_value(valuation_metric, terminal_ratio):
    """
    Calculates the terminal value of the valuation metic.

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

    return round(valuation_metric * terminal_ratio, 2)


def calculate_future_value(
    current_revenue,
    revenue_growth,
    shares_outstanding,
    shares_growth,
    margin_of_revenue,
    time,
):
    """
    Calculate the future value margin at a given time.

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
    margin_of_revenue : float
        The percentage of revenue that is being discounted.
    time : int
        Time in years.

    Returns
    -------
    future_value : float
        The calculated future value.
    """
    revenue_per_share = calculate_future_revenue_per_share(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        time=time,
    )

    future_value = calculate_margin_of_revenue(
        revenue_per_share=revenue_per_share, margin_of_revenue=margin_of_revenue
    )

    return future_value


def calculate_discounted_value(
    current_revenue,
    revenue_growth,
    shares_outstanding,
    shares_growth,
    margin_of_revenue,
    discounted_rate,
    time,
):
    """
    Calculates the discounted value at a given time in years.

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
    margin_of_revenue : float
        The percentage of revenue that is being discounted.
    discounted_rate : float
        The percentage of the expected return.
    time : int
        Time in years.

    Returns
    -------
    discounted_value : float
        The calculated discounted value.
    """
    future_value = calculate_future_value(
        current_revenue=current_revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=shares_growth,
        margin_of_revenue=margin_of_revenue,
        time=time,
    )

    discount = (1 + discounted_rate / 100) ** time
    discounted_value = future_value / discount

    return discounted_value


def calculate_intrinsic_value(
    current_revenue,
    revenue_growth,
    shares_outstanding,
    shares_growth,
    margin_of_revenue,
    discounted_rate,
    terminal_ratio,
    time,
):
    """
    Calculates the discounted instrinsic value over a given time.

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
    margin_of_revenue : float
        The percentage of revenue that is being discounted.
    discounted_rate : float
        The percentage of the expected return.
    terminal_ratio : float
        The ratio of the valuation beyond the forecasted period.
    time : int
        Time in years.

    Returns
    -------
    intrinsic_value : float
        The discounted intrinsic value.
    """

    intrinsic_value = 0
    for year in range(1, time + 1):
        discounted_value = calculate_discounted_value(
            current_revenue,
            revenue_growth,
            shares_outstanding,
            shares_growth,
            margin_of_revenue,
            discounted_rate,
            year,
        )
        intrinsic_value += discounted_value

        if year == time:
            terminal_value = calculate_terminal_value(discounted_value, terminal_ratio)
            intrinsic_value += terminal_value

    intrinsic_value = round(intrinsic_value, 2)

    return intrinsic_value
