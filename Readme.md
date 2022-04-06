# ***Une toute petite application en flask, dans un conteneur et tournant sur Azur***

>### Créer et sauvegarder le modèle
>
> à faire en premier 

```console 
python CreateModel.py
```

>#### Faire tourner en local 
```console
pip install -r requirements.txt
python app.py
```

>#### Construction de l'image docker
```console 
docker build -f Dockerfile -t <pseudo>/<nom de l'app>:<version (latest)> .
```

>##### Tester le conteneur en local 
```console
docker run -p 5000:5000 --rm <pseudo>/<nom de l'app>:<version (latest)>
```

>#### Pusher le conteneur sur dockerhub 
```console
docker login 
docker push <pseudo>/<nom de l'app>:<version (latest)>
```
>## Azure container instance 

1. Créer une nouvelle ressource **Azur Container Instance** ou **Instance de conteneur**
2. Choisir le groupe de ressource
3. Choisir *autre registre* ```<pseudo>/<nom de l'app>:<version (latest)>```
4. Choisir beaucoup de RAM (10Gb) car l'application et les dépendance ne sont pas du tout optimisé
5. Suivant éditer le port ```5000 TCP```
6. Vérifier et créer --> Créer 

Une fois déployé vous voyez l'adresse IP en haut à droite 
pour accéder à l'application il suffit d'aller à la bonne adresse, par exemple: 
```http://20.199.58.133:5000/```