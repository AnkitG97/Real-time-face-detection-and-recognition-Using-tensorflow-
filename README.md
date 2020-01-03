# Real-time-face-detection-and-recognition-Using-tensorflow-


1. python xml_to_csv.py -i /Users/koool_ag/test/images/Source\ code/workspace/training_demo/images/test -o /Users/koool_ag/test/images/Source\ code/workspace/training_demo/annotations/test_labels.csv 

2. python generate_tfrecord.py --csv_input=/Users/koool_ag/test/images/Source\ code/workspace/training_demo/annotations/test_labels.csv --output_path=/Users/koool_ag/test/images/Source\ code/workspace/training_demo/annotations/test.record --img_path=/Users/koool_ag/test/images/Source\ code/workspace/training_demo/images/test

3. python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_inception_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-814 --output_directory trained-inference-graphs/output_inference_graph_v1.pb

4. python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_inception_v2_coco.config
