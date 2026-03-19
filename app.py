from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    n = data['n']
    start = data['start']
    end = data['end']
    obstacles = data['obstacles']
    policy = data['policy'] # Dict: {index: direction}

    # Parameters
    gamma = 0.9
    threshold = 1e-4
    reward_step = -1
    
    # Initialize V
    V = np.zeros(n * n)
    
    # Directions: 0: Up, 1: Down, 2: Left, 3: Right
    # (row, col) transformations
    actions = {
        'UP': (-1, 0),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
        'RIGHT': (0, 1)
    }

    def get_next_state(s, action_name):
        r, c = divmod(s, n)
        dr, dc = actions[action_name]
        nr, nc = r + dr, c + dc
        
        # Check boundaries
        if 0 <= nr < n and 0 <= nc < n:
            next_s = nr * n + nc
            # Check obstacles
            if next_s in obstacles:
                return s
            return next_s
        return s

    # Iterative Policy Evaluation
    while True:
        delta = 0
        new_V = np.copy(V)
        for s in range(n * n):
            if s == end or s in obstacles:
                continue
            
            action_name = policy.get(str(s))
            if not action_name: continue
            
            next_s = get_next_state(s, action_name)
            
            # V(s) = R + gamma * V(s')
            # Since policy is deterministic: sum is just 1 * [...]
            v = reward_step + gamma * V[next_s]
            
            new_V[s] = v
            delta = max(delta, abs(V[s] - v))
        
        V = new_V
        if delta < threshold:
            break

    return jsonify({'values': V.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
