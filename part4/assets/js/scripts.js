document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            try {
                await loginUser(email, password);
            } catch (error) {
                console.log('error:' + error)
            }
        });
    }
});

//AJAX request to the API
async function loginUser(email, password) {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password }),
    });

    //Handle the API response
    if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
        console.log(`${data.access_token}`)
    } else {
        alert('Login failed: ' + response.statusText);
    }
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

function getCookie(name) {
    const cookieValue = document.cookie.split("; ")
        .find((row) => row.startsWith(name))
        ?.split("=")[1];
    return cookieValue
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        const places = await response.json();
        displayPlaces(places);
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    const priceFilter = document.getElementById('price-filter');

    function placesDisplay(list) {
        placesList.innerHTML = '';
        list.forEach(place => {        
            const placeCard = document.createElement('div');
            placeCard.className = 'place-card';
            placeCard.innerHTML = `
                <img src="assets/images/ecolodge.avif" alt="git">
                <h2>${place.title}</h2>
                <p>Price €${place.price}</p>
                <button class="detail-button">View details</button>
            `;
            placesList.appendChild(placeCard);
        });
    }

    placesDisplay(places);

    priceFilter.addEventListener('change', (event) => {
        const selectedPrice = parseFloat(event.target.value);
        const filteredPlaces = places.filter(place => place.price <= selectedPrice);
        placesDisplay(filteredPlaces);
    });
}
