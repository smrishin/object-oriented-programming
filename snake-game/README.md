# 🐍 Snake Game (Python, OOP)

A classic Snake game built in **Python using pygame**, designed with clean **object-oriented architecture**.
The project focuses on separation of concerns, maintainability, and extensibility.

---

## 🎮 Features

- Smooth snake movement with fixed tick timing
- Wall collision and self-collision detection
- Food spawning and snake growth
- Score tracking
- Pause / resume
- Game over screen with restart (`R`)
- Optional wrap-around mode
- Clean OOP design (Grid, Snake, Renderer, Game)

---

## 🧠 Architecture Overview

```
snake-game/
│
├── core/
│   └── grid.py          # Board dimensions, bounds, random cell helpers
│
├── entities/
│   ├── snake.py         # Snake movement, growth, direction rules
│   └── food.py          # Food entity
│
├── render/
│   └── renderer.py      # All drawing logic (pygame)
│
├── io/
│   └── input_handler.py # (optional) input abstraction
│
├── game.py              # Game loop, state management
├── main.py              # Entry point
├── README.md
└── .gitignore
```

### Design principles used
- Single Responsibility Principle
- No rendering logic inside game rules
- No game logic inside rendering
- State-driven game loop
- Intentional data structures (`deque` for snake body)

---

## 🛠 Requirements

- Python **3.9+**
- `pygame`

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd snake-game
```

### 2️⃣ Create a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install pygame
```

Verify:

```bash
python -c "import pygame; print(pygame.__version__)"
```

---

## ▶️ Running the Game

```bash
python main.py
```

---

## 🎮 Controls

| Action | Key |
|------|----|
| Move Up | W / ↑ |
| Move Down | S / ↓ |
| Move Left | A / ← |
| Move Right | D / → |
| Pause / Resume | P |
| Restart | R |
| Quit | Close window |

---

## 💀 Game Rules

- Eat food to grow
- Hit wall or self to lose
- Restart anytime after game over

---

## 🔧 Customization Ideas

- Levels and speed scaling
- Obstacles
- Power-ups
- High-score persistence
- Menu screens
- Sound effects

---

## 📄 License

MIT License.
