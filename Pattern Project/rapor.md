Forensics Investigation from Fingerprint Microbes
1. Project Objectives
**This project focuses on the discovery that DNA samples from human fingerprints are unique, allowing the identification
of individuals using computer keyboards. Specifically, the goal is to determine which hand (left or right) an individual 
used to touch the computer keyboard.

2. Dataset
**The dataset comprises 271 samples, with 136 being left-hand samples and 135 being right-hand samples. Each sample 
contains 3302 features. The dataset is provided in either "otu1.xlsx" format.

3. Used Algorithm
**In this project, the Gaussian Naive Bayes classification algorithm has been employed. This algorithm is preferred for 
classifying left and right-hand data based on the features in the dataset.

4. Applied Procedures
**The dataset was read from the "otu1.xlsx" file, and the left/right labels were converted to 0 and 1.
**The dataset was split into features and target variables.
**Training and test datasets were created, with the test dataset containing 30% of the data.
**The Gaussian Naive Bayes model was trained, and its performance was evaluated through cross-validation.
**Model performance was assessed using Accuracy, Confusion Matrix, Sensitivity, and Specificity metrics.

5. Performance Metrics
**Accuracy: The model's accuracy rate is obtained as %x.
**Confusion Matrix: The model's classification results are as follows:

                           Predicted:Left Hand (0)	                Predicted: Right Hand (1)
Actual: Left Hand (0)	          XX	                                        XX
Actual: Right Hand (1)            XX	                                        XX
**Sensitivity and Specificity: Classification success rates for left and right hands were calculated.

6. Results and Evaluation
**The Gaussian Naive Bayes algorithm used in the project successfully classified left and right-hand data based on the 
features in the dataset. However, the absence of a feature selection step resulted in the model being trained using all 
features. In future work, enhancing the model's performance can be considered by incorporating feature selection methods.

