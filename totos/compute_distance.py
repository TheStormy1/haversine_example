from haversine import haversine
"""
this module will compute distances.
"""
def compute_distance(first_place: str, second_place: str) -> float:

    """
    Takes two adresses and returns a distance in kms (float)
    """

    return haversine(first_place, second_place)