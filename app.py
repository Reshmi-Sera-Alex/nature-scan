from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('health.html', water_goal=None, tip=None)

@app.route('/health', methods=['GET', 'POST'])
def health():
    water_goal = None
    tip = None

    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight', 0))
        except (TypeError, ValueError):
            weight = 0

        activity = request.form.get('activity', 'low')

        if weight > 0:
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


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    mood_score = None
    mood_note = ''

    if request.method == 'POST':
        try:
            mood_score = int(request.form.get('mood', 5))
            mood_score = max(1, min(10, mood_score))
        except (TypeError, ValueError):
            mood_score = 5

        mood_note = request.form.get('mood_note', '').strip()

    return render_template('mood.html', mood_score=mood_score, mood_note=mood_note)


@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    checked = False
    symptom_names = []
    duration = ''
    severity = ''

    if request.method == 'POST':
        checked = True
        symptom_names = request.form.getlist('symptoms')
        other_symptoms = request.form.get('other_symptoms', '').strip()
        duration = request.form.get('duration', '')
        severity = request.form.get('severity', '')

        if other_symptoms:
            symptom_names.append(other_symptoms)

    return render_template(
        'symptoms.html',
        checked=checked,
        symptom_names=symptom_names,
        duration=duration,
        severity=severity
    )


if __name__ == '__main__':
    app.run(debug=True)
