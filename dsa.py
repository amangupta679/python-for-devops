# Array is the collection of similar kind of data type 
# list is the collection of different kind of data 



list_of_num = []

print(type(list_of_num))

list_of_num.append(1)
list_of_num.append(2)
list_of_num.append(3)
list_of_num.append("aman")


print(list_of_num)

list_of_cloud = ["aws" , "azure" , "gcp" , "oracle"]
list_of_env = ["dev" , "test" , "product"]
print(list_of_cloud)

print(list_of_cloud[0])

print(range(10))

#list iteration 

for i in range(10):
    print("boom")

for cloud in list_of_cloud:
    print(cloud)

for cloud in list_of_cloud:
    if cloud =="aws":
        print("aws is the best")

# dictonary 

dict_of_cloud = {
    "aws":"amazon web services", 
    "azure":"microsoft azure" , 
    "gcp":"google cloud platformn", 
    



}

print(dict_of_cloud["aws"])
print(dict_of_cloud.get("gcp"))
# writing if else condition as well 
print(dict_of_cloud.get("linode" , "not found"))

dict_of_cloud.update({"linode":"linode cloud"})
print(dict_of_cloud)



