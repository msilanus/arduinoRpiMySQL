# Structure d'un objet communicant avec Arduino Raspberry pi et MysQL #

Mis en oeuvre d'une structure type d'objet communicant basé sur l'utilisation d'une carte Arduino pour la partie acquisition/actionneurs et d'une carte PC embarqué (pcDuino, Raspberry Pi, ...) pour la partie traitement (script Python, programme C/C++, ...), connexion au réseau (filaire ou wifi), stockage local des données (serveur de bases de données SQLigth, MySQL, ...), mise à disposition des données (serveur web Apache2, lighttpd, ginx, ...). 

La connexion entre ces deux carte se fait naturellement par une liaison série sur USB. Le synoptique ci-dessous représente par exemple un système de surveillance de la hauteur et de la qualité de l'eau d'un cours d'eau. La température, le Ph et la hauteur de l'eau sont mesurés sur demande par la carte Arduino. Le pcDuino via un scritp Python dont l'exécution peut être planifiée avec Cron, effectue la demande puis lit les réponses et les stockent dans la base de données MySQL. Apache2, via une page web php, met à disposition des utilisateurs les informations.

![](http://silanus.fr/sin/wp-content/uploads/2017/02/arduino-PC_Duino.png)

Tutoriel complet : [http://silanus.fr/sin/?p=837](http://silanus.fr/sin/?p=837)