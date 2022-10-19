from institute import Institute

class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        trainee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        count = 0
        trainee_list_data = []
        trainee_list_data0 = []
        trainee_list_data_final = []
        data_list = []
        chnaged_value = None
        while len(trainer_list)>count:
            for i in range(len(trainee_list)):
                j = count+((i+1)-1)*len(trainer_list) if len(trainer_list)>i else None
                if j is not None:
                    if chnaged_value is not None:
                        trainee_list_data.append(trainee_list[j]["traineeId"]) if trainee_list[j]["traineeId"] not in trainee_list_data else "" 
                        trainee_list_data_final.append(trainee_list_data)
                    else:
                        trainee_list_data0.append(trainee_list[j]["traineeId"]) if trainee_list[j]["traineeId"] not in trainee_list_data0 else ""  
                        trainee_list_data_final.append(trainee_list_data0)
                    
                
            data_dict = {
                "id":trainer_list[count]["trainerId"],
                "trainees":trainee_list_data_final[count+(len(trainer_list)-1)]
            }
            data_list.append(data_dict)
            
            count+=1
            chnaged_value = "changed"+str(count)

        return print(data_list)


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










