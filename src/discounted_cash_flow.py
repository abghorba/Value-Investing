class DiscountedCashFlow:
    """Present value of all future cash flows."""

    def __init__(
        self,
        revenue=0,
        revenue_growth_rate=0,
        time_in_years=0,
        fcf_margin=0,
        desired_annual_return=0,
        terminal_multiple=0,
    ):
        """
        Constructor.

        :param revenue:
        :param revenue_growth_rate:
        :param time_in_years:
        :param fcf_margin:
        :param desired_annual_return:
        :param terminal_multiple:
        """

        assert isinstance(revenue, (int, float)), "revenue must be of type int or float"
        assert revenue >= 0, "revenue must be greater than or equal to 0"
        assert isinstance(revenue_growth_rate, (int, float)), "revenue_growth_rate must be of type int or float"
        assert revenue_growth_rate >= -100, "revenue_growth_rate must be greater than or equal to -100"
        assert isinstance(time_in_years, int), "time_in_years must be of type int"
        assert time_in_years > 0, "time_in_years must be greater than 0"
        assert isinstance(fcf_margin, (int, float)), "fcf_margin must be of type int or float"
        assert fcf_margin >= 0, "fcf_margin must be greater than or equal to 0"
        assert isinstance(desired_annual_return, (int, float)), "desired_annual_return must be of type int or float"
        assert desired_annual_return >= 0, "desired_annual_return must be greater than or equal to 0"
        assert isinstance(terminal_multiple, (int, float)), "terminal_multiple must be of type int or float"
        assert terminal_multiple >= 0, "terminal_multiple must be greater than or equal to 0"

        self.revenue = revenue
        self.revenue_growth_rate = revenue_growth_rate / 100
        self.time_in_years = time_in_years
        self.fcf_margin = fcf_margin / 100
        self.desired_annual_return = desired_annual_return / 100
        self.terminal_multiple = terminal_multiple
        self._debug_mode = False

    def _toggle_debug_mode(self):
        self._debug_mode = not self._debug_mode

        if self._debug_mode:
            print("")
            print("***Debug Mode On***")

    def print_current_assumptions(self):
        """
        Prints all class variables.

        :return: None
        """

        print("")
        print(f"Revenue = ${self.revenue:,}")
        print(f"Revenue Growth Rate = {self.revenue_growth_rate * 100}%")
        print(f"Time in Years = {self.time_in_years}")
        print(f"FCF Margin = {self.fcf_margin * 100}%")
        print(f"Desired Annual Return = {self.desired_annual_return * 100}%")
        print(f"Terminal Multiple = {self.terminal_multiple}")

    def get_cash_flow(self, time):
        """
        Calculates the cash flow at a given time = T:

            CASH_FLOW(T) = FCF_MARGIN * REVENUE * (1 + REVENUE_GROWTH_RATE) ^ T

        :param time: The year the cash flow will be calculated for
        :return: Cash flow value
        """

        assert isinstance(time, (int, float)), "time must be of type int or float"
        assert time >= 0, "time must be greater than or equal to 0"

        revenue = self.revenue * ((1 + self.revenue_growth_rate) ** time)

        if self._debug_mode:
            print(f"Revenue at Year {time} = ${revenue:,.2f}")

        cash_flow = round(revenue * self.fcf_margin, 2)

        if self._debug_mode:
            print(f"Cash Flow at Year {time} = ${cash_flow}")

        return cash_flow

    def get_present_value(self, time):
        """
        Calculates the present value of cash flow at a given time = T:

            PRESENT_VALUE(T) = CASH_FLOW(T) / (1 + DESIRED_ANNUAL_RETURN) ^ T

        :param time: The year the cash flow will be calculated for
        :return: Cash flow value
        """

        assert isinstance(time, (int, float)) and time >= 0

        current_cash_flow = self.get_cash_flow(time)
        present_value = round(current_cash_flow / ((1 + self.desired_annual_return) ** time), 2)

        if self._debug_mode:
            print(f"Present Value At Year {time} = ${present_value}")

        return present_value

    def get_terminal_value(self):
        """
        Calculates the terminal value at time = T:

            TERMINAL_VALUE = CASH_FLOW(T) * TERMINAL_MULTIPLE

        :return: Terminal value
        """

        terminal_cash_flow = self.get_present_value(self.time_in_years)

        if self._debug_mode:
            print("")
            print(f"Terminal Cash Flow = ${terminal_cash_flow:,.2f}")

        terminal_value = round(self.terminal_multiple * terminal_cash_flow, 2)

        if self._debug_mode:
            print(f"Terminal Value = ${terminal_value}")

        return terminal_value

    def calculate(self, verbose=False):
        """
        Using the current variables, calculate the DCF value.

        :param verbose: True to display all calculations on CLI; False otherwise
        :return: DCF value
        """

        self.print_current_assumptions()

        if verbose:
            self._toggle_debug_mode()

        dcf_value = 0

        for time in range(1, self.time_in_years):
            if self._debug_mode:
                print("")

            dcf_value += self.get_present_value(time)

        if self._debug_mode:
            print("")

        terminal_value = self.get_terminal_value()
        dcf_value += terminal_value
        dcf_value = round(dcf_value, 2)

        print("")
        print("-" * 40)
        print(f"DCF Value = ${dcf_value}")
        print("-" * 40)
        print("")

        # Toggle debug mode again to turn it off
        if verbose:
            self._toggle_debug_mode()

        return dcf_value
