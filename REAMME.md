# QuickDraw Grid Generator for Pen Plotter

This script generates an SVG grid of normalized drawings using the [Google QuickDraw dataset](https://github.com/googlecreativelab/quickdraw-dataset). The primary purpose of creating this grid is to print the drawings using a pen plotter. The grid consists of 15 columns and 20 rows, with each drawing being the same size and spaced evenly apart. While the default category is set to "coffee cup", you can easily change it to any other category available in the dataset.

## Dependencies

- quickdraw: https://github.com/googlecreativelab/quickdraw-python
- svgwrite: https://github.com/mozman/svgwrite

Install the dependencies using the following commands:




```pip install quickdraw```

```pip install svgwrite```


## Usage

Run the `coffee_cup_grid.py` script:


This will generate an SVG file called `coffee_cup_grid.svg` with a grid of different coffee cup drawings organized in 15 columns and 20 rows.

## Customization

You can customize the grid size, padding between drawings, and image size by modifying the following variables in the `coffee_cup_grid.py` script:

- `image_size`: The size of each drawing within the grid (default: 255)
- `padding`: The space between each drawing in the grid (default: 30)
- `columns`: The number of columns in the grid (default: 15)
- `rows`: The number of rows in the grid (default: 20)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

