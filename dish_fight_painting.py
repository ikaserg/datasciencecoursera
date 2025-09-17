#!/usr/bin/env python3
"""
Fight of Dishes - Digital Painting
A creative visualization of dishes in an epic battle!
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
import random

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Kitchen background
def create_kitchen_background():
    # Kitchen counter
    counter = patches.Rectangle((0, 0), 10, 2, linewidth=0, facecolor='#8B4513', alpha=0.7)
    ax.add_patch(counter)
    
    # Backsplash
    backsplash = patches.Rectangle((0, 2), 10, 6, linewidth=0, facecolor='#F5F5DC', alpha=0.8)
    ax.add_patch(backsplash)
    
    # Cabinet lines
    for i in range(1, 10):
        ax.plot([i, i], [2, 8], 'k-', alpha=0.3, linewidth=1)
    
    # Floor tiles
    for i in range(0, 10, 2):
        for j in range(0, 2, 1):
            tile = patches.Rectangle((i, j), 2, 1, linewidth=1, 
                                   facecolor='#D2691E' if (i+j) % 4 == 0 else '#CD853F', 
                                   edgecolor='black', alpha=0.6)
            ax.add_patch(tile)

# Dish characters
class DishFighter:
    def __init__(self, x, y, dish_type, color, size=0.8):
        self.x = x
        self.y = y
        self.dish_type = dish_type
        self.color = color
        self.size = size
        self.angle = 0
        self.anger_level = random.uniform(0.3, 1.0)
        
    def draw(self):
        if self.dish_type == "plate":
            # Main plate body
            plate = patches.Circle((self.x, self.y), self.size, 
                                 facecolor=self.color, edgecolor='black', linewidth=2)
            ax.add_patch(plate)
            
            # Plate rim
            rim = patches.Circle((self.x, self.y), self.size * 0.8, 
                               facecolor='white', edgecolor='black', linewidth=1)
            ax.add_patch(rim)
            
            # Angry eyes
            eye1 = patches.Circle((self.x - 0.3, self.y + 0.2), 0.1, 
                                facecolor='red', edgecolor='black')
            eye2 = patches.Circle((self.x + 0.3, self.y + 0.2), 0.1, 
                                facecolor='red', edgecolor='black')
            ax.add_patch(eye1)
            ax.add_patch(eye2)
            
            # Angry eyebrows
            ax.plot([self.x - 0.4, self.x - 0.2], [self.y + 0.4, self.y + 0.3], 
                   'k-', linewidth=3)
            ax.plot([self.x + 0.2, self.x + 0.4], [self.y + 0.3, self.y + 0.4], 
                   'k-', linewidth=3)
            
            # Angry mouth
            mouth = patches.Arc((self.x, self.y - 0.2), 0.6, 0.3, 
                              angle=0, theta1=0, theta2=180, 
                              linewidth=3, color='red')
            ax.add_patch(mouth)
            
        elif self.dish_type == "bowl":
            # Bowl body
            bowl = patches.Wedge((self.x, self.y), self.size, 0, 180, 
                               facecolor=self.color, edgecolor='black', linewidth=2)
            ax.add_patch(bowl)
            
            # Bowl interior
            interior = patches.Wedge((self.x, self.y), self.size * 0.7, 0, 180, 
                                   facecolor='white', edgecolor='black', linewidth=1)
            ax.add_patch(interior)
            
            # Determined eyes
            eye1 = patches.Circle((self.x - 0.25, self.y + 0.1), 0.08, 
                                facecolor='blue', edgecolor='black')
            eye2 = patches.Circle((self.x + 0.25, self.y + 0.1), 0.08, 
                                facecolor='blue', edgecolor='black')
            ax.add_patch(eye1)
            ax.add_patch(eye2)
            
            # Determined mouth
            ax.plot([self.x - 0.3, self.x + 0.3], [self.y - 0.1, self.y - 0.1], 
                   'k-', linewidth=2)
            
        elif self.dish_type == "cup":
            # Cup body
            cup = patches.Rectangle((self.x - 0.3, self.y - 0.2), 0.6, 0.8, 
                                  facecolor=self.color, edgecolor='black', linewidth=2)
            ax.add_patch(cup)
            
            # Cup handle
            handle = patches.Arc((self.x + 0.3, self.y), 0.4, 0.4, 
                               angle=0, theta1=270, theta2=90, 
                               linewidth=3, color='black')
            ax.add_patch(handle)
            
            # Steam from hot beverage
            for i in range(3):
                steam_x = self.x + random.uniform(-0.2, 0.2)
                steam_y = self.y + 0.4 + i * 0.2
                ax.plot([steam_x, steam_x + random.uniform(-0.1, 0.1)], 
                       [steam_y, steam_y + 0.1], 'gray', linewidth=2, alpha=0.7)
            
            # Focused eyes
            eye1 = patches.Circle((self.x - 0.15, self.y + 0.1), 0.06, 
                                facecolor='green', edgecolor='black')
            eye2 = patches.Circle((self.x + 0.15, self.y + 0.1), 0.06, 
                                facecolor='green', edgecolor='black')
            ax.add_patch(eye1)
            ax.add_patch(eye2)
            
            # Focused mouth
            ax.plot([self.x - 0.2, self.x + 0.2], [self.y - 0.05, self.y - 0.05], 
                   'k-', linewidth=2)

# Create fighting dishes
fighters = [
    DishFighter(2, 4, "plate", "#FF6B6B", 0.8),  # Red angry plate
    DishFighter(8, 4, "bowl", "#4ECDC4", 0.8),   # Teal determined bowl
    DishFighter(5, 6, "cup", "#45B7D1", 0.7),    # Blue focused cup
    DishFighter(3, 6, "plate", "#96CEB4", 0.7),  # Green plate
    DishFighter(7, 6, "bowl", "#FFEAA7", 0.7),   # Yellow bowl
]

# Fighting elements
def add_fighting_elements():
    # Flying utensils
    utensils = [
        ("fork", 1.5, 5.5, 45),
        ("knife", 8.5, 5.5, -45),
        ("spoon", 4.5, 7, 0),
        ("fork", 6.5, 7, 180),
    ]
    
    for utensil, x, y, angle in utensils:
        if utensil == "fork":
            # Draw fork
            ax.plot([x, x], [y-0.3, y+0.3], 'silver', linewidth=4)
            ax.plot([x-0.1, x+0.1], [y+0.3, y+0.3], 'silver', linewidth=2)
            ax.plot([x-0.05, x+0.05], [y+0.2, y+0.2], 'silver', linewidth=2)
        elif utensil == "knife":
            # Draw knife
            ax.plot([x, x], [y-0.3, y+0.3], 'silver', linewidth=4)
            ax.plot([x-0.1, x+0.1], [y-0.3, y-0.3], 'silver', linewidth=6)
        elif utensil == "spoon":
            # Draw spoon
            ax.plot([x, x], [y-0.2, y+0.3], 'silver', linewidth=4)
            circle = patches.Circle((x, y+0.1), 0.15, facecolor='silver', edgecolor='black')
            ax.add_patch(circle)
    
    # Action lines and motion effects
    for i in range(5):
        x1 = random.uniform(1, 9)
        y1 = random.uniform(3, 7)
        x2 = x1 + random.uniform(-1, 1)
        y2 = y1 + random.uniform(-1, 1)
        ax.plot([x1, x2], [y1, y2], 'red', linewidth=2, alpha=0.6)
    
    # Steam and smoke effects
    for i in range(8):
        x = random.uniform(2, 8)
        y = random.uniform(4, 7)
        ax.plot([x, x + random.uniform(-0.3, 0.3)], 
               [y, y + random.uniform(0.2, 0.5)], 
               'gray', linewidth=1, alpha=0.5)

# Create the painting
def create_painting():
    # Clear the axis
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add background
    create_kitchen_background()
    
    # Add fighting elements
    add_fighting_elements()
    
    # Draw all fighters
    for fighter in fighters:
        fighter.draw()
    
    # Add title
    ax.text(5, 7.5, "FIGHT OF DISHES!", fontsize=24, fontweight='bold', 
            ha='center', va='center', color='darkred',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.8))
    
    # Add dramatic lighting effect
    for i in range(20):
        x = random.uniform(0, 10)
        y = random.uniform(0, 8)
        size = random.uniform(0.1, 0.3)
        alpha = random.uniform(0.1, 0.3)
        circle = patches.Circle((x, y), size, facecolor='yellow', alpha=alpha)
        ax.add_patch(circle)

# Create the static painting
create_painting()

# Save the painting
plt.tight_layout()
plt.savefig('/workspace/fight_of_dishes.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("🎨 'Fight of Dishes' painting created and saved as 'fight_of_dishes.png'!")
print("The painting features:")
print("• Angry plates with red eyes and scowling faces")
print("• Determined bowls ready for battle")
print("• Focused cups with steam rising from their hot contents")
print("• Flying utensils as weapons")
print("• Action lines and dramatic lighting effects")
print("• A kitchen battlefield setting")