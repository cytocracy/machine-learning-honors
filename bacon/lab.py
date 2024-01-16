import json

def make_actor_dictionary(data):
    raise NotImplementedError("Implement me!")

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

def get_actors_with_bacon_number(data, n):
    raise NotImplementedError("Implement me!")

def get_bacon_path(data, actor_id):
    raise NotImplementedError("Implement me!")

def get_path(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

def actor_path(data, path):
    raise NotImplementedError("Implement me!")

def get_movie_path(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    with open("resources/movieToID.json") as f:
        data = json.load(f)
    print(data)
