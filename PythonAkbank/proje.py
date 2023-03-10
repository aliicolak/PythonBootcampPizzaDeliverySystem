#Bu Proje Muhammet Ali ÇOLAK Tarafından Geliştirilmiştir.
import pandas as pd
from datetime import datetime
class Pizza():# pizza class'ı oluşturuldu 
         def __init__(self,description,price):
          #pizza kullanıcıdan gelen seçimler ile oluşturuldu
          self.description = description
          self.price = price
         def GetDescription(self):
          return self.description 
         def GetPrice(self):
           return self.price  
class DecoratorSauce(Pizza):#pizza sınıfı kalıtılarak sosDekoratör class'ı oluşturuldu
  def __init__(self, pizza,SauceDescription,SaucePrice):#burda veri kullanıcıdan gelen pizza seçimi ve sos detayları
    self.pizza = pizza
    self.SauceDescription = SauceDescription
    self.SaucePrice = SaucePrice
  def getPrice(self):
    return self.SaucePrice
  def getDescription(self):
    return self.SauceDescription
#her pizza türü için bir class açmak yerine pizza classından nesneler türetildi ve maliyetten kaçınıldı
klasik=Pizza("Klasik İtalyan Pizzası, Mozarella ve yeşillik içerir.",149.99)
margarita=Pizza("Margarita Pizza,domates, mozarella, fesleğen, zeytinyağı ve tuzla yapılan Napoli pizzasıdır.",179.99)
supreme=Pizza("Supreme Pizza, pizza sosu, mozzarella peyniri, sosis, taze dilimlenmiş kırmızı ve yeşil biber, soğan, mantar içerir",190)
pepperoni=Pizza("Pepperoni Pizza, pepperoni, pepperoni sos, mozerella peyniri, mısır, yeşil zeytin ve siyah zeytin içerir.",210)
gennaro=Pizza("Gennaro Pizza,pizza sosu, mozzarella peyniri, dilimlenmiş sucuk, marine mantar, mısır ve kekik!",140)
dortPeynirli=Pizza("Dört Peynirli Pizza, 4 farklı peynir türünü içerir.",200)
barbekuTavuklu=Pizza("Barbekü Tavuklu Pizza, Mangalda pişirilmiş tavuk içerir.",180)
tonBalikli=Pizza("Ton Balıklı Pizza, Ton balığı içerir.",170)
sucukluKasarli=Pizza("Sucuklu Kaşarlı Pizza, Sucuk ve Kaşar içerir.",185)
turkUsulu=Pizza("Özel Türk Pizzası, Pastırma, Kavurma, Kaşar ve Yeşil Biber içerir.",249.99)
ucret=0
def AddtoDatabase(isim,KimlikNo,KrediKarti,KartSifre,Aciklama,Sipucret,Zaman):#siparişi veritabanına ekleyecek fonksiyon oluşturuldu
    
    #ordersDatabase=pd.read_csv("ordersDatabase.txt")
    df=pd.DataFrame(
                   {
                     'isim':[isim],
                     'KimlikNo':[KimlikNo],
                     'KrediKarti':[KrediKarti],
                     'KartSifre':[KartSifre],
                     'SiparisAciklama':[Aciklama],
                     'ucret':[Sipucret],
                     'Zaman':[Zaman]
                   }
      )
    df.to_csv('ordersDatabase.txt', mode='a', index=False, header=False) 
def main():#işlemlerin çağırıldığı main fonksiyonu yazıldı

   pizzaCesit = pd.read_csv("pizzalar.txt")#pizza türleri değişken içerisine txt dosyasından aktarıldı.
   print(pizzaCesit)#ve ekrana bastırıldı
   
   pizzaSecim=input("Pizza Seçiniz(0-9):")#kullanıcı pizza seçimini yaptı
   #kullanıcının seçimine göre siparisPizza değişkeni içerisine ilgili pizza çeşidinin nesnesi aktarıldı
   if pizzaSecim=="0":
    siparisPizza=klasik
   elif pizzaSecim=="1":
    siparisPizza=margarita
   elif pizzaSecim=="2":
    siparisPizza=supreme
   elif pizzaSecim=="3":
    siparisPizza=pepperoni
   elif pizzaSecim=="4":
    siparisPizza=gennaro
   elif pizzaSecim=="5":
    siparisPizza=dortPeynirli
   elif pizzaSecim=="6":
    siparisPizza=barbekuTavuklu
   elif pizzaSecim=="7":
    siparisPizza=tonBalikli
   elif pizzaSecim=="8":
    siparisPizza=sucukluKasarli
   elif pizzaSecim=="9":
    siparisPizza=turkUsulu
