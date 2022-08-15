import pickle


def save(obj_to_save, filename):
    with open(filename, "wb") as my_file:
        pickle.dump(obj_to_save, my_file)


def load(filename):
    with open(filename, "rb") as my_file:
        return pickle.load(my_file)

