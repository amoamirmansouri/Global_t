import logging

def cube(x):
    return 2*x

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    format="<%(asctime)s : %(levelno)s  > %(name)s ")
x = 2
logging.warning(f"{x} cube is {cube(x)}")

logging.warning(f"{x} square is {cube(x*2)}")

