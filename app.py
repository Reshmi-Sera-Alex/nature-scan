from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/health', methods=['GET', 'POST'])
def health():
    water_goal = None
    tip = None

    if request.method == 'POST':
        weight = float(request.form.get('weight', 0))
        activity = request.form.get('activity')

        water_goal = round((weight * 35) / 1000, 2)

        if activity == 'moderate':
            water_goal = round(water_goal + 0.5, 2)
            tip = "Great job staying active! Remember to sip water before and after your workout."
        elif activity == 'high':
            water_goal = round(water_goal + 1.0, 2)
            tip = "High activity levels require extra hydration and electrolytes to help your muscles recover."
        else:
            tip = "Try taking a 5-minute stretch break every hour to keep your energy levels steady."

    return render_template('health.html', water_goal=water_goal, tip=tip)

if __name__ == '__main__':
    app.run(debug=True)