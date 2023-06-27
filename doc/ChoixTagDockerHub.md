# Justification des tag DockerHub

Les tags de Docker permette de créer de facilement identifier les images. Les tags dans Docker sont utiliser comme identifiants.
Voici nos choix de tags et la justification de leur utilisation :

1. **latest** : Ce tag permet de facilement identifier qu'elle image est la plus récente. Il y a toujours une seule images avec 
le tag "latest".
2. **Numéro(Github Build Number)** : Le deuxième tag est un numéro correspondant au numéro du build de github lorsque l'image à
été créer. Ceci permet de garder une copie des anciennes images. À chaque fois qu'un build est fait et que le build correspond à
un push dans la branche main, une nouvelle image sera créer avec le numéro du build en tant que tag. 