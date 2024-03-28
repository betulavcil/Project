# ÖRNEK ÇALIŞMA
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import euclidean_distances
import pylab
from scipy.cluster import hierarchy


X = customers[['Annual Income (k$)','Spending Score (1-100)']]
scaler = StandardScaler() 
# Scaling and assigning the scaled features to feature_mtx variable
feature_mtx = scaler.fit_transform(X)
feature_mtx[0:5]

# Calculating the distance matrix based on the euclidean distance between datapoints
dist_matrix = euclidean_distances(feature_mtx,feature_mtx) 
print(dist_matrix)
Z_using_dist_matrix = hierarchy.linkage(dist_matrix, 'ward')


#Dendrogram visualization:

# Creating a hierarchical clustering linkage matrix using the complete-linkage method
Z_using_dist_matrix = hierarchy.linkage(dist_matrix, 'ward')

# Define the leaf label function to include 'Age' and 'Annual Income'
def llf(id):
    age = int(customers['Age'][id])
    income = int(customers['Annual Income (k$)'][id])
    return '[%s %s %s]' % (customers['Age'][id], customers['Annual Income (k$)'][id], customers['Gender'][id])

# Vertical dendrogram
fig = plt.figure(figsize=(18, 50))
dendrogram = hierarchy.dendrogram(Z_using_dist_matrix, leaf_label_func=llf, orientation='right')

# Increase the size and boldness of y-axis labels
plt.tick_params(axis='y', labelsize=8)

# Make y-axis labels bold
for label in plt.gca().get_yticklabels():
    label.set_fontweight('bold')
    
plt.title('Dendrogram', fontsize=20)
plt.xlabel('Euclidean Distance', fontsize=15)
plt.ylabel('Customers', fontsize=15)
plt.show()




aggCluster = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
labels = aggCluster.fit_predict(dist_matrix)

labels


# Adding the cluster labels as a new column to our dataframe
customers['cluster_'] = labels
customers.head()

#Visualizing Clusters:


# Visualize the clusters
plt.figure(figsize=(12, 8))

# Scatter plot for each cluster
for cluster_num in range(5):
    plt.scatter(X[labels == cluster_num]['Annual Income (k$)'], 
                X[labels == cluster_num]['Spending Score (1-100)'],
                label=f'Cluster {cluster_num}')

plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()




# To see the gender distribution in each cluster
customers.groupby(['cluster_','Gender'])['cluster_'].count()


# Now we can look at the characteristics of each cluster:

clusters_Stat = customers.groupby(['cluster_', 'Gender'])[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
clusters_Stat


#Let's interpret the above table:

# Men:

# Cluster 0: with the most Annual Income on average.
#Cluster 1: with the most Average Age , but the least Spending Score and Annual Income.
#Cluster 3: with the most Spending Score.

#Women:

#Cluster 0: with the most Annual Income on average, the most Spending Score
#Cluster 1: with the most Average Age , but the least Spending Score and one of the least Annual Incomes.
#Cluster 4: with the most Spending Score, yet the least Annual Incomes.
#Please notice that we did not use Gender and Age of customers in the clustering process, 
#but Hierarchical clustering could forge the clusters and discriminate them with quite a high accuracy.
















