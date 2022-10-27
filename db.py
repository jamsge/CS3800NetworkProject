import copy

MEMORY_DB = {}

# load file contents into MEMORY_DB
def load():
    pass

# save MEMORY_DB contents into file
def save():
    pass

# return a deep copy of the in memory DB
def retrieve_all():
    my_copy = copy.deepcopy(MEMORY_DB)
    return my_copy
