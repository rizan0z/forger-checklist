from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'a-VERY-secret-key'

# Manually add users: username: hashed_password
users = {
    'rizan': 'riz123',
    'eduardo': 'anotherpassword',
    'osho': 'osho237','aanya': 'rizanisabitch',
    'sayeedfarhad': 'farhad237',
    'brandon': 'brandon237','saurav':'saurav237'
}

# Checklist
CHECKLIST = {
    "PRE ENTRY CHECKLIST (must)": [
        "Are you sure you took less than 2 trade today?",
        "Are you in best time to trade this pair?",
        "Did you see the current trend and bias?",
        "Is there an 15FVG (htf imbalance) or a liquidity sweep?",
        "Do you have obvious DOL (Target)?",
        "Wait for ltf manipulation before looking for an entry",
        "Is there an IFVG for entry after manipulation? (must)",
        "Is there CISD after the IFVG? (must)",
        "Is there an smt? (optional)",
        "Are you following the appropriate risk?",
        "Target most recent highs and lows"
    ],
    "POST ENTRY PSYCHOLOGY (must)": [
        "Are you willing not to take more trade if this trade is a loss?",
        "Do you agree that losses are part of the game?",
        "Do you know that profitability comes with discipline?",
        "Are you aware of the fact 100% profitable trades only take 1 or 2 trade?",
        "Do you know that if you lost a trade even after sticking to all your rules you should blame the market and never doubt yourself?",
        "There is always tomorrow! Today is not the last day! If you lost 2 trade don't overtrade and come back tomorrow",
        "You lost 2 trade then that means today's market is bad don't trade anymore",
        "If others took win today that means they got lucky, don't doubt yourself"
    ],
    "POST TRADE CHECKLIST (must)": [
        "Target minimum 1:2rr and max 1:3rr",
        "Take partial 50% at 1:1 - 1:1.5rr (must)",
        "Trail sl to break even at 1:2rr",
        "Journal the trade after SL OR TP",
        "Avoid revenge trading and overtrading"
    ]
}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        uname = request.form['username']
        pw = request.form['password']
        # Plain text password check
        if uname in users and users[uname] == pw:
            session['user'] = uname
            return redirect(url_for('checklist'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/checklist')
def checklist():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('checklist.html', checklist=CHECKLIST, username=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
