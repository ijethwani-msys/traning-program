from institute import Institute

class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        tranee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        lenght_of_trainer_list = len(trainer_list)
        lenght_of_trainee_list = len(tranee_list)
        remaining_trainee= lenght_of_trainee_list%lenght_of_trainer_list
        # data_dict = {
        #     "trainer_id":self.id
        #     "trainee_list":[

                
        #     ]


        # }


obj = Asignment()
obj.group_creation_with_trainer("Python")


        









