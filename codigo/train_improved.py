#!/usr/bin/env python3
"""Parte 2b: LSTM melhorado = Bi-LSTM + atencao sobre a sequencia de atributos.
Treino com checkpoint/resume (janelas de tempo). Rode varias vezes ate concluir."""
import os, json, pickle, time, numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"; os.environ["PYTHONHASHSEED"]="42"
import random; random.seed(42); np.random.seed(42)
import tensorflow as tf; tf.random.set_seed(42)
from tensorflow.keras import layers
import keras
A="/sessions/upbeat-gracious-mayer/mnt/outputs/artifacts"
TARGET=30; BUDGET=34.0

@keras.saving.register_keras_serializable()
class AttentionPool(layers.Layer):
    """Atencao aditiva: pontua cada passo, normaliza (softmax) e faz soma ponderada."""
    def build(self, s):
        self.w=self.add_weight(shape=(s[-1],1), initializer="glorot_uniform", name="w")
        self.b=self.add_weight(shape=(1,), initializer="zeros", name="b")
    def call(self, x):
        score=keras.ops.tanh(keras.ops.matmul(x,self.w)+self.b)   # (b,T,1)
        a=keras.ops.softmax(score, axis=1)                         # (b,T,1)
        return keras.ops.sum(x*a, axis=1)                          # (b,units)
d=np.load(A+"/data.npz"); meta=pickle.load(open(A+"/meta.pkl","rb"))
classes=meta["classes"]; F=d["X_tr"].shape[1]
Xtr=d["X_tr"].reshape(-1,F,1); Xte=d["X_te"].reshape(-1,F,1)
ytr=d["y_tr"]; yte=d["y_te"]
mpath=A+"/improved_model_v3.keras"; hpath=A+"/improved_hist_v3.json"

def build():
    inp=layers.Input((F,1))
    x=layers.Bidirectional(layers.LSTM(48, return_sequences=True))(inp)  # (b,T,96)
    ctx=AttentionPool()(x)                     # soma ponderada por atencao
    x=layers.Dropout(0.3)(ctx)
    x=layers.Dense(32, activation="relu")(x)
    out=layers.Dense(len(classes), activation="softmax")(x)
    m=tf.keras.Model(inp,out)
    m.compile(tf.keras.optimizers.Adam(1e-3),"sparse_categorical_crossentropy",metrics=["accuracy"])
    return m

if os.path.exists(mpath):
    model=tf.keras.models.load_model(mpath, safe_mode=False)
    hist=json.load(open(hpath))
else:
    model=build(); hist={"loss":[],"val_loss":[],"accuracy":[],"val_accuracy":[]}
done=len(hist["loss"])
print("epochs done:", done)

class Budget(tf.keras.callbacks.Callback):
    def __init__(s): s.t0=time.time()
    def on_epoch_end(s,e,logs=None):
        for k in hist: hist[k].append(float(logs[k]))
        if time.time()-s.t0>BUDGET: self_stop(s)
    def self_stop(s): s.model.stop_training=True
# bind stop properly
def on_epoch_end(self, epoch, logs=None):
    for k in hist: hist[k].append(float(logs[k]))
    if time.time()-self.t0>BUDGET: self.model.stop_training=True
Budget.on_epoch_end=on_epoch_end

if done<TARGET:
    model.fit(Xtr,ytr,epochs=TARGET-done,batch_size=64,verbose=0,
              validation_split=0.1, callbacks=[Budget()])
    model.save(mpath); json.dump(hist, open(hpath,"w"))
    done=len(hist["loss"]); print("now done:", done)

if done>=TARGET:
    from sklearn.metrics import (confusion_matrix, accuracy_score,
        precision_recall_fscore_support)
    prob=model.predict(Xte,verbose=0); yp=prob.argmax(1)
    NORMAL=classes.index("Normal Traffic")
    acc=accuracy_score(yte,yp)
    P,R,Fs,_=precision_recall_fscore_support(yte,yp,labels=range(len(classes)),zero_division=0)
    mp,mr,mf,_=precision_recall_fscore_support(yte,yp,average="macro",zero_division=0)
    cm=confusion_matrix(yte,yp,labels=range(len(classes)))
    fp=int(((yte==NORMAL)&(yp!=NORMAL)).sum()); fn=int(((yte!=NORMAL)&(yp==NORMAL)).sum())
    perclass={classes[i]:{"precision":float(P[i]),"recall":float(R[i]),"f1":float(Fs[i])} for i in range(len(classes))}
    out={"model":"BiLSTM-Attention","accuracy":float(acc),"macro_precision":float(mp),
         "macro_recall":float(mr),"macro_f1":float(mf),"per_class":perclass,
         "confusion_matrix":cm.tolist(),"classes":classes,"fp_normal":fp,"fn_normal":fn,
         "loss_curve":hist["loss"],"val_loss":hist["val_loss"]}
    json.dump(out, open(A+"/improved_results.json","w"), indent=2, ensure_ascii=False)
    np.save(A+"/improved_prob.npy", prob)
    print("IMPROVED acc=%.4f macroF1=%.4f FP=%d"%(acc,mf,fp))
    print("OK improved DONE")
else:
    print("RESUME NEEDED (done %d/%d)"%(done,TARGET))
