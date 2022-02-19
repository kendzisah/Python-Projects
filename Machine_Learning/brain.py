from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(
    execution_path, "DenseNet-BC-121-32.h5"))
prediction.loadModel()


predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "white_guy.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
