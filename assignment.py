from datetime import datetime
import json
from institute import Institute
class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        trainee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        final_main_list = []
        final_trainee_list = []
        count = 0
        while len(trainer_list)>count:
            main_list = list(range(count,len(trainee_list),len(trainer_list)))
            count+=1
            final_main_list.append(main_list)
        count = 0
        while(len(trainer_list))>count:
            for main_list in final_main_list:
                if count==final_main_list.index(main_list):
                    data_dict = {
                        "id":trainer_list[count],
                        f"trainee_list{count}":[]

                        }
                    for i in main_list:
                        data_dict[f"trainee_list{count}"].append(trainee_list[i])
            final_trainee_list.append(data_dict)

            count+=1
        with open("asingment.json","w",encoding="utf-8") as file:
            data = json.dumps(final_trainee_list)
            file.write(data)
        return print("Trainee Asigned Sucessfully")

    def give_asignement(self,trainer_id,asingment_title,asignment_description,submit_date,points):
        with open("asingment.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            for object in data:
                for key in object:
                    if "trainerId" in object[key]:
                        if object[key]["trainerId"]==int(trainer_id):
                            object["asingment"]={"asignment_title":asingment_title,"asignment_description":asignment_description,"points":points,"last_date_for_submition":submit_date,"start_date":datetime.today().strftime("%d/%b/%Y")}
                            print("Asingment Alloted Sucessfully!")
                        else:
                            print("not found")
                        
                
                            
                        
 
    


                        


                      







obj = Asignment()
obj.give_asignement("1855")             
                    

                

