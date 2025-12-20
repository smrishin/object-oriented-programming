# Minesweeper

Classic Minesweeper Game as played since ages.

This game has both GUI (Tkinker) app and a Web app.

## Game Architecture

This game is build with a Model-View-Controller Architecture.

### Model

Brains of the game which holds the game logic and rules.

#### Objects

**Cell** : Contains what each cell in the mineland holds.
**Board** : Contains a 2D array of cells and how they interact/
**Game State** : Contains the state of a single game played until won/lost.

### View

The game has two views:

- The GUI to run as a app on any OS. (tk_app)
- The Web app to play on the browser. (web_app)

### Controller

The controller connect the view with the game logic in model.

This game has two controllers:

- The tkinker controller connect the tkinker GUI with the model.
- The web app event handler to connect the HTML with the model.

## How to run the app

### Tkinker app

- Requires Python
- All the external packages used come inbuild with python.

From the root run main_tk in your terminal as a module

```
python -m tk_app.main_tk
```

### Web app
