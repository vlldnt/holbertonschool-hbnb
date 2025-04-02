/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner tous les boutons "detail-button"
    const detailButtons = document.querySelectorAll('.detail-button');

    detailButtons.forEach(button => {
        // Ajouter un événement "mouseover" pour changer la couleur du <h2>
        button.addEventListener('mouseover', () => {
            const placeCard = button.closest('.place-card'); // Trouver la carte parente
            const title = placeCard.querySelector('h2'); // Trouver le <h2> dans la carte
            title.style.color = 'red'; // Changer la couleur du texte
        });

        // Ajouter un événement "mouseout" pour restaurer la couleur originale
        button.addEventListener('mouseout', () => {
            const placeCard = button.closest('.place-card'); // Trouver la carte parente
            const title = placeCard.querySelector('h2'); // Trouver le <h2> dans la carte
            title.style.color = ''; // Restaurer la couleur originale (défaut CSS)
        });
    });
});