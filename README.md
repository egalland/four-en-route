# Four en route

Application française de minuteurs de cuisson indépendants, avec cuisine animée et calcul de proportions.

- Application : https://egalland.github.io/four-en-route/
- Statistiques : https://egalland.github.io/four-en-route/stats.html

## Utiliser

Nommez un plat, indiquez une durée positive et lancez la cuisson. Chaque minuteur a ses propres commandes de pause, reprise, ajout d'une minute, remise à zéro et suppression. Jusqu'à 30 minuteurs. Les animations peuvent être mises en pause et respectent `prefers-reduced-motion`.

Proportions : 250 g pour 4 personnes, adaptés à 6 personnes = 250 × 6 ÷ 4 = 375 g. Arrondi des g/ml au dixième le plus proche ; pièces à l'entier supérieur. Portions entières strictement positives.

## Développer

Source TypeScript dans `src/app.ts`, fichiers publiés dans `docs/`. Aucune dépendance à installer. Node 24.3+ et Python 3 :

```sh
node scripts/build.mjs
node --check docs/app.js
python3 scripts/stats.py
python3 -m http.server 8000 --directory docs
```

Le retrait des types avec Node ne remplace pas une vérification statique TypeScript. GitHub Pages est configuré sur `main`, dossier `/docs`.

## Données et limites

Les minuteurs sont sauvegardés dans `localStorage`, dans ce navigateur et sur cet appareil. Leurs échéances absolues sont restaurées après actualisation. Pas de serveur de données, ni de synchronisation entre appareils. Effacer les données du navigateur efface les minuteurs. Une autre origine (Sites / GitHub Pages) a une sauvegarde séparée : aucune migration automatique.

Le son doit être activé à chaque session. Aucune alerte garantie quand la page est fermée ou l'appareil en veille. Les temps suggérés sont indicatifs ; vérifier la cuisson réelle. Aucun minuteur de démonstration chargé par défaut. Les statistiques décrivent le projet, pas les cuissons des visiteurs.

## Historique

Deux versions fonctionnelles réellement produites, importées séparément sur GitHub avec leur SHA et date d'origine dans le message du commit :

1. `4737ec913c0e09bcac9738d25b90abd4c0b9118c` — 03/11/2026 06:47:31 Paris : première version utilisable.
2. `c734ae6f5c05f3dd0633288e6c961ae44c73b657` — 03/11/2026 06:57:38 Paris : cuisine animée.

L'initialisation GitHub et la publication/statistiques ajoutent des commits techniques. Les dates des imports ne sont pas présentées comme les dates de développement.

## Statistiques

`docs/stats.json` est généré par `scripts/stats.py`. Il compte les octets UTF-8 et lignes physiques des fichiers HTML, CSS et TypeScript, sans doubler le JavaScript généré. Le code est compact : le nombre de lignes est fortement dépendant du formatage.

Temps actif de vibecoding : non chronométré. Équivalent développeur estimé : 6–10 h ; valorisation hypothétique : 300–700 € à 50–70 €/h. Ces estimations ne sont ni des dépenses réelles ni des économies mesurées.

## Vérifications

Parcours testés en navigateur : création de deux cuissons indépendantes, pause, reprise, +1 minute, remise à zéro, fin de cuisson, restauration après actualisation, refus d'un nom vide, refus de portions nulles, exemple 250 g × 6 ÷ 4 = 375 g, pause des animations. Publication Pages et page statistiques vérifiées séparément.
