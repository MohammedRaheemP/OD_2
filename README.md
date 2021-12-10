# OD_2
Object Detection using YOLOv5x

Dataset Description:

Total images : 2239 (including both person and car)

Total instances from all images :16772 (person ~ 10K, car ~ 6K)

Training description:

Model : YOLO_v5, pretrained weight: yolov5x -extra large ,framework : pytorch, total epochs :300, batch_size :8 , 

Total iterations to complete one epoch: 263(2239/8),

Input image size : 640 pixel, torch version :1.10, GPU core - Tesla K80(Google Colab GPU),

Total layers: 567, Total parameters: 8.8 crores, 

Hyperparameters and Augmentation description: 

lr0=0.01, lrf=0.1, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.5, cls_pw=1.0, obj=1.0, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.0, copy_paste=0.0




