from sklearn.preprocessing import LabelEncoder

labels = ["Cat","Dog","Dog","Cat","Bird"]
encoder = LabelEncoder().fit(labels)

print("Encoded:", encoder.transform(labels))
print("Classes:", encoder.classes_)
