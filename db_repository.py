import sqlite3 as sql

db=sql.connect("C:/Users/Burak's Pc/Desktop/PythonProGörev/soruBankasi.db")

imlec=db.cursor()

createTable="""CREATE TABLE IF NOT EXISTS sorular(soru,cevapA,cevapB,cevapC,cevapD,dogruCevap)"""


createSoru="""
INSERT INTO sorular VALUES
('Bir görüntüyü gri tonlamaya dönüştürmek için hangi kütüphane kullanılır?', 'Matplotlib', 'OpenCV', 'Seaborn', 'Scikit-learn', 'OpenCV'),
('Nesne algılama için kullanılan popüler bir algoritma nedir?', 'YOLO', 'K-Means', 'PCA', 'Logistic Regression', 'Regression'),
('Doğal dil işleme için kullanılan popüler bir Python kütüphanesi nedir?', 'Pandas', 'NumPy', 'NLTK', 'PyTorch', 'Pandas'),
('Kelime gömme (word embedding) oluşturmak için kullanılan model nedir?', 'BERT', 'Word2Vec', 'RNN', 'CNN', 'BERT'),
('Keras hangi yapay zeka çerçevesinin bir üst düzey API''sidir?', 'PyTorch', 'TensorFlow', 'SciPy', 'Scikit-learn', 'SciPy'),
('Veri ön işleme için kullanılan popüler bir Python kütüphanesi nedir?', 'Pandas', 'NumPy', 'Matplotlib', 'NLTK', 'Pandas');
"""


imlec.execute(createTable)


imlec.execute(createSoru)
imlec.execute("SELECT * FROM sorular")
    
dizi=imlec.fetchall()
print(dizi)
db.commit()
db.close()


def veriGetir():
    return dizi