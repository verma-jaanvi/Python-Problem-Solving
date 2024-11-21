import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_doll():
    fig, ax = plt.subplots()

    # Head (Circle)
    head = patches.Circle((0.5, 0.75), 0.1, edgecolor='pink', facecolor='pink')
    ax.add_patch(head)
    
    # Body (Square)
    body = patches.Rectangle((0.35, 0.45), 0.3, 0.2, edgecolor='blue', facecolor='blue')
    ax.add_patch(body)
    
    # Left Arm (Rectangle)
    left_arm = patches.Rectangle((0.2, 0.55), 0.15, 0.05, edgecolor='orange', facecolor='orange')
    ax.add_patch(left_arm)

    # Right Arm (Rectangle)
    right_arm = patches.Rectangle((0.65, 0.55), 0.15, 0.05, edgecolor='orange', facecolor='orange')
    ax.add_patch(right_arm)

    # Left Leg (Rectangle)
    left_leg = patches.Rectangle((0.38, 0.25), 0.08, 0.2, edgecolor='green', facecolor='green')
    ax.add_patch(left_leg)

    # Right Leg (Rectangle)
    right_leg = patches.Rectangle((0.54, 0.25), 0.08, 0.2, edgecolor='green', facecolor='green')
    ax.add_patch(right_leg)

    # Skirt (Triangle)
    skirt = patches.Polygon([[0.35, 0.45], [0.65, 0.45], [0.5, 0.3]], edgecolor='red', facecolor='red')
    ax.add_patch(skirt)
    
    # Set limits and aspect ratio for the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    
    plt.axis('off')  # Turn off the axis
    plt.show()

draw_doll()
