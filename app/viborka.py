import glob
import re
from .need15 import *
#from .needshar import *
#from pymongo import MongoClient


class CheckViborka():
    """docstring for CheckViborka"""
    def __init__(self):
        super(CheckViborka, self).__init__()
        #self.arg = arg
        self.data = {} # Array for output
        self.need_gorod = n_gorod
        self.need_rayon = n_rayon
        self.need_selo = n_selo
	
        self.gorod = {"m18": 0, "m30": 0, "m59": 0, "m60": 0,"w18": 0,"w30": 0,"w59": 0,"w60": 0}
        self.rayon = {"m18": 0,"m30": 0,"m59": 0,"m60": 0,"w18": 0,"w30": 0,"w59": 0,"w60": 0}
        self.selo = {"m18": 0,"m30": 0,"m59": 0,"m60": 0,"w18": 0,"w30": 0,"w59": 0,"w60": 0}
        self.obrazov = {"nach": 0,"obsh": 0,"sred": 0,"prof": 0,"nezvis": 0,"vis": 0}
        self.code_gorod = "552"
        self.code_rayon = "554"
        self.code_selo = "555"
        self.code_woman = "501"
        self.code_man = "500"
        self.code_18 = "505"
        self.code_30 = "506"
        self.code_59 = "507"
        self.code_60 = "508"
        self.code_nach = "510"
        self.code_obsh = "511"
        self.code_sred = "512"
        self.code_prof = "513"
        self.code_nezvis = "514"
        self.code_vis = "515"

    def OpenFiles(self):
        count = 0
        all_list = []
        tmp_list = []
        extensions = glob.glob("in/*.txt") + glob.glob("in/*.yes") + glob.glob("in/*.opr")
        for files in extensions:
            try:
                cur_file = open(files, "r")
            except Exception as e:
                print(e)
            cur_file_list = cur_file.readlines()            
            for line in cur_file_list:

                if re.search("===", line):
                    # print "yep!"
                    break
                if re.search("999", line):                    
                    all_list.append(line)
                    tmp_list.append(line)
                    count = count + 1
            tmp_list = []
        return all_list

    def testinline(self,str1,str2,str3,line):
            return ((str1 in line) and (str2 in line) and (str3 in line))

    def check(self):        
        list = self.OpenFiles()         
        for line in list:
            #print (line)
            if   self.testinline(self.code_man, self.code_18, self.code_gorod, line):
                self.gorod["m18"] = self.gorod["m18"] + 1   #Мужчины город
            elif self.testinline(self.code_man, self.code_30, self.code_gorod, line):
                    self.gorod["m30"] = self.gorod["m30"] + 1
            elif self.testinline(self.code_man, self.code_59, self.code_gorod, line):
                    self.gorod["m59"] = self.gorod["m59"] + 1
            elif self.testinline(self.code_man, self.code_60, self.code_gorod, line):
                    self.gorod["m60"] = self.gorod["m60"] + 1

            elif self.testinline(self.code_woman, self.code_18, self.code_gorod, line):
                self.gorod["w18"] = self.gorod["w18"] + 1 #Женщины город
            elif self.testinline(self.code_woman, self.code_30, self.code_gorod, line):
                    self.gorod["w30"] = self.gorod["w30"] + 1
            elif self.testinline(self.code_woman, self.code_59, self.code_gorod, line):
                    self.gorod["w59"] = self.gorod["w59"] + 1
            elif self.testinline(self.code_woman, self.code_60, self.code_gorod, line): 
                    self.gorod["w60"] = self.gorod["w60"] + 1

            # Район
            elif self.testinline(self.code_man, self.code_18, self.code_rayon, line): 
                self.rayon["m18"] = self.rayon["m18"] + 1 #Мужчины районнный
            elif self.testinline(self.code_man, self.code_30, self.code_rayon, line): 
                self.rayon["m30"] = self.rayon["m30"] + 1
            elif self.testinline(self.code_man, self.code_59, self.code_rayon, line): 
                self.rayon["m59"] = self.rayon["m59"] + 1
            elif self.testinline(self.code_man, self.code_60, self.code_rayon, line): 
                self.rayon["m60"] = self.rayon["m60"] + 1

            elif self.testinline(self.code_woman, self.code_18, self.code_rayon, line): 
                self.rayon["w18"] = self.rayon["w18"] + 1 #Женщины районный           
            elif self.testinline(self.code_woman, self.code_30, self.code_rayon, line): 
                self.rayon["w30"] = self.rayon["w30"] + 1
            elif self.testinline(self.code_woman, self.code_59, self.code_rayon, line): 
                self.rayon["w59"] = self.rayon["w59"] + 1
            elif self.testinline(self.code_woman, self.code_60, self.code_rayon, line): 
                self.rayon["w60"] = self.rayon["w60"] + 1

            # Село
            elif self.testinline(self.code_man, self.code_18, self.code_selo, line): 
                self.selo["m18"] = self.selo["m18"] + 1 #Мужчины село
            elif self.testinline(self.code_man, self.code_30, self.code_selo, line): 
                self.selo["m30"] = self.selo["m30"] + 1
            elif self.testinline(self.code_man, self.code_59, self.code_selo, line): 
                self.selo["m59"] = self.selo["m59"] + 1
            elif self.testinline(self.code_man, self.code_60, self.code_selo, line): 
                self.selo["m60"] = self.selo["m60"] + 1

            elif self.testinline(self.code_woman, self.code_18, self.code_selo, line):
                self.selo["w18"] = self.selo["w18"] + 1 #Женщины село
            elif self.testinline(self.code_woman, self.code_30, self.code_selo, line):
                self.selo["w30"] = self.selo["w30"] + 1
            elif self.testinline(self.code_woman, self.code_59, self.code_selo, line): 
                self.selo["w59"] = self.selo["w59"] + 1
            elif self.testinline(self.code_woman, self.code_60, self.code_selo, line): 
                self.selo["w60"] = self.selo["w60"] + 1
            else: self.errormsg = "Неправильная строка: " + line

            #ОБразование
            if (self.code_nach in line): self.obrazov["nach"] = self.obrazov["nach"] + 1
            if (self.code_obsh in line): self.obrazov["obsh"] = self.obrazov["obsh"] + 1
            if (self.code_sred in line): self.obrazov["sred"] = self.obrazov["sred"] + 1
            if (self.code_prof in line): self.obrazov["prof"] = self.obrazov["prof"] + 1
            if (self.code_nezvis in line): self.obrazov["nezvis"] = self.obrazov["nezvis"] + 1
            if (self.code_vis in line): self.obrazov["vis"] = self.obrazov["vis"] + 1


            all_gorod = self.gorod["m18"] + self.gorod["m30"] + self.gorod["m59"] + self.gorod["m60"] + self.gorod["w18"] + self.gorod["w30"] + self.gorod["w59"] +self.gorod["w60"]
            all_rayon = self.rayon["m18"] + self.rayon["m30"] + self.rayon["m59"] + self.rayon["m60"] + self.rayon["w18"] + self.rayon["w30"] + self.rayon["w59"] + self.rayon["w60"]
            all_selo =  self.selo["m18"] + self.selo["m30"] + self.selo["m59"] + self.selo["m60"] + self.selo["w18"] + self.selo["w30"] + self.selo["w59"] + self.selo["w60"]
            all_ank = all_gorod + all_rayon + all_selo

            self.data = {
                "Город":[
                        ["Мужчина 18-29",self.gorod["m18"],self.need_gorod["m18"]],
                        ["Мужчина 30-49",self.gorod["m30"],self.need_gorod["m30"]],
                        ["Мужчина 50-59",self.gorod["m59"],self.need_gorod["m59"]],
                        ["Мужчина 60",self.gorod["m60"],self.need_gorod["m60"]],
                        ["Женщина 18-29",self.gorod["w18"],self.need_gorod["w18"]],
                        ["Женщина 30-49",self.gorod["w30"],self.need_gorod["w30"]],
                        ["Женщина 50-59",self.gorod["w59"],self.need_gorod["w59"]],
                        ["Женщина 60",self.gorod["w60"],self.need_gorod["w60"]],
                        ["Всего",all_gorod,self.need_gorod["all"]],
                ],
                "Район":[
                        ["Мужчина 18-29",self.rayon["m18"],self.need_rayon["m18"]],
                        ["Мужчина 30-49",self.rayon["m30"],self.need_rayon["m30"]],
                        ["Мужчина 50-59",self.rayon["m59"],self.need_rayon["m59"]],
                        ["Мужчина 60",self.rayon["m60"],self.need_rayon["m60"]],
                        ["Женщина 18-29",self.rayon["w18"],self.need_rayon["w18"]],
                        ["Женщина 30-49",self.rayon["w30"],self.need_rayon["w30"]],
                        ["Женщина 50-59",self.rayon["w59"],self.need_rayon["w59"]],
                        ["Женщина 60",self.rayon["w60"],self.need_rayon["w60"]],
                         ["Всего",all_rayon,self.need_rayon["all"]],
                        ],
                "Село":[
                        ["Мужчина 18-29",self.selo["m18"],self.need_selo["m18"]],
                        ["Мужчина 30-49",self.selo["m30"],self.need_selo["m30"]],
                        ["Мужчина 50-59",self.selo["m59"],self.need_selo["m59"]],
                        ["Мужчина 60",self.selo["m60"],self.need_selo["m60"]],
                        ["Женщина 18-29",self.selo["w18"],self.need_selo["w18"]],
                        ["Женщина 30-49",self.selo["w30"],self.need_selo["w30"]],
                        ["Женщина 50-59",self.selo["w59"],self.need_selo["w59"]],
                        ["Женщина 60",self.selo["w60"],self.need_selo["w60"]],
                         ["Всего",all_selo,self.need_selo["all"]],
                        ],
                "Образование":[
                        ["Начальное",self.obrazov["nach"]*100/all_ank,self.obrazov["nach"]*100/all_ank],
                        ["Основное общее",self.obrazov["obsh"]*100/all_ank,self.obrazov["obsh"]*100/all_ank],
                        ["Среднее", self.obrazov["sred"]*100/all_ank,self.obrazov["sred"]*100/all_ank],
                        ["Профессиональное", self.obrazov["prof"]*100/all_ank,self.obrazov["prof"]*100/all_ank],
                        ["Незаконченное высшее", self.obrazov["nezvis"]*100/all_ank,self.obrazov["nezvis"]*100/all_ank],
                        ["Высшее", self.obrazov["vis"]*100/all_ank,self.obrazov["vis"]*100/all_ank]
                        ]
                        }
                