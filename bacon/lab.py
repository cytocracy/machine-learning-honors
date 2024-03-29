import json

def make_actor_dictionary(data):
    actors = {}
    for actorPair in data:
        actor0 = actorPair[0]
        actor1 = actorPair[1]
        if actor0 in actors:
            actors[actor0].append(actor1)
        else:
            actors[actor0] = [actor1]

        if actor1 in actors:
            actors[actor1].append(actor0)
        else:
            actors[actor1] = [actor0]
    return actors

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    actors = make_actor_dictionary(data)
    return actor_id_2 in actors[actor_id_1] or actor_id_1 in actors[actor_id_2]

def get_actors_with_bacon_number(data, n):
    actors = make_actor_dictionary(data)
    visited = set()
    q = [(4724, 0)]
    returns = set()
    while q:
        actor, bacon_number = q.pop(0)
        if actor not in visited:
            visited.add(actor)

            if bacon_number == n:
                returns.add(actor)
                continue
            for neighbor in actors[actor]:
                q.append((neighbor, bacon_number + 1))
    return returns

def get_bacon_path(data, actor_id):
    return get_path(data, 4724, actor_id)

def get_path(data, actor_id_1, actor_id_2):
    actors = make_actor_dictionary(data)
    visited = set()
    q = [(actor_id_1, [actor_id_1])]
    while q:
        actor, path = q.pop(0)
        if actor not in visited:
            visited.add(actor)
            if actor == actor_id_2:
                return path
            for neighbor in actors[actor]:
                q.append((neighbor, path + [neighbor]))

def actor_path(data, path):
    
    actor_path = []
    with open("resources/IDToName.json") as f:
        IDToName = json.load(f)
    for actor in path:
        actor_path.append(IDToName[str(actor)])
    return actor_path

def get_movie_path(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    with open("resources/tiny.json") as f:
        data = json.load(f)
    print(actor_path(data, get_bacon_path(data, 46866)))
