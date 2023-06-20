#!/usr/bin/python3
""" class Base """
import csv
import turtle
import json


class Base:
    """private class attribute"""
    __nb_objects = 0
    """class constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """returns the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                dm = cls(1, 1)
            else:
                dm = cls(1)
            dm.update(**dictionary)
            return dm

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Create a turtle object"""
        t = turtle.Turtle()
        t.screen.bgcolor("lightgray")
        t.pensize(5)
        t.shape("turtle")
        # Draw rectangle
        t.bgcolor("red")
        for r in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(r.x, r.y)
            t.down()
            for _ in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
        # Draw squares
        t.bgcolor("orange")
        for s in list_squares:
            t.showturtle()
            t.up()
            t.goto(s.x, s.y)
            t.down()
            for _ in range(4):
                t.forward(s.size)
                t.left(90)
            t.hideturtle()
        t.exitonclick()

    @classmethod
    """writes the JSON string representation of list_objs"""
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        ls = []
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                ls = [n.to_dictionary() for n in list_objs]
                jsfile.write(Base.to_json_string(ls))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                ls = Base.from_json_string(f.read())
                return [cls.create(**d) for d in ls]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                cvsf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                wr = csv.DictWriter(csvf, fieldnames=fieldnames)
                for n in list_objs:
                    wr.writerow(n.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                ls_d = csv.DictReader(csvf, fieldnames=fieldnames)
                ls_d = [dict([r, int(o)] for r, o in d.items())
                        for d in ls_d]
                return [cls.create(**f) for f in ls_d]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
