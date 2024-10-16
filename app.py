import numpy as np
from flask import Flask, request, render_template, jsonify
from scipy import stats

app = Flask(__name__)

def resample_trajectory(trajectory, length=60):  # Reduced length to 60
    trajectory = np.array(trajectory)
    indices = np.linspace(0, len(trajectory) - 1, length).astype(int)
    return trajectory[indices]

def is_straight_line(trajectory, threshold=0.01):  # Increased threshold to 0.01
    x = trajectory[:, 0]
    y = trajectory[:, 1]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return abs(r_value) >= (1 - threshold)

def analyze_trajectory(trajectory):
    trajectory = resample_trajectory(trajectory)
    return "Bot detected (perfect straight line trajectory)" if is_straight_line(trajectory) else "Human detected"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    trajectory = request.json['trajectory']
    result = analyze_trajectory(np.array(trajectory))
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
