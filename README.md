# Asteroids

A modern recreation of the classic Asteroids arcade game built with Python and Pygame. Navigate through space, destroy asteroids, and rack up points while avoiding collisions in this action-packed shooter.

## Demo

![Game Demo](./demo.gif)

## Features

- **Classic Arcade Gameplay**
  - Control a spaceship that can rotate and thrust in any direction
  - Shoot projectiles to destroy asteroids
  - Asteroids split into smaller pieces when hit
  - Progressive difficulty with continuous asteroid spawning

- **Physics-Based Movement**
  - Realistic vector-based movement and rotation
  - Momentum-based ship controls
  - Smooth 360-degree rotation
  - Collision detection using circle-based geometry

- **Dynamic Asteroid System**
  - Asteroids spawn from screen edges at random intervals
  - Three size tiers: large, medium, and small
  - Splitting mechanics: larger asteroids break into two smaller ones
  - Random velocities and spawn positions for unpredictability

- **Game Mechanics**
  - Real-time score tracking
  - Shooting cooldown system to prevent spam
  - Sprite group management for efficient collision detection
  - Smooth 60 FPS gameplay

- **Development Features**
  - Event logging system for gameplay analysis (optional)
  - Game state tracking in JSONL format
  - Clean OOP architecture with inheritance

## Technologies Used

- **Python 3.x**
- **Pygame 2.x** - Graphics, input handling, and sprite management
- **Vector Mathematics** - For realistic physics and movement
- **Object-Oriented Programming** - Inheritance-based architecture with base `CircleShape` class

## How It Works

### Core Game Loop

The game runs at 60 FPS and updates all game objects each frame:

1. **Input Processing**: Detect keyboard input for ship controls
2. **Update Phase**: Move all objects (player, asteroids, shots) based on velocity
3. **Collision Detection**: Check for asteroid-player and asteroid-shot collisions
4. **Rendering**: Draw all sprites to the screen
5. **Score Display**: Show current score in real-time

### Physics System

All game objects inherit from `CircleShape`, which provides:

- Position and velocity vectors
- Circle-based collision detection
- Base update and draw methods

**Movement Calculation:**

```python
# Ship movement uses vector rotation
forward = pygame.Vector2(0, 1).rotate(self.rotation)
self.position += forward * PLAYER_SPEED * dt
```

### Asteroid Splitting Logic

When an asteroid is hit:

1. The asteroid is destroyed
2. If it's not minimum size, it splits into two smaller asteroids
3. New asteroids inherit velocity with randomized angles
4. Velocity is increased by 1.2x for added challenge

```python
# Split into two asteroids at different angles
velocity1 = self.velocity.rotate(angle)
velocity2 = self.velocity.rotate(-angle)
# Both move 20% faster than parent
asteroid1.velocity = velocity1 * 1.2
asteroid2.velocity = velocity2 * 1.2
```

## What I Learned

This project deepened my understanding of several key concepts:

- **Vector Mathematics**: Implementing rotation, velocity, and position using 2D vectors. Understanding how vector operations create smooth, physics-based movement.

- **Sprite Management**: Using Pygame's sprite groups for efficient collision detection and rendering. Understanding the container pattern for automatic sprite management.

- **Game Physics**: Delta time (dt) for frame-independent movement, ensuring consistent gameplay regardless of frame rate.

- **Collision Detection**: Implementing circle-to-circle collision using distance calculations: `distance <= radius1 + radius2`

- **Object-Oriented Design**: Creating a base `CircleShape` class that all game objects inherit from, demonstrating the power of inheritance for code reuse.

- **Event-Driven Architecture**: Handling continuous input (holding keys) vs. discrete events (single key presses).

## How to Run

### Prerequisites

- Python 3.6 or higher
- Pygame library

### Installation

1. Clone this repository:

```bash
git clone https://github.com/a-maystorov/asteroids.git
cd asteroids
```

2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

### Project Structure

```
asteroids/
│
├── main.py              # Main game loop and collision handling
├── player.py            # Player ship class with movement and shooting
├── asteroid.py          # Asteroid class with splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Projectile class
├── circleshape.py       # Base class for all circular game objects
├── constants.py         # Game configuration constants
├── logger.py            # Optional: Game state and event logging
├── game_state.jsonl     # Generated: Game state snapshots (optional)
└── game_events.jsonl    # Generated: Game events log (optional)
```

