
# Gözetimsiz Öğrenme ile Müşteri Segmentasyonu
# (Customer Segmentation with Unsupervised Learning)


### Veri Seti Hikayesi

Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline) olarak yapan müşterilerin geçmiş alışveriş davranışlarından elde edilen bilgilerden oluşmaktadır.

Online ayakkabı mağazası olan FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor. Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranışlardaki öbeklenmelere göre gruplar oluşturulacak

Unsupervised Learning yöntemleriyle (Kmeans, Hierarchical Clustering )  müşteriler kümelere ayrılıp ve davranışları gözlemlenmek istenmektedir.


  *  19.945 gözlem, 12 değişken

1) master_id: Eşsiz müşteri numarası
2) order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
3) last_order_channel : En son alışverişin yapıldığı kanal
4) first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
5) last_order_date : Müşterinin yaptığı son alışveriş tarihi
6) last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
7) last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
8) order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
9) order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
10) customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
11) customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
12) interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


###### Hedefler:

Biraz veri keşif analizinden sonra iki farklı kümeleme algoritması uygulayacağım ve sonuçları görselleştireceğim:

* Scikit-learn K-Means kümelemesini kullanın ve
* Scikit-learn Hiyerarşik kümelemeyi kullanın ve kümelenmeyi görselleştirmek için dendogramlar oluşturun



Segmentasyona ayırmak ne kazandırır peki;

* Satışlarınızı/gelirinizi arttırmanıza yardımcı olur
* Pazarlama yönteminizi geliştirmenize yardımcı olur
* Müşterinizi elde tutma oranınız artar. Diğer bir ifade ile müşterilerinizin churn(terk etme) oranı düşer

