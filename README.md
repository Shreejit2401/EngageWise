# EngageWise 
Monitoring Alertness and Wellbeing in Digital WorkSpace

**ABSTRACT**
--

As final-year students approaching our time to work in a continuous, streamlined environment that requires a lot of focus to get things done, we often find ourselves procrastinating and losing focus or attention sitting in front of a computer or a laptop. Such real-life incidents have inspired us to develop an assistant that uses real-time video to generate a detailed report on how attentive a person sitting in front of the computer is while working or studying. We decided to name this AI assistant EngageWise to reflect its mission of fostering focused and informed engagement during work and study sessions. EngageWise is designed to assist individuals in maintaining their attention and productivity, ultimately helping them achieve their goals efficiently in a world full of distractions.

**PROJECT OBJECTIVES**
--

1. **Comprehensive Focus Analysis:** In-depth scrutiny of an individual's concentration and attention levels, providing a detailed understanding of their cognitive engagement.
2. **Real-time Reporting:** Continuous and immediate delivery of performance feedback, enabling users to make timely adjustments and improvements.
3. **Accurate Distraction Detection:** Precise identification of diversions or interruptions in the user's workflow or task, facilitating focused productivity.
4. **User Flexibility:** A system designed to accommodate individual preferences and adapt to varying user needs and requirements.
5. **Informative Visualization:** Presenting data in visually appealing and insightful formats, enhancing comprehension and decision-making.
6. **User-Friendly Interface:** An intuitive and easily navigable design that ensures a seamless and enjoyable user experience.
7. **Long-term Progress Tracking:** Consistent monitoring and recording of an individual's performance trends over an extended period, enabling goal setting and growth assessment.
8. **Data Privacy and Security:** A robust commitment to safeguarding user data, ensuring confidentiality, and protecting against unauthorized access or breaches.

**PROJECT OUTCOMES**
--

1. **Real-time Distraction Detection:** The system accurately identifies and alerts users in real-time when they exhibit signs of distraction, such as frequent blinking or yawning during tasks.
2. **Enhanced User Productivity:** Users experience improved productivity and focus through proactive notifications on the screen and awareness of their attentiveness levels with the values.
3. **Alarm System** : EngageWise performs comprehensive calculations summarizing users' drowsiness patterns, and alerts them if they are drowsy for more than 10 seconds.
4. **Privacy-Centric Design:** EngageWise ensures stringent adherence to data privacy and ethical guidelines, safeguarding user information and upholding anonymity while collecting attention-related data, ensuring user trust and compliance with privacy regulations.
5. **Wide Applicability:** EngageWise caters to a diverse user base, including students, professionals, teachers, and gamers, by offering a versatile solution for monitoring and enhancing concentration during various activities.

# **INTRODUCTION**

_You don't need more time; you need more focus!_ is a powerful quote by the author and entrepreneur Jesse Itzler. As students, we sometimes find it hard to focus on our work, be it studying for exams or working on a project on a computer or laptop. We often get distracted by other elements on our screens, toggling between pages and app icons. This behavior wastes time and hampers our attentiveness.

We came up with the idea of building a focus app that analyses how attentive the person is based on their facial movements and gestures and generates a report after the end of the session.

**1.1) Existing Model:**

The existing models for an attention or focus detection systems are spread across various domains like attention heatmaps, pupil tracking, Eye Aspect Ratio (EAR), drowsiness detection systems and EEG based attention detection systems.

**1. Attention Heatmaps:** These models involve creating heatmaps of where a person's gaze or attention is concentrated on a screen. While not OpenCV-specific, this technique can be used to provide visualizations of attention patterns of the person.

**2. Pupil Tracking:** Pupil tracking is a common technique for assessing focus and attention. OpenCV can be used to detect and track the position of the pupil in the eye, which can provide insights into a person's focus based on the direction of their gaze.

**3. Eye Aspect Ratio (EAR):** The EAR is a measure of eye openness and can be used to detect blinks and assess alertness. In the proposed model, we use this ratio to detect the blinks and keep a check on how many times a person has blinked during the session.

**4. Deep Learning Models:** Deep learning models, particularly convolutional neural networks (CNNs) and recurrent neural networks (RNNs), have been used to analyse facial expressions, eye movements, and other factors to predict attention and focus.

**1.2) Proposed Model:**

Incorporating elements from the existing models mentioned earlier, our comprehensive approach aims to generate a detailed report at the end of each user-selected session duration. By amalgamating OpenCV and Machine Learning in the initial prototype, we intend to accurately identify instances when the user experiences distractions or lacks focus. The ultimate goal is to develop an interactive application, potentially in the form of a mobile or web app, that embodies these functionalities seamlessly.

**1.3) Aim & Objectives:**

