import random 
import numpy as py
import copy

#This is a logical abstraction of Cluster.
class Cluster: 
    # Centriod of that Cluster
    # HashTable containing a mapping between points and the distances 
    def __init__(self, dataPoint, pointsandDistance = {}):
        self.centroid = dataPoint
        self.pointsandDistance = pointsandDistance
        
    def getCurrentCentroid(self):
        print "Current centroid for this cluster is - ", self.centroid  
        
    def __repr__(self):
        return '%s %s' % (self.centroid, self.pointsandDistance)
        
#This is a logical abstraction of a Point
class DataPoint:
    #Method to initialize the Tuple (basically the Data Point) 
    def __init__(self, tuple): 
        self.tuple = tuple
    
    #Method to be able to print the Tuple 
    '''Reference: http://stackoverflow.com/questions/1984162/purpose-of-pythons-repr'''
    def __repr__(self):
        return '%s' % self.tuple
    
    #def __eq__(self,other):
        #return self.tuple == other.tuple

#Generate Random Data 
def fireUp(lowerBound, upperBound, maxPoints, numClusters, threshold):
    dataCollection = []
    for i in range(1, maxPoints):
        dataCollection.append(DataPoint([(py.random.uniform(lowerBound,upperBound)) for j in range(2)])) #2D points
        
    #Creating Dictionaries for each of the Clusters. Since they need to operate on that    
    ListofHashtableofDataPoints = []
    
    '''Created a HashTable with the Points and Distance set to ZERO'''
    tempHashTable = {}
    for i in range(len(dataCollection)):
        tempHashTable.update({dataCollection[i]:0}) 
    
    
    '''Deep Copy to Make as many copies as the Number of Clusters we need'''
    for i in range(numClusters):
        ListofHashtableofDataPoints.append(copy.deepcopy(tempHashTable));
         
    print ListofHashtableofDataPoints
    
    #Get three random Centriods
    initialCentroids = random.sample(dataCollection, numClusters)
    print initialCentroids
    
    #numClusters will automatically ensure that the size of ListofHashtableofDataPoints and initialCentroids is same.
    clusterList = []
    for i in range(len(ListofHashtableofDataPoints)):
        clusterList.append(Cluster(initialCentroids[i], ListofHashtableofDataPoints[i]));
        
    print clusterList

    flag = True;
    #Calling the KMeans Algorithm
    '''kMeansAlgo(clusterList, threshold, flag)'''
    
    
    # Experimental Code to Learn Python
    x = {}
    x.update({dataCollection[0] : 10})
    print x
    x.update({dataCollection[0] : 11})
    print x
    '''
    c = Cluster(dataCollection[0], x)
    if(10 == x.get(dataCollection[0])):
        print "We Are good"

    for k in sorted(x.keys()):
        if(dataCollection[0] == k):
            print "even better"
    c.getCurrentCentroid()    
    print dataCollection[0]
    '''

    
def main():
    #numDimensions = int (raw_input("Enter number of Dimensions N:\n"))
    lowerBound = 1 #int (raw_input("Enter the lowerBound for DataGenerationN: \n"))
    upperBound = 2 #int (raw_input("Enter the upperBound for DataGenerationN: \n"))
    maxPoints = 10 #int (raw_input("Enter the maxPoints for DataGenerationN:\n"))
    numClusters = 3 #int (raw_input("Enter the number of Clusters :\n")) 
    threshold = 0.2
    
    fireUp(lowerBound, upperBound, maxPoints, numClusters, threshold)
    
if __name__ == "__main__":
    main()
    