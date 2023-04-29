class CompoundedAnnualGrowthRate:
    def __init__(self, starting_value=0, ending_value=0, time_in_years=0):
        """
        Constructor.

        :param starting_value: Initial value
        :param ending_value: Final value
        :param time_in_years: Time in years
        """

        assert isinstance(starting_value, (int, float)), "starting_value must be of type int or float"
        assert starting_value > 0, "starting_value must be greater than 0"
        assert isinstance(ending_value, (int, float)), "ending_value must be of type int or float"
        assert ending_value >= 0, "ending_value must be greater than or equal to 0"
        assert isinstance(time_in_years, int), "time_in_years must be of type int"
        assert time_in_years > 0, "time_in_years must be greater than 0"

        self.starting_value = starting_value
        self.ending_value = ending_value
        self.time_in_years = time_in_years

    def print_current_assumptions(self):
        """
        Prints all class variables.

        :return: None
        """

        print("")
        print(f"Starting Value = ${self.starting_value:,}")
        print(f"Ending Value = ${self.ending_value:,}")
        print(f"Time in Years = {self.time_in_years}")

    def calculate(self):
        """
        Using the current variables, calculate the CAGR.

        :return: CAGR value
        """

        self.print_current_assumptions()

        cagr = ((self.ending_value / self.starting_value) ** (1 / self.time_in_years) - 1) * 100

        print("")
        print("-" * 40)
        print(f"CAGR = {cagr:,.2f}%")
        print("-" * 40)
        print("")

        return round(cagr, 2)
