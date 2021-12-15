import os
import glob
import json
import sys
jsonfolder = sys.argv[1]
txtfolder = sys.argv[2]
class FindID :
    def __init__(self, path, txtpath):
        self.path = path       #폴더들 주소
        self.txtpath = txtpath
        self.json_list = []    #폴더들에서 json파일만 뽑아서 저장
        self.file_dic = {}     #모든 폴더와 폴더경로안의 파일들을 정리해놓은 사전.
        self.output_dic = {}   #마지막 출력을 위해서 key->json파일이름, value->각각의ID를 저장시킬거임. 

        self.add_files(path)   #file_dic사전만들기 시작
        self.creat_output(txtpath)    #출력할 내용을 정리하는 output_dic에 값을 넣어주는 함수.

    def my_list(self, file_path):
        '''
            폴더안의 파일들을 리스트로 정리해서 return 해준다.
            glob함수는 폴더경로를 이용해 그안에 있는 모든 파일을 출력해준다.
        '''
        file_list = glob.glob(file_path + "/*")
        return file_list
    
    def check_json(self, file_name):
        '''
            만약 json파일까지 도달했다면(파일이름이 .json으로 끝난다면), 그 json파일은 json_list에 저장하고,
            아직 폴더가 남았다면, 다시 add_files()를 호출해서 file_dic사전에 추가정리. 
        '''
        if(self.file_dic[file_name][0].endswith(".json")):
            self.json_list.extend(self.file_dic[file_name])
        else:
            for name in self.file_dic[file_name]:
                self.add_files(name)

    def add_files(self, file_path):
        '''
            main함수
            my_list로 폴더안의 파일리스트를 받아서 file_dic에 저장.
            그리고 json 파일까지 도달했는지 체크한다.
        '''
        self.file_dic[file_path] = self.my_list(file_path)
        self.check_json(file_path)

    def creat_output(self, txtpath):
        '''
            이제 다 뽑아낸 json_list(시리얼넘버)들로 각각의 json파일안의 'sampleId'의 value값을 뽑아,
            output_dic사전에 저장한다. 
        '''
        for filename in self.json_list:
            with open(filename, 'r',) as file:
                json_data_l = json.load(file)
            new_name = json_data_l[0]['Code Name'].rstrip('.jpg')+'.txt'
            new_label = txtpath +  new_name
            f = open(new_label, 'w')
            for json_data in json_data_l:
                cls = int(json_data['Cat 1'])
                width = float(json_data['W'])
                height = float(json_data['H'])
                point = json_data['Point(x,y)']
                pointlist = point.split(',')
                x = float(pointlist[0])
                y = float(pointlist[1])
                f.write("%i %f %f %f %f\n"%(cls,x,y,width,height))


FindID(jsonfolder, txtfolder)
