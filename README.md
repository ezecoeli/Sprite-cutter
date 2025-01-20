# Sprite Slicer

This program uses the **Pillow** library in Python to split a sprite sheet into multiple individual files based on the size of each sprite.

---

## Features

- Automatically slices sprite sheets into equal parts.
- Saves each sprite as a separate file.
- Customizable for different sprite sizes.

---

## Parameters

- Defines the path of the sprite sheet (e.g. `"player.png"`).
- Defines the width of each sprite in pixels.
- Defines the height of each sprite in pixels.
- Defines the folder where the sliced ​​sprites will be saved.

---

## Input Example

- Sprite sheet: `160x256 pixels`.
- Layout: `5 columns and 8 rows`.
- Size of each sprite: `32x32 pixels`.

```python
cut_sheet_sprites("sheet_sprites.png", 32, 32, "sprites")
```

---

## Requirements

- Python 3.x
- Pillow Library

---

## Notes

1. Make sure the output folder exists before running the program. If it doesn't, you can create it automatically:

```python
import os
if not os.path.exists("sprites"):
os.makedirs("sprites")
```

2. If the sprite dimensions do not evenly divide the sheet dimensions, the excess edges will not be processed.