## Controls

- **W / ↑**: Thrust forward
- **S / ↓**: Thrust backward
- **A / ←**: Rotate left
- **D / →**: Rotate right
- **SPACE**: Shoot

## Game Rules

1. Destroy asteroids by shooting them
2. Large asteroids split into medium asteroids (×2)
3. Medium asteroids split into small asteroids (×2)
4. Small asteroids are destroyed completely
5. Each asteroid destroyed earns 10 points
6. Colliding with any asteroid ends the game
7. Asteroids continuously spawn from screen edges

## Scoring

- **Hit any asteroid**: +10 points
- Large asteroids spawn more asteroids when destroyed, leading to higher potential scores
- Try to create chain reactions by splitting multiple asteroids quickly

## Code Highlights

### Circle-Based Collision Detection

```python
def collides_with(self, other):
    """
    Check if two circular objects are colliding.
    Uses distance formula: if distance between centers
    is less than sum of radii, they're colliding.
    """
    distance = self.position.distance_to(other.position)
    return distance <= self.radius + other.radius
```

This elegant solution is computationally efficient and works perfectly for circular objects.

### Asteroid Spawning System

The `AsteroidField` class spawns asteroids from random edges:

```python
edges = [
    # Each edge defined by: [velocity direction, position lambda]
    [pygame.Vector2(1, 0), lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],  # Left edge
    [pygame.Vector2(-1, 0), lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],  # Right edge
    # ... top and bottom edges
]
```

This design makes it easy to spawn asteroids that move inward from any screen edge.

### Delta Time for Frame Independence

```python
def update(self, dt):
    # dt = time since last frame in seconds
    self.position += self.velocity * dt
```

Multiplying movement by `dt` ensures the game runs at the same speed regardless of frame rate, a crucial technique for professional game development.

## Configuration

Edit `constants.py` to customize gameplay:

```python
SCREEN_WIDTH = 1280          # Window width
SCREEN_HEIGHT = 720          # Window height
PLAYER_SPEED = 200           # Ship movement speed
PLAYER_TURN_SPEED = 300      # Rotation speed
PLAYER_SHOOT_SPEED = 500     # Projectile speed
PLAYER_SHOOT_CD_SECONDS = 0.3  # Shooting cooldown
ASTEROID_SPAWN_RATE_SECONDS = 0.8  # How often asteroids spawn
ASTEROID_KINDS = 3           # Number of size tiers
```

## Optional Logging System

The game includes an optional logging system that tracks:

- **Game State**: Snapshots of all sprites every second (position, velocity, etc.)
- **Game Events**: Specific events like "asteroid_split", "asteroid_shot", "player_hit"

Logs are saved as JSONL files and can be used for:

- Analyzing gameplay patterns
- Debugging collision issues
- Creating gameplay replays
- Performance analysis

To disable logging, remove or comment out the `log_state()` and `log_event()` calls.

## Technical Challenges Solved

1. **Inheritance Architecture**: Created a base `CircleShape` class that all game objects inherit from, reducing code duplication and making collision detection universal.

2. **Sprite Container Pattern**: Used class-level `containers` tuple to automatically add sprites to multiple groups (updatable, drawable, collidable) upon instantiation.

3. **Vector-Based Physics**: Implemented rotation and movement using Pygame's Vector2 class, making physics calculations elegant and readable.

4. **Edge Spawning Algorithm**: Designed a flexible system where asteroids can spawn from any screen edge with appropriate velocity vectors.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Alkin Maystorov**

- GitHub: [@a-maystorov](https://github.com/a-maystorov)
- Portfolio: [alkinmaystorov.com](https://alkinmaystorov.com)
- LinkedIn: [Alkin Maystorov](https://linkedin.com/in/alkin-maystorov)

## Acknowledgments

- Inspired by the 1979 Atari classic _Asteroids_
- Built as part of learning game development with Python and Pygame
- Physics implementation based on vector mathematics principles
- Special thanks to the Pygame community for excellent documentation