1. **Real-Time Attention Monitoring:** Develop a real-time attention monitoring system that tracks and assesses a person's level of attention and focus while working or studying on a computer.
2. **User-Friendly Assistant:** Create a user-friendly AI assistant that seamlessly integrates into a person's workflow without causing distractions or interruptions.
3. **Early Warning System** : Develop an early warning system that alerts users when their attention starts to wane, helping them take proactive measures to regain focus and productivity.
4. **Detailed Reports** : Generate detailed reports and insights on attention patterns, including the duration of focused work, distractions, and periods of reduced attention.
5. **Customizable Settings** : Allow users to customize the system's sensitivity and alert thresholds to match individual preferences and needs.
6. **Privacy and Ethics** : Ensure strict adherence to privacy and ethical guidelines, respecting user data and anonymity while collecting attention-related information.

**1.4) Scope:**

The existing models are only directed towards the attention of students during classroom sessions or eLearning. We aim to develop a system that can be used by every individual working on a computer.

EngageWise can be used by students studying for their semester examinations, working professionals completing their tasks, teachers grading the students' assignments, gamers who want to track their level of immersion and attention during gaming sessions and so on.

# **LITERATURE SURVEY**

With EngageWise, we aim to develop a personal assistant that alerts the user when there are signs of drowsiness and decreased attention levels. One can seldom find an exact implementation of EngageWise; the probability is nearly negligible. However, it is a compilation of many computer vision tasks put in one place.

We started this journey considering the driver drowsiness or alert systems as our predecessors, as the principle behind EngageWise and these existing systems overlap a little. While the complete survey can be found in our paper, here is the summary:

**Summary**

EngageWise is developed as a personal assistant for detecting drowsiness and decreased attention levels. Drawing inspiration from various research papers, the system combines elements of facial behaviour analysis and non-verbal cues to assess attentiveness. Notable influences include research on student attention assessment in classrooms, attentiveness in eLearning, and driver drowsiness detection techniques. EngageWise's methodology incorporates features like blink frequency and yawn count, similar to the techniques employed in these papers. While its primary focus is on personal attention monitoring, EngageWise shares common functionalities with driver drowsiness detection systems, such as assessing facial features and head position for signs of drowsiness.

# **DESIGN**

**3.1) Hardware Requirements:**

The success of real-time computer vision applications, such as facial landmark detection and distance estimation, often hinges on the capabilities of the underlying hardware. For the Python-based facial analysis code snippet under consideration, the hardware requirements are notably influenced by the need for efficient image processing.

- Multicore Processor
- RAM – 4 GB RAM recommended
- Web Cam for capturing real time video (720p resolution)
- An integrated Graphical Processing Unit for better video feed and output (GPU)

**3.2)**  **Software Requirements:**

- **Anaconda Navigator** : Anaconda Navigator was instrumental in managing and organizing the diverse Python libraries and dependencies required for our project, ensuring smooth compatibility and efficient package management.
- **VS Code:** Visual Studio Code (VS Code) served as our primary integrated development environment (IDE), offering a user-friendly interface and a wide range of extensions for Python development, greatly enhancing our coding and debugging efficiency.
- **Python:** Python, as the core programming language, formed the backbone of our project, providing versatile libraries for computer vision, machine learning, and real-time data processing.
- **Web Browser** : Web browsers were essential for testing and deploying our project. They enabled us to develop the web-based interface for our application and conduct real-time testing and monitoring.
- **HTML, CSS, and JS:** These web technologies played a pivotal role in creating an interactive and visually appealing user interface for our project, enhancing the user experience and accessibility.
- **Flask** : Flask, a micro web framework for Python, facilitated the development of our web application, enabling seamless integration of our machine learning models and real-time monitoring capabilities.

**3.3)**  **Model Architecture:**

Our model captures the real-time video through the user's webcam, calculates how far the user is from the camera, keeps a track of the blink frequency and yawn count, therefore display an alert that the user is drowsy if they blink multiple times.

The flowchart below clearly explains all the events starting from the user initiating the session to ending the session.


**3.4) Algorithms**

- **Haar Cascade Classifier** : Although it's not explicitly mentioned in the code, the cv2.VideoCapture and dlib.get\_frontal\_face\_detector functions often use Haar Cascade Classifiers for face detection. Haar Cascades are a machine learning object detection method used to identify objects in images or video.
- **Facial Landmark Detection (dlib)**: The code utilizes dlib's facial landmark detection model. While not named in the code, dlib uses a combination of shape predictors and trained models to locate specific facial landmarks (such as eyes, nose, mouth, etc.) on detected faces.
- **Eye Aspect Ratio (EAR)**: The EAR is a blink detection technique. It calculates the ratio of distances between specific points on the eye, typically using the landmarks of the left and right eyes. If this ratio falls below a threshold, a blink is detected.
- **Mouth Aspect Ratio (MAR)**: The MAR is used for yawn detection. It computes the ratio of the vertical distance between the upper and lower lip to the horizontal distance between the corners of the mouth. A yawn is detected if this ratio exceeds a threshold.
- **Gaussian Blur** : cv2.GaussianBlur is applied to the video frames. Gaussian blurring is a technique for reducing noise and detail in an image, which can improve the accuracy of facial feature detection.

