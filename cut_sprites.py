from PIL import Image

def cut_sprite_sheet(image_sheet, sprite_width, sprite_height, output):
    image = Image.open(image_sheet)
    sheet_width, sheet_height = image.size
    counter = 0

    for y in range(0, sheet_height, sprite_height):
        for x in range(0, sheet_width, sprite_width):
            # Define the area to be cut
            area = (x, y, x + sprite_width, y + sprite_height)
            sprite = image.crop(area)
            # Save the sprite
            sprite.save(f"{output}/sprite_{counter}.png")
            counter += 1

cut_sprite_sheet("campfire_sheet.png", 32, 32, "sprites")
