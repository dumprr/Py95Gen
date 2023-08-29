# Py95Gen

 Windows 95 Key Generator - but in Python now!

## Download

Warning: These links are raw links, so if you open them, they will just show the code.

To avoid this, right click on the version you want and click "Save link as...". This will save the file as a .py file which you can then run.

 [Windowed](https://github.com/dumprr/Py95Gen/raw/main/gen.py)
 |
 [Console](https://github.com/dumprr/Py95Gen/raw/main/consolegen.py)

## Usage

There are 2 versions: The fully console version and the Window version.

The fully console version is self explanatory; it runs in the console and outputs in the console.

However, the Window version uses `tkinter` to create a windowed experience for the user, with a button and output box.

If it doesn't work, do `pip install tkinter`

## Specifics

The code in the `tkinter`/Windowed version is much cleaner, as the function is not one large "if-else" statement, but rather a function that calls other functions and actually returns the values instead of passing them on. This is much more optimized.

However... the console version itself does not carry this optimization (because I'm too lazy.)
