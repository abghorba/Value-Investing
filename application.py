from flask import Flask, render_template, request

from src.compounded_annual_growth_rate import CompoundedAnnualGrowthRate
from src.discounted_cash_flow import DiscountedCashFlow

# Initialize Flask app
application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@application.route("/dcf-calculator", methods=["GET", "POST"])
def dcf_calculator():
    if request.method == "GET":
        return render_template("dcf.html")

    else:
        revenue = float(request.form.get("revenue").replace(",", ""))
        revenue_growth_rate = float(request.form.get("revenue-growth-rate"))
        fcf_margin = float(request.form.get("fcf-margin"))
        pfcf_ratio = float(request.form.get("pfcf-ratio"))
        desired_annual_return = float(request.form.get("return"))
        time_in_years = int(request.form.get("time"))

        discounted_cash_flow = DiscountedCashFlow(
            revenue=revenue,
            revenue_growth_rate=revenue_growth_rate,
            time_in_years=time_in_years,
            fcf_margin=fcf_margin,
            desired_annual_return=desired_annual_return,
            terminal_multiple=pfcf_ratio,
        )

        dcf_value = discounted_cash_flow.calculate()
        dcf_value_formatted = "{:.2f}".format(dcf_value)

        return render_template("dcf.html", discounted_cash_flow=dcf_value_formatted)


@application.route("/cagr-calculator", methods=["GET", "POST"])
def cagr_calculator():
    if request.method == "GET":
        return render_template("cagr.html")

    else:
        starting_value = float(request.form.get("starting-value"))
        ending_value = float(request.form.get("ending-value"))
        time_in_years = int(request.form.get("time"))

        cagr = CompoundedAnnualGrowthRate(
            starting_value=starting_value, ending_value=ending_value, time_in_years=time_in_years
        )

        cagr_value = cagr.calculate()
        cagr_value_formatted = "{:.2f}".format(cagr_value)

        return render_template("cagr.html", cagr=cagr_value_formatted)


if __name__ == "__main__":
    application.run()
