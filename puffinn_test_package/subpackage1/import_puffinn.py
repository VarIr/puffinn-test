import puffinn


def print_version():
    print(puffinn.__version__)
    return True


def create_index():
    index = puffinn.Index('angular', 10, 1024 ** 2)
    print(index)
    return True
