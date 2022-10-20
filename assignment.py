from institute import Institute
#range(start,stop,step)
# range (count,len(trainee_list),len(trainer_list))
class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        trainee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        count = 0
        trainee_list_data1= []
        trainee_list_data2= []
        trainee_list_data3= []
        trainee_list_data4= []
        final_trainee_list = []
        trainee_list_data_final = []
        data_list = []

        chnaged_value = None
        # while len(trainer_list)>count:
        #     for i in range(len(trainee_list)):
        #         j = count+((i+1)-1)*len(trainer_list) if len(trainer_list)>i else None
        #         if j is not None:
        #             if chnaged_value is not None:
        #                 trainee_list_data.append(trainee_list[j]["traineeId"]) if trainee_list[j]["traineeId"] not in trainee_list_data else "" 
        #                 trainee_list_data_final.append(trainee_list_data)
        #             else:
        #                 trainee_list_data0.append(trainee_list[j]["traineeId"]) if trainee_list[j]["traineeId"] not in trainee_list_data0 else ""  
        #                 trainee_list_data_final.append(trainee_list_data0)
                    
                
        #     data_dict = {
        #         "id":trainer_list[count]["trainerId"],
        #         "trainees":trainee_list_data_final[count+(len(trainer_list)-1)]
        #     }
        #     data_list.append(data_dict)
            
        #     count+=1
        #     chnaged_value = "changed"+str(count)

        while len(trainer_list)>count:
            main_list = list(range(count,len(trainee_list),len(trainer_list)))
            
            for i in main_list:
                if count==0:
                    trainee_list_data1.append(trainee_list[i]["traineeId"])
                    data_list = trainee_list_data1
                elif count==1:
                    trainee_list_data2.append(trainee_list[i]["traineeId"])
                    data_list = trainee_list_data2
                elif count==2:
                    trainee_list_data3.append(trainee_list[i]["traineeId"])
                    data_list = trainee_list_data3
                elif count==3:
                    trainee_list_data4.append(trainee_list[i]["traineeId"])
                    data_list =trainee_list_data4
            trainee_list_data_final.append(data_list)
                

            data_dict = {
                "id":trainer_list[count]["trainerId"],
                "trainee_id_list":trainee_list_data_final[count]
            }
            final_trainee_list.append(data_dict)
            count+=1
        print(final_trainee_list)

        
[{'id': 1992, 'trainee_id_list': [23414, 23418, 23422, 23426]}, {'id': 1855, 'trainee_id_list': [23414, 23418, 23422, 23425]}, {'id': 1856, 
'trainee_id_list': [23416, 23420, 23424]}, {'id': 1857, 'trainee_id_list': [23417, 23421, 23425]}]


{"trainer_id":1,"trainee_id_list":[0,2,4],"trainer_id":2,"trainee_id_list":[1,3]}
# trainee = 10
# trainer = 5
# last_term = first_term + (term)*len(trainer_list)




obj = Asignment()
obj.group_creation_with_trainer("Python")


        
# 1 list - 2
# 1 = 1 3 5 7 9 11
# 2 = 2 4 6 8 10 12

# 1 = 1 4 7 10
# 2 = 2 5 8 11
# 3 = 3 6 9 12






[{'id': 1992, 'trainee_id_list': [23414, 23418, 23422, 23425]}, {'id': 1855, 'trainee_id_list': [23415, 23419, 23423]}, {'id': 1856, 'trainee_id_list': [23416, 23420, 23424]}, {'id': 1857, 'trainee_id_list': [23417, 23421, 23425]}]



