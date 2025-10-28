<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Simple Pong Game</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="game-container">
    <header>
      <h1>Simple Pong</h1>
      <div class="scoreboard">
        <div class="score">Player: <span id="leftScore">0</span></div>
        <div class="score">Computer: <span id="rightScore">0</span></div>
      </div>
    </header>

    <canvas id="gameCanvas" width="800" height="500"></canvas>

    <div class="controls">
      <button id="startBtn">Start</button>
      <button id="pauseBtn">Pause</button>
      <button id="resetBtn">Reset</button>
      <label>
        AI Difficulty
        <select id="aiDifficulty">
          <option value="0.06">Easy</option>
          <option value="0.10" selected>Normal</option>
          <option value="0.16">Hard</option>
        </select>
      </label>
      <small class="hint">Use mouse or ↑/↓ keys to move left paddle</small>
    </div>

    <footer>
      <p>Made with HTML/CSS/JS — simple Pong demo</p>
    </footer>
  </div>

  <script src="script.js"></script>
</body>
</html>
