from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_epf_corpus(
    salary: float, 
    employer_percent: float, 
    employee_percent: float, 
    age: int, 
    retirement_age: int = 58, 
    interest_rate: float = 0.0825
) -> float:
    if any([
        salary < 0, 
        employer_percent < 0, 
        employee_percent < 0, 
        age < 0,
        age > retirement_age,
        interest_rate < 0,
    ]):
        return 0.0

    years_left = retirement_age - age
    if years_left <= 0:
        return 0.0

    monthly_contribution = salary * (employer_percent + employee_percent) / 100
    if monthly_contribution <= 0:
        return 0.0

    total_amount = 0.0

    if interest_rate == 0:
        total_amount = monthly_contribution * years_left * 12
        return round(total_amount, 2)

    monthly_interest_rate = interest_rate / 12
    for _ in range(years_left * 12):
        total_amount = (total_amount + monthly_contribution) * (1 + monthly_interest_rate)

    return round(total_amount, 2)

@app.route("/", methods=["GET", "POST"])
def home():
    total_amount = None
    # Default input values
    salary_val = 50000
    employer_val = 12
    employee_val = 12
    age_val = 25

    if request.method == "POST":
        try:
            salary_val = float(request.form.get("salary"))
            employer_val = float(request.form.get("employer_percent"))
            employee_val = float(request.form.get("employee_percent"))
            age_val = int(request.form.get("age"))

            total_amount_num = calculate_epf_corpus(
                salary_val, employer_val, employee_val, age_val
            )
            total_amount = f"{total_amount_num:,.2f}"
        except Exception:
            total_amount = None

    return render_template(
        "index.html",
        total_amount=total_amount,
        salary_val=salary_val,
        employer_val=employer_val,
        employee_val=employee_val,
        age_val=age_val,
    )

if __name__ == "__main__":
    app.run(debug=True)
