# One Time Pad Cipher using int32 or string seed as key

### Anetaret e grupit: Roni Kukaj, Suhejl Vejseli, Rron Sherifi
### Gjuha programuese: Python

**Pershkrim:**
>Algoritmi One Time Pad eshte algoritem i cili perdor nga nje celes te vecante
 per cdo komunikim ne mes te paleve. Celesin e dijne vetem palet komunikuese dhe 
celesi duhet te jete me gjatesi te njejte sa mesazhi qe te kryhet enkriptimi/dekriptimi.

Enkriptimi behet duke kryer XOR ne mes te celesit dhe mesazhit, duke krijuar ciphertextin,
kurse dekriptimi behet duke kryer XOR mes ciphertextit dhe celesit per te mberritur ne plaintext.

One Time Pad ofron siguri maksimale sepse eshte e pamundur te dihet celesi kur cdo here
nderron me cdo komunikim dhe nuk ka ndonje strukture me ane te se ciles gjendet mesazhi plain.

*Gjithsesi, ky algoritem ka pengesat e veta qe nuk e bejne efikas ne perdorim large-scale 
sepse duhet zgjidhur problemi i shperndarjes se celesave ne mes te paleve komunikuese per cdo komunikim te tyre.*


Implementimin e algoritmit e kemi bere duke perdorur Python OOP, ne nje file kemi shkruar klasat baze
qe kryejne funksionet e nevojshme gjate enkriptimit/dekriptimit.
Ne dy file tjera kemi thirrur funksionalitet per encryption dhe decryption.
Ndersa ne file te fundit kemi perdorur nje librari per GUI te python qe te vizualizojme punen e ketij
algoritmi dhe ta bejme me te lehte per prezentim.

Per GUI kemi perdorur librarine e Python, PyQt5 e cila me ane te Programimit te Orientuar ne Objekte na ka mundesuar qe te dizajnojme pjesen FrontEnd te projektit tone. 
Kemi perdorur dy tabs, nje per encryption dhe nje tjeter per decryption, te cilar kryejne funksionet perkatese.