import pygame
import math

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
CUBE_SIZE = 200       # Size of the cube
FOCAL_LENGTH = 200    # Distance from camera to screen

# --- SETUP ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
]

faces = [
    ((0, 1, 2, 3), (255, 255, 255)),   # Back (Red)
    ((4, 5, 6, 7), (255, 255, 255)),   # Front (Green)
    ((0, 1, 5, 4), (255, 255, 255)),   # Bottom (Blue)
    ((2, 3, 7, 6), (255, 255, 255)), # Top (Yellow)
    ((0, 3, 7, 4), (255, 255, 255)), # Left (Cyan)
    ((1, 2, 6, 5), (255, 255, 255))  # Right (Magenta)
]

angle_x = 0
angle_y = 0

# --- MAIN LOOP ---
running = True
while running:
    # 1. Standard Pygame Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20)) #background

    angle_x += 0.01
    angle_y += 0.02


    projected_points = []
    rotated_vertices = []

    for v in vertices:
        x, y, z = v[0] * CUBE_SIZE, v[1] * CUBE_SIZE, v[2] * CUBE_SIZE

        # Rotate around X axis
        y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
        
        # Rotate around Y axis
        x, z = x * math.cos(angle_y) + z * math.sin(angle_y), -x * math.sin(angle_y) + z * math.cos(angle_y)

        # Save rotated 3D coordinate (for depth sorting later)
        rotated_vertices.append((x, y, z))

        # Project to 2D
        z_dist = z + 600 # Move the cube away from the camera
        scale = FOCAL_LENGTH / z_dist
        px = x * scale + WIDTH / 2
        py = y * scale + HEIGHT / 2
        projected_points.append((px, py))

    faces_to_draw = []
    for indices, color in faces:
        # Get the Z coordinate of all 4 corners of this face
        z_coords = [rotated_vertices[i][2] for i in indices]
        avg_z = sum(z_coords) / 4
        
        faces_to_draw.append({
            "indices": indices,
            "color": color,
            "z": avg_z
        })

    # Sort furthest Z first
    faces_to_draw.sort(key=lambda item: item["z"], reverse=True)

    # 5. DRAW EVERYTHING
    for item in faces_to_draw:
        indices = item["indices"]
        color = item["color"]
        
        # Get the 2D points for this face
        points = [projected_points[i] for i in indices]
        
        # Draw only the outline by adding a width (3)
        pygame.draw.polygon(screen, color, points, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


