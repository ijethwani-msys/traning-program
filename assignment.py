import json
from institute import Institute
class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        trainee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        count = 0
        final_main_list = []
        final_trainee_list = []
        while len(trainer_list)>count:
            main_list = list(range(count,len(trainee_list),len(trainer_list)))
            count+=1
            final_main_list.append(main_list)
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
        with open("asingment.json","w") as file:
            data = json.dumps(final_trainee_list)
            file.write(data)
        return print("Trainee Asigned Sucessfully")