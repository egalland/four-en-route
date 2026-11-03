# Four en route
Application française de minuteurs indépendants. Source TypeScript sans dépendances ; sortie statique dans dist.

## Compiler
Node 24 :
```sh
node -e "const fs=require('fs');fs.writeFileSync('dist/app.js',require('module').stripTypeScriptTypes(fs.readFileSync('app.ts','utf8')));"
node --check dist/app.js
```

## Données
Minuteurs sauvegardés dans localStorage (four-en-route-v1) dans ce navigateur, sur cet appareil. Pas de serveur de données ni synchronisation entre appareils. L'effacement des données du navigateur efface les minuteurs. Les échéances sont absolues et restaurées après actualisation. Le son nécessite une activation à chaque session. Aucune alerte garantie quand la page est fermée ou l'appareil en veille.

## Vérification manuelle
Création d'un minuteur nommé ; seconde cuisson indépendante ; pause de la première ; actualisation : pause conservée et seconde cuisson toujours active. Nom vide refusé. Portions nulles refusées. Calcul : 250 g pour 4 vers 6 portions = 375 g. Durées suggérées indicatives, aucun minuteur préchargé.
