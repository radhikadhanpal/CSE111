
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    
    draw_oval(canvas, 100, 450, 200, 400, outline="white", fill="white")
    draw_oval(canvas, 0, 470, 130, 400,  outline="white", fill="white")
    draw_oval(canvas, 750, 470, 650, 400, outline="white", fill="white")


    draw_cloud(canvas, 450, 400, 350)#1
    draw_cloud(canvas, 420, 350, 450)#2
    draw_cloud(canvas, 480, 320, 350)#3
    draw_cloud(canvas, 500, 300, 350)#4
    draw_cloud(canvas, 600, 410, 400)#5
   

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_cloud(canvas, center_x, bottom, height):
    #draw clouds
    cloud_width = height / 7
    cloud_height = height / 5
    left_cloud = center_x - cloud_height
    bottom_cloud = bottom
    right_cloud = center_x + cloud_height
    cloud_top = bottom + cloud_height
    draw_oval(canvas, left_cloud, bottom_cloud, right_cloud, cloud_top, outline="white", fill='white')

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 20
    tree_bottom = 50
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 250
    tree_bottom = 50
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

# Draw another pine tree.
    tree_center_x = 350
    tree_bottom = 50
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)




def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    for x2 in range(25, 900, 55):
        draw_pine_tree(canvas, x2, 100, 170)
        x2 = x2 + 25
        draw_pine_tree(canvas, x2, 100, 150)
        x2 = x2 + 7
        draw_pine_tree(canvas, x2, 100, 140)


    for x1 in range(25, 900, 50):
        draw_pine_tree(canvas, x1, 100, 150)

    for x in range(100, 900, 50):
        #draw_pine_tree(canvas, x, 250, 80)
        x = x + 50
        #draw_pine_tree(canvas, x, 150, 200)
        x = x + 100
        #draw_pine_tree(canvas, x, 100, 200)
        x = x - 200
        draw_pine_tree(canvas, x, 50, 220)
        #draw_pine_tree(canvas, x, 50, 220) #redundint

        

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()
