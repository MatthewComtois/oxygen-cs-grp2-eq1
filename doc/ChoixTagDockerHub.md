# Justification des tags DockerHub

Les tags de Docker permettent de créer et de facilement identifier les images. Les tags de Docker sont utilisés comme identifiant.
Voici nos choix de tags et la justification de leur utilisation :

1. **latest** : Ce tag permet de facilement identifier quelle image est la plus récente. Il y a toujours une seule image avec 
le tag "latest".
2. **Numéro(Github Build Number)** : Le deuxième tag est un numéro correspondant au numéro du build de github lorsque l'image a
été créée. Ceci permet de garder une copie des anciennes images. À chaque fois qu'un build est fait et que le build correspond à
un push dans la branche main, une nouvelle image sera créée avec le numéro du build en tant que tag. 