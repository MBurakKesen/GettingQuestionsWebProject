// Dinamik bir veri listesi
const soruCevaplari = new Map();
let skor=0;

function dogrula(cevap,dogruCevap){
      if(cevap===dogruCevap){
        skor++;
        console.log(skor);
      }
      else{
        skor--
        console.log(skor);
      }
}

function show(){
  if(skor<0){
    skor=0;
    alert("Puanınız: " + skor);
  }
}