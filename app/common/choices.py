from django.db.models import TextChoices


class Status(TextChoices):
    ACTIVE = "ACTIVE", "Active"
    DRAFT = "DRAFT", "DRAFT"
    INACTIVE = "INACTIVE", "Inactive"
    REMOVED = "REMOVED", "Removed"


class BDCity(TextChoices):
    BAGERHAT = "BAGERHAT", "Bagerhat"
    BAKHTEYARPUR = "BAKHTEYARPUR", "Bakhteyarpur"
    BANDARBAN = "BANDARBAN", "Bandarban"
    BARGUNA = "BARGUNA", "Barguna"
    BARISHAL = "BARISHAL", "Barishal"
    BHOLA = "BHOLA", "Bhola"
    BOGRA = "BOGRA", "Bogra"
    CHANDPUR = "CHANDPUR", "Chandpur"
    CHAPAINAWABGANJ = "CHAPAINAWABGANJ", "Chapainawabganj"
    CHHAGALNAIYA = "CHHAGALNAIYA", "Chhagalnaiya"
    CHITTAGONG = "CHITTAGONG", "Chittagong"
    CHITTAGONG_PORT = "CHITTAGONG_PORT", "Chittagong Port"
    CHUADANGA = "CHUADANGA", "Chuadanga"
    COX_S_BAZAR = "COX_S_BAZAR", "Cox's Bazar"
    DHAKA = "DHAKA", "Dhaka"
    COMILLA = "COMILLA", "Comilla"
    FARIDPUR = "FARIDPUR", "Faridpur"
    FENI = "FENI", "Feni"
    GAZIPUR = "GAZIPUR", "Gazipur"
    GOPALGANJ = "GOPALGANJ", "Gopalganj"
    HABIGANJ = "HABIGANJ", "Habiganj"
    JESSORE = "JESSORE", "Jessore"
    JHALOKATHI = "JHALOKATHI", "Jhalokathi"
    JHENIDAH = "JHENIDAH", "Jhenidah"
    JOYPURHAT = "JOYPURHAT", "Joypurhat"
    KALIGANJ = "KALIGANJ", "Kaliganj"
    KERANIGANJ = "KERANIGANJ", "Keraniganj"
    KHAGRACHARI = "KHAGRACHARI", "Khagrachari"
    KISHOREGANJ = "KISHOREGANJ", "Kishoreganj"
    KISHORGANJ = "KISHORGANJ", "Kishorganj"
    KHULNA = "KHULNA", "Khulna"
    KUAKATA = "KUAKATA", "Kuakata"
    KURIGRAM = "KURIGRAM", "Kurigram"
    KUSHTIA = "KUSHTIA", "Kushtia"
    LAKSHMIPUR = "LAKSHMIPUR", "Lakshmipur"
    LALMONIRHAT = "LALMONIRHAT", "Lalmonirhat"
    MAGURA = "MAGURA", "Magura"
    MAULVI_BAZAR = "MAULVI_BAZAR", "Maulvi Bazar"
    MADARIPUR = "MADARIPUR", "Madaripur"
    MOHESHKHALI = "MOHESHKHALI", "Moheshkhali"
    MYMENSINGH = "MYMENSINGH", "Mymensingh"
    NARAIL = "NARAIL", "Narail"
    NARAYANGANJ = "NARAYANGANJ", "Narayanganj"
    NARSINGDI = "NARSINGDI", "Narsingdi"
    NARSHINGDI = "NARSHINGDI", "Narshingdi"
    NATORE = "NATORE", "Natore"
    NAOGAON = "NAOGAON", "Naogaon"
    NAWABGANJ = "NAWABGANJ", "Nawabganj"
    NILPHAMARI = "NILPHAMARI", "Nilphamari"
    PATUAKHALI = "PATUAKHALI", "Patuakhali"
    PABNA = "PABNA", "Pabna"
    PAIKGACHHA = "PAIKGACHHA", "Paikgachha"
    PANCHAGARH = "PANCHAGARH", "Panchagarh"
    PARBATIPUR = "PARBATIPUR", "Parbatipur"
    PUTHIA = "PUTHIA", "Puthia"
    RAJBARI = "RAJBARI", "Rajbari"
    RAIPUR = "RAIPUR", "Raipur"
    RAJSHAHI = "RAJSHAHI", "Rajshahi"
    RANGPUR = "RANGPUR", "Rangpur"
    SARISHA = "SARISHA", "Sarisha"
    SATKHIRA = "SATKHIRA", "Satkhira"
    SABAIL = "SABAIL", "Sabail"
    SANDWIP = "SANDWIP", "Sandwip"
    SHARANKHALI = "SHARANKHALI", "Sharankhali"
    SHYAMNAGAR = "SHYAMNAGAR", "Shyamnagar"
    SIRAJGANJ = "SIRAJGANJ", "Sirajganj"
    SITAKUNDA = "SITAKUNDA", "Sitakunda"
    SUNAMGANJ = "SUNAMGANJ", "Sunamganj"
    SYLHET = "SYLHET", "Sylhet"
    TANGAIL = "TANGAIL", "Tangail"
    THAKURGAON = "THAKURGAON", "Thakurgaon"
    TUNGIPARA = "TUNGIPARA", "Tungipara"
    ULLAHPARA = "ULLAHPARA", "Ullahpara"
    UNKNOWN = "UNKNOWN", "Unknown"
