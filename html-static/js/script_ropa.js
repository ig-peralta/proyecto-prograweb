fetch('http://fakestoreapi.com/products')
  .then(response => response.json())
  .then(data => {
    const cardContainer = document.getElementById('card-container');
    data.forEach(item => {
      const card = document.createElement('div');
      card.classList.add('col-md-4', 'mb-4');
      card.innerHTML = `
        <div class="card p-3" style="height:45vh;">
          <img src="${item.image}" class="card-img-top ms-auto me-auto mb-2" alt="${item.title}" style="height:20vh; width:20vh; object-fit: contain;">
          <a href="#" class="text-reset text-decoration-none"><h5 class="card-title">${item.title}</h5></a>
          <p style="overflow: hidden; text-overflow: ellipsis; width: 100%;">${item.description}</p>
        </div>`;
      cardContainer.appendChild(card);
      });
    })
  .catch(error => console.error('Error obteniendo data:', error));