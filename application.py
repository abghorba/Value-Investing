from flask import Flask, render_template, request
from formulas import *

# Initialize Flask app
application = Flask(__name__)


@application.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        revenue = request.form.get("revenue")
        revenue_growth = request.form.get("revenue-growth")
        shares_outstanding = request.form.get("shares-out")
        share_change = request.form.get("share-chg")
        profit_margin = request.form.get("profit-margin")
        fcf_margin = request.form.get("fcf-margin")
        pe_ratio = request.form.get("pe-ratio")
        pfcf_ratio = request.form.get("pfcf-ratio")
        desired_annual_return = request.form.get("return")
        time_in_years = request.form.get("time")

        multiple_of_earnings = calculate_intrinsic_value(
        current_revenue=revenue,
        revenue_growth=revenue_growth,
        shares_outstanding=shares_outstanding,
        shares_growth=share_change,
        margin_of_revenue=profit_margin,
        discounted_rate=desired_annual_return,
        terminal_ratio=pe_ratio,
        time=time_in_years
        )
        print(multiple_of_earnings)

        discounted_cash_flow = calculate_intrinsic_value(
            current_revenue=revenue,
            revenue_growth=revenue_growth,
            shares_outstanding=shares_outstanding,
            shares_growth=share_change,
            margin_of_revenue=fcf_margin,
            discounted_rate=desired_annual_return,
            terminal_ratio=pfcf_ratio,
            time=time_in_years
        )
        print(discounted_cash_flow)





        return render_template("index.html")


if __name__ == "__main__":
    application.run()