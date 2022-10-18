from institute import Institute

class Asignment(Institute):
    "trainer-->(list of trainee)"
    def group_creation_with_trainer(self,technology_name):
        tranee_list = self.get_trainee_by_technology(technology_name=technology_name)
        trainer_list = self.get_trainer_by_technology(technology_name=technology_name)
        for trainer in trainer_list:
            data_dict = {
                "trainer_id":1992,
                "trainee_list":[23414,23414,23414,23414]
            }


obj = Asignment()
obj.group_creation_with_trainer("Python")


        
# 1 list - 2
# 1 = 1 3 5 7 9 11
# 2 = 2 4 6 8 10 12

# 1 = 1 4 7 10
# 2 = 2 5 8 11
# 3 = 3 6 9 12










