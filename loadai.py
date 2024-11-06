import cv2
import numpy as np
import pickle
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load Pokémon data from a file
def load_data_from_file(filename="pokemon.ai"):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

# Reconstruct KeyPoints from serialized data
def reconstruct_keypoints(serialized_keypoints):
    keypoints = []
    for pt in serialized_keypoints:
        keypoints.append(cv2.KeyPoint(x=pt[0][0], y=pt[0][1], size=pt[1], angle=pt[2],
                                      response=pt[3], octave=pt[4], class_id=pt[5]))
    return keypoints

# Function to match an input image against the loaded templates
def match_pokemon(input_image_path, loaded_data, nf = 350):
    input_imagee = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    if input_imagee is None:
        print(f"Error: Could not load input image at {input_image_path}")
        return None
    
    input_image = cv2.bilateralFilter(input_imagee, d=9, sigmaColor=75, sigmaSpace=75) 
    orb = cv2.ORB_create(nfeatures=nf)
    kp_input, des_input = orb.detectAndCompute(input_image, None)

    best_match = None
    best_score = 0
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Helper function for threading
    def match_with_pokemon(pokemon_name, keypoints_descriptors):
        highest_score = 0
        for serialized_keypoints, descriptors in keypoints_descriptors:
            keypoints = reconstruct_keypoints(serialized_keypoints)
            matches = bf.match(des_input, descriptors)
            score = len(matches)
            if score > highest_score:
                highest_score = score
        return pokemon_name, highest_score

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(match_with_pokemon, pokemon_name, keypoints_descriptors)
                   for pokemon_name, keypoints_descriptors in loaded_data.items()]

        for future in as_completed(futures):
            pokemon_name, score = future.result()
            if score > best_score:
                best_score = score
                best_match = pokemon_name

    return best_match, best_score