**3.5) Libraries**

- **openCV:** OpenCV is a popular computer vision library used for capturing video frames, image manipulation, and various computer vision operations
- **Scipy:** The Scipy library built on Numpy, is used to perform complex scientific and mathematical peroblems,In our model, we used scipy to calculate distance between the points
- **cvzone:** Cvzone is a library used for facial detection. It has utilities like FaceDetector and FaceMesDetector
- **imutils:** The imutils library provides a number of convenience functions to carry out image processing and computer vision tasks. In our model, we used imutils to resize the video frames and obtain the landmarks of the mouth
- **dlib:** The dlib library is used for a number of reasons.We used dlib to utilize the facial shape predictor to detect the landmarks on the face
- **collections:** The collections library is imported to utilize the OrderedDict to store the facial landmark indices in the form of a dictionary

# **IMPLEMENTATION**

In this section, we present the implementation details of the Blink and Yawn Detection System using Computer Vision and Facial Landmarks. The system leverages various computer vision techniques and libraries to perform real-time detection of blink and yawn events.

**4.1) Facial Landmark Detection**

The system relies on facial landmarks to track the movements of eyes and the mouth. The facial landmarks are detected using the dlib library, which provides a pre-trained shape predictor model ("shape\_predictor\_68\_face\_landmarks.dat"). These landmarks are used to calculate various metrics related to eye and mouth movement.

The key landmarks used in the system include:

- Mouth landmarks (Indexes 48 to 68)
- Right eyebrow landmarks (Indexes 17 to 22)
- Left eyebrow landmarks (Indexes 22 to 27)
- Right eye landmarks (Indexes 36 to 42)
- Left eye landmarks (Indexes 42 to 48)
- Nose landmarks (Indexes 27 to 35)
- Jaw landmarks (Indexes 0 to 17)

**4.2) Blink Detection**

Blink detection is performed by measuring the Eye Aspect Ratio (EAR). The EAR is calculated using the Euclidean distances between key points of the left and right eyes. If the EAR falls below a predefined threshold (EAR\_THRESHOLD), it is considered as a blink event. The system keeps track of the blink count.

**4.3) Yawn Detection**

Yawn detection is based on the Mouth Aspect Ratio (MAR). The MAR is calculated by measuring the ratio of the vertical distance between the upper and lower lip to the horizontal distance between the corners of the mouth. If the MAR exceeds a predefined threshold (MAR\_THRESHOLD), it is detected as a yawn event. The system maintains a count of yawn events.

**4.4) Distance Estimation**

The system also incorporates distance estimation functionality using face detection. It utilizes the dlib face detector to identify faces in the video stream. The width of the detected face is used to estimate the distance from the camera, considering the known width of an average human face.


**4.5) Alarm System**

The system includes an alarm feature designed to activate when the individual exhibits signs of drowsiness for an extended duration, typically surpassing 10 seconds. This function aims to assist the user in promptly reawakening from potential moments of fatigue, enabling them to refocus and maintain productivity in their tasks.

**4.6) User Interaction**

The system provides a user interface for capturing images by pressing the 'c' key. Captured images are saved with incremental filenames (e.g., "image1.png"). The 'q' key is used to exit the program.

**4.7) Real-time Visualization**

The processed video frames are displayed in real-time using OpenCV's 'imshow' function. Various textual information, such as blink count, yawn count, and drowsiness status, is overlaid on the video feed to provide real-time feedback to the user.

**4.8) Execution and Termination**

The system continuously captures frames from the camera feed, processes them for blink and yawn detection, and displays the results. The program can be terminated by pressing the 'q' key. Upon termination, the camera is released, and all OpenCV windows are closed.

# **Conclusion:**

EngageWise is a sophisticated focus detection application designed to assess the attention span of individuals, including students preparing for exams, working professionals, and teachers. Leveraging advanced computer vision techniques and facial feature analysis, the application provides real-time insights into the user's level of attentiveness.

The system employs a combination of facial landmark detection, blink, and yawn analysis to gauge the user's focus during study or work sessions. By monitoring the Eye Aspect Ratio (EAR) for blink detection and the Mouth Aspect Ratio (MAR) for yawn detection, EngageWise can effectively identify signs of drowsiness or reduced attention.

# **Future Enhancements:**

