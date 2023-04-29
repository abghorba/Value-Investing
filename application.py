from flask import Flask, render_template, request

from src.formulas import *

# Initialize Flask app
application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@application.route("/intrinsic-value-calculator", methods=["GET", "POST"])
def intrinsic_value_calculator():
    if request.method == "GET":
        return render_template("intrinsic-value.html")
    else:
        revenue = float(request.form.get("revenue").replace(",", ""))
        revenue_growth = float(request.form.get("revenue-growth"))
        shares_outstanding = float(request.form.get("shares-out").replace(",", ""))
        share_change = float(request.form.get("share-chg"))
        profit_margin = float(request.form.get("profit-margin"))
        fcf_margin = float(request.form.get("fcf-margin"))
        pe_ratio = float(request.form.get("pe-ratio"))
        pfcf_ratio = float(request.form.get("pfcf-ratio"))
        desired_annual_return = float(request.form.get("return"))
        time_in_years = int(request.form.get("time"))

        multiple_of_earnings = calculate_intrinsic_value(
            current_revenue=revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=share_change,
            margin_of_revenue=profit_margin,
            discounted_rate=desired_annual_return,
            terminal_ratio=pe_ratio,
            time=time_in_years,
        )

        discounted_cash_flow = calculate_intrinsic_value(
            current_revenue=revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=share_change,
            margin_of_revenue=fcf_margin,
            discounted_rate=desired_annual_return,
            terminal_ratio=pfcf_ratio,
            time=time_in_years,
        )

        return render_template(
            "intrinsic-value.html",
            multiple_of_earnings="{:.2f}".format(multiple_of_earnings),
            discounted_cash_flow="{:.2f}".format(discounted_cash_flow),
        )


if __name__ == "__main__":
    application.run()
