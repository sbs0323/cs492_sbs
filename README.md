# cs492_sbs
diet_for_kaist_cafeteria  
if you have any questions, contact sbs0323@kaist.ac.kr  
also pretrained_model might be deleted in my google drive, when long time after  

I recommend you do these things in ubuntu 20.04 (my case)  
##########################################  

0. make conda environment   
conda create --name NAME python=3.8  
conda activate NAME  
pip install -r require_sbs.txt  
 
1. download pretrained files ( my google drive links connected )  
python download.py  

2. execute main file  
python CS492_final_sbs.py  

3. manual  
prepare not tilted image of kaist cafeteria food.  

'predict_calories' button is automatically executed    
you can test the images by clicking buttons in order also.    

########################################  

For training yolo [아래 segmentation 트레이닝 가이드라인 참고] 

########################################  
goto cs492_project_training directory
0. to learn single images for food go to https://aihub.or.kr/aidata/30747 to download them.  
다운로드 받아서 머 어떻게? 

1. download kaist food data
python download_data.py, 

2. kama_final.yaml은 어디에 넣고, aihub data는 어디에 활용하고? json2txt_label.py 는 왜 제일 밖에 있고  
3. 걍 python json2txt_label.py ? 에러날거 같은데 , 트레이닝 결과는 어디 생기고, 등등
  종류디텍션이름 : best.pt / 식판디텍션 이름 : base_best.pt
5. 채점할것도 많은데 내가 조교면 걍 이부분 점수 안주고 넘어감. 

#######################################
0. to learn single images for food go to https://aihub.or.kr/aidata/30747 to download them.  
1. to train use command  
python train.py --data DATA --cfg VERSION --weights PRETRAIN --batch-size SIZE  
you can refer detail instructions in https://github.com/ultralytics/yolov5  
2. KAIST food images are included and you can train them with kama_final.yaml  

########################################  

########################################  

For training segmentation  

########################################  
go to directory 'cs492_project/segmentation/'  
1. you can make COCO image datasets[for single croped image] using 'labelme' and 'labelme2coco',   
1-1. i already give some of datasets for users.  
1-2. if you want to put your custom datasets, prepare COCO image dataset[for single croped image] into directory 'cs492_project/segmentation/images'  
2. do not modify detectron2_train.py settings.   
3. just execute  
   python detectron2_train.py  
4. final weight might be in cs492_project/segmentation/output/mode_final.pth  
5. move it to 'cs492_project/' dierectory  
6. Rename it 'model_final_best.pth'  
########################################  

# this project thanks to yolov5, Detectron2 open source    
# its code was edited little bit by my self.  
