# Mentor-Relate
This the implementation of a course project in SJTU EE359. Contributor Dixi Yao, Chumeng Liang, Kunhong Hao
## Building Environment
The frontend is based on the html and css. The backend and the implementation is based on python3. The required package include follows:
* genism
* spacy
* pickle
* numpy
### Webserver
To run the frontend, you can directly move all files in this repo to htdocs in Apache server. Php environment is required.
### Webcommunicaton
The webcommunicatoin is through socket. The frontend php web send a command to python code client.py and the client.py use the encrypted socket to establish communication with backend main.py to call our algorithm.

To start the system, we need first start main.py at the backend and keep it running. Then start the webserver.
### WebTemplate
The template of the web is based on [Educature](https://colorlib.com/wp/template/educature/)
## Algorithm
Our algorithm is implemented in the backend program main.py. To start up the program you need to download such files.
* script. You need to download the professor list and the trained word2vector model in the folder script. The required files include data.pkl, data2.pkl and GoogleNews-vectors-negative300.bin. You can download first two files from [Jboox Link](https://jbox.sjtu.edu.cn/l/01Hw4D) and word2vec model from  [Jbox Link](https://jbox.sjtu.edu.cn/l/YFgdLD)
* Imgs. You need to download the imgs of professors in the folder image. Each image should have the name the same as data in pickle file with .PNG ending.

You can refer to the datailed explanation of algorithm in our report which will be uploader later
## Acknowledgement
Sincere thanks to professor Liyao Xiang and Dr. Jungang Yang, Dr Hui Xu and Dr Mingze Li for help in this project.