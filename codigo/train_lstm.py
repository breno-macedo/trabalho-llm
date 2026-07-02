#!/usr/bin/env python3
import os, json, pickle, numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"; os.environ["PYTHONHASHSEED"]="42"
import random; random.seed(42); np.random.seed(42)
import tensorflow as tf; tf.random.set_seed(42)
from sklearn.metrics import (classification_report, confusion_matrix,
    accuracy_score, precision_recall_fscore_support)

A="/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"
d=np.load(A+"/data.npz"); meta=pickle.load(open(A+"/meta.pkl","rb"))
classes=meta["classes"]; F=d["X_tr"].shape[1]
Xtr=d["X_tr"].reshape(-1,1,F); Xte=d["X_te"].reshape(-1,1,F)
ytr=d["y_tr"]; yte=d["y_te"]

model=tf.keras.Sequential([
    tf.keras.layers.Input((1,F)),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(len(classes), activation="softmax")])
model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy", metrics=["accuracy"])
hist=model.fit(Xtr,ytr,epochs=30,batch_size=64,verbose=0,validation_split=0.1)

prob=model.predict(Xte,verbose=0); yp=prob.argmax(1)
acc=accuracy_score(yte,yp)
P,R,Fs,_=precision_recall_fscore_support(yte,yp,labels=range(len(classes)),zero_division=0)
mp,mr,mf,_=precision_recall_fscore_support(yte,yp,average="macro",zero_division=0)
cm=confusion_matrix(yte,yp,labels=range(len(classes)))
perclass={classes[i]:{"precision":float(P[i]),"recall":float(R[i]),"f1":float(Fs[i])}
          for i in range(len(classes))}
out={"model":"LSTM","accuracy":float(acc),
     "macro_precision":float(mp),"macro_recall":float(mr),"macro_f1":float(mf),
     "per_class":perclass,"confusion_matrix":cm.tolist(),"classes":classes,
     "loss_curve":[float(x) for x in hist.history["loss"]],
     "val_loss":[float(x) for x in hist.history["val_loss"]],
     "acc_curve":[float(x) for x in hist.history["accuracy"]],
     "val_acc":[float(x) for x in hist.history["val_accuracy"]]}
json.dump(out, open(A+"/lstm_results.json","w"), indent=2, ensure_ascii=False)
model.save(A+"/lstm_model.keras")
np.save(A+"/lstm_prob.npy", prob)
print("LSTM acc=%.4f macroF1=%.4f"%(acc,mf))
for c in classes: print("  %-15s P=%.3f R=%.3f F1=%.3f"%(c,perclass[c]["precision"],perclass[c]["recall"],perclass[c]["f1"]))
print("OK lstm")