EngageWise is not entirely accurate as this is the first phase. We definitely look forward to enhance the model by fine tuning the parameters, adding a few functionalities to make it more engaging, incorporate user feedback mechanism and prioritize security and privacy of the users.

# **REFERENCES**

[1] Raca, Mirko. (2015). Camera-based Estimation of Student's Attention in Class.

[2] Qingshan Deng and Zhili Wu 2018 _IOP Conf. Ser.: Earth Environ. Sci._ 199032042

[3] Pooja Koshti(2022) AttenQ- Attention Span Detection Tool for Online Learning

[4] Chakraborty, Partha & Yousuf, Mohammad & Zahid, Zahidur & Faruqui, Nuruzzaman. (2020). How Can a Robot Calculate the Level of Visual Focus of Human's Attention. 10.1007/978-981-15-3607-6\_27.

[5] Kumar, N., & Barwar, D.N. (2014). Detection of Eye Blinking and Yawning for Monitoring Driver' s Drowsiness in Real Time.

[6] Maganti Manasa, Vikas B, K. Subhadra (2019). Drowsiness detection using Eye-Blink frequency and Yawn count for Driver Alert.

[7] Ling Gan, Bing Cui and Weixing Wang, "Driver Fatigue Detection Based on Eye Tracking," 2006 6th World Congress on Intelligent Control and Automation, Dalian, China, 2006, pp. 5341-5344, doi: 10.1109/WCICA.2006.1714090.

[8] Vandna and Rekha Saini. "Driver Drowsiness Detection System and Techniques: A Review." (2014).

[9] M. Ramzan, H. U. Khan, S. M. Awan, A. Ismail, M. Ilyas and A. Mahmood, "A Survey on State-of-the-Art Drowsiness Detection Techniques," in IEEE Access, vol. 7, pp. 61904-61919, 2019, doi: 10.1109/ACCESS.2019.2914373.

[10] S. Sathasivam, A. K. Mahamad, S. Saon, A. Sidek, M. M. Som and H. A. Ameen, "Drowsiness Detection System using Eye Aspect Ratio Technique," 2020 IEEE Student Conference on Research and Development (SCOReD), Batu Pahat, Malaysia, 2020, pp. 448-452, doi: 10.1109/SCOReD50371.2020.9251035.

[11] B. Alshaqaqi, A. S. Baquhaizel, M. E. Amine Ouis, M. Boumehed, A. Ouamri and M. Keche, "Driver drowsiness detection system," 2013 8th International Workshop on Systems, Signal Processing and their Applications (WoSSPA), Algiers, Algeria, 2013, pp. 151-155, doi: 10.1109/WoSSPA.2013.6602353.

[12] L. Thulasimani; Poojeevan P; Prithashasni S P. "Real Time Driver Drowsiness Detection Using Opencv and Facial Landmarks". Int. J. of Aquatic Science, 12, 2, 2021, 4297-4314.

[13] R. Vishnu et al 2021 J. Phys.: Conf. Ser. 1916 012172 "Driver drowsiness detection system with opencv and keras"

DOI 10.1088/1742-6596/1916/1/012172

[14] Y. Suryawanshi and S. Agrawal, "Driver Drowsiness Detection System based on LBP and Haar Algorithm," 2020 Fourth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC), Palladam, India, 2020, pp. 778-783, doi: 10.1109/I-SMAC49090.2020.9243347.

[15] P. P. Patel, C. L. Pavesha, S. S. Sabat and S. S. More, "Deep Learning based Driver Drowsiness Detection," 2022 International Conference on Applied Artificial Intelligence and Computing (ICAAIC), Salem, India, 2022, pp. 380-386, doi: 10.1109/ICAAIC53929.2022.9793253.

[16] Mohanty, Archit, and Saurabh Bilgaiyan. "Drowsiness detection system using KNN and OpenCV." Machine Learning and Information Processing: Proceedings of ICMLIP 2020. Springer Singapore, 2021.

[17] Neelanjan. (n.d.). GitHub - neelanjan00/Driver-Drowsiness-Detection: https://github.com/neelanjan00/Driver-Drowsiness-Detection

[18] Misbah. (n.d.). GitHub - misbah4064/drowsinessDetector: OpenCV Drowsiness Detector using Python and Dlib. GitHub. https://github.com/misbah4064/drowsinessDetector

[19] Steflayanto. (n.d.). GitHub - steflayanto/nwHacks-2020-Back-End. GitHub. https://github.com/steflayanto/nwHacks-2020-Back-End

[20] Zhermin. (n.d.). GitHub - zhermin/ripplecreate-attention-model: Attention Indexing Computer Vision POC for ripplecreate. GitHub. https://github.com/zhermin/ripplecreate-attention-model
