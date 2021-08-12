
import dlib
import os
import pandas as pd
import numpy as np
features_known_list=[]
current_frame_face_X_e_distance_list=[]
# current_frame_face_feature_list = [dlib.vector([-0.0426765, 0.0452495, 0.0883809, -0.0199355, -0.0764203, -0.0356452, 0.0323837, -0.0541926, 0.130529, -0.0654639, 0.248604, -0.111745, -0.197794, -0.0584312, -0.027686, 0.0915593, -0.173652, -0.0748117, -0.0412755, -0.0316912, 0.0738874, 0.00112513, -0.00359592, 0.0970978, -0.0714481, -0.339845, -0.0536223, -0.0781099, 0.0557223, -0.102848, 0.0450351, 0.145947, -0.19823, -0.0189848, -0.0125433, 0.0620622, -0.0348409, -0.0546108, 0.208484, -0.038651, -0.181252, 0.00542093, 0.0188412, 0.226898, 0.181234, 0.057051, -0.0499837, -0.0210258, 0.110332, -0.230812, -0.0562494, 0.218979, 0.0148316, 0.0240535, 0.0584929, -0.104397, 0.0233317, 0.0621085, -0.188149, -0.000630416, -0.0256104, -0.117037, 0.0350116, -0.0865637, 0.142863, -0.00478173, -0.0766432, -0.0774343, 0.118518, -0.195465, -0.0231263, 0.127331, -0.118058, -0.188691, -0.238021, 0.0467084, 0.424426, 0.102813, -0.112044, 0.0925275, -0.00525279, -0.0826338, 0.100388, 0.0936747, -0.033115, -0.0168886, -0.0777906, 0.0464816, 0.165514, -0.0130921, -0.00870656, 0.206692, -0.0628786, 0.0141609, 0.0264728, -0.034846, -0.0136247, 0.0394483, -0.110466, 0.0403541, 0.0242469, -0.104827, -0.033976, 0.0441406, -0.188891, 0.0651022, -0.00918286, -0.0399382, -0.0112122, -0.0182418, -0.141598, 0.0124645, 0.166406, -0.307166, 0.200508, 0.159188, -2.57848e-05, 0.123727, 0.0361575, 0.0658762, -0.0126401, -0.0637244, -0.121273, -0.0833351, 0.09394, -0.0278561, 0.0530479, -0.0664664])]

def return_euclidean_distance(feature_1,feature_2):
    feature_1 = np.array(feature_1)
    feature_2 = np.array(feature_2)
    dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
    return dist

def get_face_database():
    global features_known_list
    if os.path.exists("data/features_all.csv"):
        path_features_known_csv = "data/features_all.csv"
        csv_rd = pd.read_csv(path_features_known_csv, header=None)
        for i in range(csv_rd.shape[0]):
            features_someone_arr = []
            for j in range(0, 128):
                if csv_rd.iloc[i][j] == '':
                    features_someone_arr.append('0')
                else:
                    features_someone_arr.append(csv_rd.iloc[i][j])
            features_known_list.append(features_someone_arr)


def main(aaa):
    # print(aaa)
    get_face_database()
    for i in range(len(features_known_list)):
        e_distance_tmp = return_euclidean_distance(aaa,features_known_list[i])
        current_frame_face_X_e_distance_list.append(e_distance_tmp)
    similar_person_num = current_frame_face_X_e_distance_list.index(
                                        min(current_frame_face_X_e_distance_list))    
    # print(similar_person_num)
    return(similar_person_num)

if __name__ == '__main__':
    result = main(current_frame_face_feature_list)
    print(result)