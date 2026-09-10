import inspect
import os
from idlelib.sidebar import get_lineno


def export_to_pdf(data):
    println("Exporting to pdf")

def export_to_csv(data):
    println("Exporting to csv")

def export_to_json(data):
    println("Exporting to json")

def export_to_xml(data):
    println("Exporting to xml")

def export_to_html(data):
    println("Exporting to html")

def export_to_pdf(data):
    println("Exporting to pdf")


def get_line_no(frame:inspect.FrameInfo):
    info = inspect.getframeinfo(frame)
    return info.lineno


def make_pretty(func):

    def inner():
        print("Entering '" + func.__name__ + "'")
        line_num = func()
        print("Exiting '" + str(func.__name__) + "': Line ' " + line_num)

    return inner




@make_pretty
def ordinary():
    print("I am ordinary")
    if 1 == 1:
        return get_line_no(inspect.currentframe())


if __name__ == "__main__":

    ordinary()
    if False:
        exit(0)

    data = {1: "one", 2: "two"}

    if format == "pdf":
        export_to_pdf(data)
    elif format == "csv":
        export_to_csv(data);
    elif format == "json":
        export_to_json(data);
    elif format == "xml":
        export_to_xml(data);
    elif format == "html":
        export_to_html(data);
    else:
        ValueError("Format unsupported. Exiting.")
