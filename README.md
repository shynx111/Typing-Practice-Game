# Type Dodge (Pygame)

Type Dodge is an arcade-style dodge game built with Pygame where your character is a circle moving across a visual QWERTY keyboard layout. Press letter keys on your keyboard to snap your circle to matching key zones and avoid incoming red hazard attacks until you survive the full run.

## How to Play

* **Move Your Character:** Press any letter key from `Q`–`P`, `A`–`L`, or `Z`–`M` to move your circle directly to that key's position on the grid.
* **Survive the Hazards:** Watch for warning telegraph shapes that fade in before turning into active red danger zones:
  * **Vertical Attacks:** Sweep down columns across the board.
  * **Horizontal Attacks:** Cut across rows from the left or right side.
  * **Key Tile Attacks:** Target specific letter tiles on the keyboard grid (introduced at higher difficulties).
  * **Circular Attacks:** Detonate circular hazard zones that cover nearby keys (introduced at the highest difficulty).
* **Lives & Progression:** You start with **3 lives** and a brief immunity window after taking a hit. Difficulty ramps up as the game progresses—survive until the timer completes to win, or lose all lives to game over.

## Using This Game to Improve Typing Skills

Regular typing tests are great for building words-per-minute and rhythm, but Circle Dodge takes a looser, more playful approach—it's a handy warm-up for getting a better feel for where keys actually sit on the board:

* **Find Keys Without Peeking:** Because the grid mirrors a standard QWERTY layout across the top (`Q`–`P`), home (`A`–`L`), and bottom (`Z`–`M`) rows, you start connecting letters to their spots rather than glancing down every time you need to move.
* **Jump Between Rows Faster:** Waves of vertical and horizontal hazards force you to hop back and forth between rows on the fly, which helps smooth out awkward row-to-row reaches.
* **Reach Keys You Normally Skip:** Safe spaces don't stay open for long, so you end up tapping outer and bottom-row keys you might otherwise hesitate over in everyday typing.
* **A Quick Warm-Up Between Tasks:** Play a round or two between study sessions or work blocks to loosen up your hands and get your brain into typing mode before diving into real practice.

## Getting Started

### Prerequisites

* Python 3.8+
* `pygame`

Install Pygame using pip:

```bash
pip install pygame
```

### Running the Game

Save the game script (for example, as `circle_dodge.py`) and run it from your terminal:

```bash
python circle_dodge.py
```
