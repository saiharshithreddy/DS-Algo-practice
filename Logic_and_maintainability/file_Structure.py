# @Author: Sai Harshith
# @Date:   26-May-2020-11-05
# @Last modified by:   Sai Harshith
# @Last modified time: 26-May-2020-12-05



# Filter list of files with size greaterthan 50MB.
from abc import ABC, abstractmethod

class File:
    def _init_(self, ID, size):
        self.fileID = ID
        self.size = size

# abstract class (used for extending functionalities)
class Criteria(ABC):
    @abstractmethod
    def meetcriteria(self, files, size):
        pass

# Greater than file size passed
class greaterThan(Criteria):
    def _init_(self, files, size1):
        self.files = files
        self.size1 = size1

    def meetcriteria(self):
        res = []
        for file in self.files:
            if file.size > self.size1:
                res.append(file)
        return res 

# Lesser than file size passed
class lesserThan(Criteria):
    def _init_(self, files, size1):
        self.files = files
        self.size1 = size1

    def meetcriteria(self):
        res= []
        for file in self.files:
            if file < self.size1:
                res.append(file)
        return res 

# Greater than and lesser than file sizes passed
class greaterandlesser(Criteria):
    def _init_(self, files, size1, size2):
        self.files = files
        self.size1 = size1
        self.size2 = size2

    def meetcriteria(self):
        res = []
        return obj_greaterThan(obj_lesserThan(self.files, self.size1), self.size2)



