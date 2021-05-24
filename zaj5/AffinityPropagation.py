from sklearn.cluster import AffinityPropagation
from metrics import *

from text_preprocessing import *
from clasters_indexes import *
from parse_file_of_dist import *

if __name__ == '__main__':

    lines_numb = 1700
    del_words = 200
    name = "leven"
    reduced = False
    precomputed = True
    if name == "eucl":
        d = euclidean_distance
    elif name == "dice":
        d = dice_distance
    elif name == "lcs":
        d = lcs_distance
    elif name == "cos":
        d = cos_distance
    elif name == "leven":
        d = levenstein_distance

    Distances = parse_file_of_dist(f"{name}_{'reduced' if reduced else ''}.txt", lines_numb)
    if name == "leven":
        Distances /= np.max(np.abs(Distances))

    with open("lines.txt") as f:
        text = f.read()
    Lines = get_list_of_lines(text, del_words, lines_numb, reduced=reduced)
    Lines = np.asarray(Lines)
    print("Prepocessing done")

    similarity = -1 * Distances
    print(similarity)
    print("Similarity calculated")

    affprop = AffinityPropagation(affinity="precomputed")
    affprop.fit(similarity)

    clusters = []
    centroids = []
    Indexes = []
    Clusterd_TXT = ""
    for cluster_id in np.unique(affprop.labels_):

        cent = Lines[affprop.cluster_centers_indices_[cluster_id]]
        if cent not in centroids:
            centroids.append(cent)
            Indexes.append(np.unique(np.nonzero(affprop.labels_ == cluster_id)[0]))
            cluster = (Lines[Indexes[-1]])

            clusters.append(cluster)
            Clusterd_TXT += f"<<{cent}>>\n"
            Clusterd_TXT += ("**" + "\n** ".join(cluster) + "\n" + "#"*25 + "\n")

    print(Clusterd_TXT)


    print("Clusterizing done")
    print("calculating Davies-Boulding index")
    I_davis_bouldin = davies_bouldin_index(clusters, centroids, d=d, D=Distances, Indexes=Indexes, precomputed=precomputed)
    print("calculating Dunn index\n\n")
    I_Dunn = dunn_index(clusters, centroids, d=d, D=Distances, Indexes=Indexes, precomputed=precomputed)
    comment = f"Lines={lines_numb}\n" + \
              f"metric={name}\n" + \
              f"Deleted words={del_words if reduced else 0}\n" +\
              f"Clusters numb={len(centroids)}\n" +\
              f"Davis-Bouldin index = {I_davis_bouldin}\n" +\
              f"Dunn index = {I_Dunn}"

    print(comment)
    with open(f"Clustered{name}{'_reduced' if reduced else ''}.txt", "a") as f:
        f.write(comment + "\n" + "#"*20 + "\n" + Clusterd_TXT)

