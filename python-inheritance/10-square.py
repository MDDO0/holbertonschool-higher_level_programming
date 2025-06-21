import importlib.util
import sys

module_name = "9-rectangle"
spec = importlib.util.spec_from_file_location("Rectangle", "9-rectangle.py")
rectangle_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rectangle_module)
Rectangle = rectangle_module.Rectangle
