


class Job :

    def __init__(self, id : int, duree : list[int]) -> None:
        self.id = id
        self.duree = duree
        self.nb_machine = len(duree)
        self.debut = [None] * self.nb_machine
        

    def __str__(self) -> str:
        result = ''
        result += f"Job n°  {self.id} de durée totale {sum(self.duree)}: \n \n"

        
        for index, (duree, debut) in enumerate(zip(self.duree, self.debut)):
            
            result += f"  opération n° {index} : durée = {duree} démarre à {debut} \n"
        
        return result


    def __hash__(self):
        return id

    
    def set_debut(self, machine : int, debut: int) -> None:
        self.debut[machine] = debut


    def reset_debut(self) -> None:
        '''
        Remet à None toutes les valeur de la liste debut
        '''

        self.debut = [None] * self.nb_machine
    

    def copy(self):
        return Job(self.id, self.duree)
