from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

y_true = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
y_prep = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# Confusion matrix
c_matrix = confusion_matrix(y_true, y_prep)
print("Confusion Matrix : ", c_matrix)

# Accuracy Score
a_score = accuracy_score(y_true, y_prep)
print("Accuracy Score : ", a_score)

# Recall Score
r_score = recall_score(y_true, y_prep)
print("Recall Score : ", r_score)

# Precision Score
p_score = precision_score(y_true, y_prep)
print("Precision Score : ", p_score)

# F1 Score
f1_s = f1_score(y_true, y_prep)
print("F1 Score : ", f1_s)

