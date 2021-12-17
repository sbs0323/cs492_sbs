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

3. execution guideline
first of all prepare not tilted image of kaist cafeteria food.  

'predict_calories' button is automatically executed    
you can test the images by clicking buttons in order also.    

########################################  

# For training yolo 

########################################  

0. to learn single images for food go to https://aihub.or.kr/aidata/30747 to download them.
   you should unzip and use json2txt_labe.py to change labeling format.
   type python json2txt_label.py [AI hub label directory] cs492_project_training/datasets/[Directory Name]/labels
   Also, image files should be moved to cs492_project_training/datasets/[Directory Name]/images

   to download kaist food data python download_data.py and unzip them
   
1. to train use command
  python train.py --data [DATA] --cfg [VERSION] --weights [PRETRAIN] --batch-size [SIZE]
  commands that we used are following
  for AI hub: python train.py --data food.yaml --cfg yolov5s --weights '' 
  for KAIST images: python train.py --data kama_final.yaml --weights [AIhub bets.pt directory] 
  you can refer detail instructions in https://github.com/ultralytics/yolov5

2. If you didn't add parameter for directory for results, it will be saved in ./runs/train/
   Best model is saved as "best.pt
   
3. KAIST food images are included and you can train them with kama_final.yaml
   AI hub images can be trained with food.yaml


########################################  

# For training segmentation  

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
