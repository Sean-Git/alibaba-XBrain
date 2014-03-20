alibaba-XBrain
==============

This is a workshop for XBrain.

1. '/data/t_alibaba_data.csv' is the original data file;
2. '/data/train.csv' contains original data for training;(month 4 to 7)
3. '/data/test.csv' contains original data for testing;(month 8)
4. '/src/pre_data.py' is the python script used for getting 'train.csv' and 'test.csv';(unnecessary now)
5. '/src/build_truth.py' is used for building the 'groundtruth.txt' file;
6. '/src/build_index.py' is used for building the 'user_id.txt' and 'brand_id.txt' files;
7. '/src/build_behavior_matrix.py' is used for building the 'behavior_matrix.txt';
8. '/src/kNN.py' provides basic methods like kNN-find and topN-votes;
9. '/src/predict.py' combine the tools and files above to give a prediction 'predict.txt';
10. '/src/evaluate.py' is used for evaluating the performance of algorithm;
11. '/result/groundtruth.txt' is generated easily and '/result/predict.txt' is our algorithm's output; (now these two files are just model);
12. '/docs/Initial Algorithm.pdf' is a descriptor of the inital designed algorithm;

To do:
  Design algorithm and give a proper 'predict.txt' file ASAP. 
  
By Sean.