#####################################

   malzemeCesit = pd.read_csv("malzeme.txt")#Sos çeşitleri değişken içerisine alındı
   print(malzemeCesit)#ve ekrana bastırıldı
   malzemeSecim=input("Ekstra Malzeme Seçiniz(0-11):")#kullanıcıya seçim yaptırıldı
   #kullanıcının seçimine göre sos sınıfından nesneler türetildi, bu nesnelerin içerisine kullanıcının seçtiği pizzalarda aktarıldı
   if malzemeSecim=="0":
      zeytin=DecoratorSauce(siparisPizza,'Ekstra 100 gr Zeytin',12)#kullanıcının daha önce seçtiği pizza,açıklama ve fiyat
      global ucret#dışardan erişebilmek için sos ve ücret isminde iki değişken tanımlandı
      global sos
      sos=zeytin.getDescription()#sosun açıklaması sos değişkeni içerisine aktarıldı
      ucret=zeytin.getPrice()+siparisPizza.GetPrice()#pizza+sos ücreti ucret değişkeninin içerisine aktarıldı
      print("Toplam Tutar : "+ str(ucret))#toplam tutar ekrana bastırıldı
   elif malzemeSecim=="1":
       keciPeyniri=DecoratorSauce(siparisPizza,'Ekstra 100 gr Keçi Peyniri',12)
       sos=keciPeyniri.getDescription()
       ucret=keciPeyniri.getPrice()+siparisPizza.GetPrice()
       print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="2":
      et=DecoratorSauce(siparisPizza,'Ekstra 100 gr Kırmızı Et',22)
      sos=et.getDescription()
      ucret=et.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="3":
      sogan=DecoratorSauce(siparisPizza,'Ekstra 100 gr Soğan',8)
      sos=sogan.getDescription()
      ucret=sogan.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="4":
      misir=DecoratorSauce(siparisPizza,'Ekstra 100 gr Mısır',10)
      sos=misir.getDescription()
      ucret=misir.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="5":
      kasarPeyniri=DecoratorSauce(siparisPizza,'Ekstra 100 gr Kaşar Peyniri',18)
      sos=kasarPeyniri.getDescription()
      ucret=kasarPeyniri.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="6":
      sucuk=DecoratorSauce(siparisPizza,'Ekstra 100 gr Sucuk',20)
      sos=sucuk.getDescription()
      ucret=sucuk.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="7":
      yumurta=DecoratorSauce(siparisPizza,'Ekstra 2 Adet Yumurta',15)
      sos=yumurta.getDescription()
      ucret=yumurta.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="8":
      danaJambon=DecoratorSauce(siparisPizza,'Ekstra 100 gr Dana Jambon',24)
      sos=danaJambon.getDescription()
      ucret=danaJambon.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="9":
      biber=DecoratorSauce(siparisPizza,'Ekstra 100 gr Biber',8)
      sos=biber.getDescription()
      ucret=biber.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   elif malzemeSecim=="10":
      bos=DecoratorSauce(siparisPizza,'Ekstra malzeme yok',0)
      sos=bos.getDescription()
      ucret=bos.getPrice()+siparisPizza.GetPrice()
      print("Toplam Tutar : "+ str(ucret))
   else:
     print("Geçersiz seçim")
#######################################################
   isim=input("İsim Giriniz : ")
   kimlikNo=input("Kimlik No Giriniz : ")
   krediKarti=input("Kart No Giriniz : ")
   kartSifre=input("Kart Şifre Giriniz : ")
   #kullanıcıdan gerekli veriler alındı
   now = datetime.now()
   suAn = now.strftime("%Y-%m-%d %H:%M:%S")
   pizzaAciklama=siparisPizza.description +sos#veritabanına eklemek üzere kullanıcının
   #seçtiği pizzanın ve sosun açıklamaları tek bir değişken içerisine alındı
   AddtoDatabase(isim,kimlikNo,krediKarti,kartSifre,pizzaAciklama,ucret,suAn)#sipariş oluşturuldu ve veritabanına
   #eklemek için AddtoDatabase fonksiyonu çağırılıp içerisine gerekli veriler aktarıldı
   secim=input("Devam etmek için 'E' tuşuna basınız")#programı kapatmak veya devam ettirmek için kullanıcıya soruldu
   #gerekli işlemler if-else bloğu içerisinde gerçekleştirildi
   if secim=='E' or secim=='e':
     main()
   else:
     exit()
main()   