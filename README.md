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

For training yolo

########################################  
0. to learn single images for food go to https://aihub.or.kr/aidata/30747 to download them.
1. to train use command 
python train.py --data DATA --cfg VERSION --weights PRETRAIN --batch-size SIZE
you can refer detail instructions in https://github.com/ultralytics/yolov5
2. KAIST food images are included and you can train them with kama_final.yaml
########################################  

# this project thanks to yolov5, Detectron2 open source    
# its code was edited little bit by my self.  
