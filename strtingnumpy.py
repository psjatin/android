import numpy as np

jasmin  = np.array([[["roya mai" , "teri saari" ,"batein cudi"],["mil jaye" , "jo bhi" , "raaj tera"],
                     ["tu aata" , "sambhal kr" , "rkha wo"]],[["wo phool","mera tu" , "adhuri si"],["ab hisse" , "rhna tha" ,"bnke hm"]
    ,["pr tu" , "atta nhi " ,"jaata wahin"]]])
rahul = np.array([[[1,2,3] ,[2,3,4] ,[3,4,5]]
                     ,[[5,6,7],[6,7,8],[7,8,9]]])

# print(jasmin)
# print(rahul)

# jasrahul = np.stack((jasmin,rahul) , axis=0)
# jasrahul1 = np.stack((jasmin,rahul) , axis=1)
# jasrahul2 = np.stack((jasmin,rahul) , axis=2)
# print(jasrahul)
# print(jasrahul1)
# print(jasrahul2)

j = np.array([[["a","b","c"] ,["a","b","c"],["a","b","c"]]
                 ,[["a","b","c"],["a","b","c"],["a","b","c"]]])
k = np.array([[[1,2,3] ,[2,3,4] ,[3,4,5]]
                     ,[[5,6,7],[6,7,8],[7,8,9]]])
j1 = np.stack((j ,k) , axis=0)
j2 = np.stack((j ,k) , axis=1)
j3 = np.stack((j ,k) , axis=2)
print(j1)
print("")
print(j2)
print("")
print(j3)

