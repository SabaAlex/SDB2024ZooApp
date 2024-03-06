from domain.exceptions import CustomException


class Repository:
    def __init__(self, entities_list):
        self.__entities_list = entities_list

    def __find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return i
        return None

    def add(self, entity):
        position = self.__find_position(entity)
        if position is not None:
            raise CustomException('Entity already exists!')
        self.__entities_list.append(entity)

    def delete(self, entity):
        position = self.__find_position(entity)
        if position is None:
            raise CustomException('Entity does not exist!')
        del self.__entities_list[position]

    def get_all(self):
        return self.__entities_list