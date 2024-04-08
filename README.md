#  <p align ="center" height="40px" width="40px"> Action Recognizer </p>

#  <p align ="center" height="40px" width="40px">  AI-powered Action Recognizer🤖 </p>



### <p align ="center"> Implemented using: </p>
<p align ="center">
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="64" height="64" /></a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer">   <img src="https://opencv.org/wp-content/uploads/2022/05/logo.png" width="64" height="64" /></a> 
<a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer">   <img src="https://github.com/prajwal-code2/dogs-emotion/assets/74657725/92956e76-9975-48fe-b253-66073a64aa58" width="128" height="80" /></a>
<a href="https://keras.io/" target="_blank" rel="noreferrer">   <img src="https://github.com/prajwal-code2/dogs-emotion/assets/74657725/ed5ce50e-409e-4d3a-b4fc-f0853efb1bf9" width="128" height="64" /></a>  
</p>

<br>

##     <p align = "left"> Introduction 📚 </p>

This is a real-time python application that recognizes what the person is doing in the video or in front of camera. This application can be installed with cctv cameras to detect if any criminal activity such as burglary, fighting and in such scenarios alarm will get activated. This can be modified for any field where we want to recognize a particular action done by person. The model used in the project is trained on UCF50 dataset where we only used 8 categories for this project. 

<br>

##     <p align = "left">About CNN_Model💻 </p>

The system utilizes the model made on mobilenet. <br>Model uses TimeDistributed mobilenet as its feature extractor followed by TimeDistributed GlobalAveragePooling and Dropout Layer then by two LSTM layers of 128 and 32 units resp. followed by a dense layer of 8 units and activation softmax to determine the action from the video input.<br> Architecture fo the model is given below:<br>


![Screenshot (26)](https://github.com/prajwal-code2/action-recognizer/assets/74657725/19dff47f-7572-4097-a93a-bd8c79f43bd6)


<br>

##     <p align = "left"> Features ⭐ </p>
 -  Real-time human action recognizer.
 -  Can be used for other scenarios where we want to recognize a action after few modification.

<br>

##     <p align = "left"> Installation and Usage 🛠️ </p>
1. Clone this repository to your local machine.
2. Change the directory to action-recognizer so that it will run without any errors.
3. Then install the required packages by running below script
   ```sh
   pip install -r requirement.txt
   ```
4. Download the UCF50 dataset from the link given in dataset folder in the repository.
5. Run each cell of detector.ipynb and save the model in file after training is completed.
6. Then use the model to do inference by running below script
   ```sh
   python test.py
   ```
7. Can check demo video attached below for help.

<br>

##     <p align = "left"> DEMO Video 📹 </p>

<br>





https://github.com/prajwal-code2/action-recognizer/assets/74657725/9efad4d2-2bab-40ac-88ae-1cbf6b8c43bc





<br>

### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>

---


<div align="center">
  Made by <a href="https://github.com/prajwal-code2">Prajwal Joshi</a>
</div>
