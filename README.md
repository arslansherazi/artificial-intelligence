# Artificial Intelligence
## Machine Learning (Supervised)
### Bias
Difference between actual results and machine predicted results

### Variance
Difference between predicted results

### Problems of Classification
* #### Under fitting (High Bias-Low Variance)
neither accuracy of training is correct nor testing accuracy is correct
<br /> 
##### Solution:
1. Add more features into dataset (It lowers the bias)
2. Try different algorithm

* #### Over fitting (Low Bias-High Variance)
1. accuracy of training is correct but accuracy of testing is not correct
2. model reads noise from dataset/model reads all of the points from dataset including noise
3. model just memorizes the patterns from training dataset
##### Solution:
1. Train model with more data
2. Features Engineering (reduce unnecessary features)
3. RFECV
4. Try different algorithm

### Best fit / Generalization (Our Goal)
both accuracies of training and testing are correct
#### Generalized model
 1. best fit classification algorithm
 2. classification algorithm which is neither overfit nor underfit 
