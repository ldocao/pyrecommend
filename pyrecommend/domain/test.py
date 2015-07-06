from atoms import VRating, Rating

dims=[2,3]
v=VRating(dims)
j=0

for i in range(0,dims[0]):
    for j in range(0,dims[1]):
        v[i,j]=Rating(i+j)
    
