# Real_Time_Sign_Language_Detection

If you wanted to use NickNochNack's tutorial, make sure to install python 3.8.*.
Here is the code for conda, write them line by line: 

[https://github.com/nicknochnack/RealT...
](https://github.com/nicknochnack/RealTimeObjectDetection.git)

conda create --name tf_env python=3.8

conda activate tf_env

conda install -c conda-forge tensorflow

conda install -c conda-forge protobuf

conda install -c conda-forge pillow lxml jupyter matplotlib

git clone https://github.com/tensorflow/models.git

cd models/research

protoc object_detection/protos/*.proto --python_out=.

cp object_detection/packages/tf2/setup.py .

python -m pip install .

conda install -c conda-forge h5py

![image](https://github.com/PouyaSonej/Real_Time_Sign_Language_Detection/blob/8c4e7aa874baec9233e6c45d347bbd065a4962ad/Real_Time_Sign_Language_Detection/CVzone/Sign%20Language%20Numbers/0to9.png)
