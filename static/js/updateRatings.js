const editButton = document.querySelector('.edit-climbing-route-rating');

  editButton.addEventListener('click', () => {
    // first ask the user what they want the new rating to be
    const newScore = prompt('What is your new star rating for this climb?');
    const routeId = document.querySelector("#route-id").value
    const formInputs = {
      updated_score: newScore
    };

    console.log(routeId);

    // send a fetch/AJAX request to the update_rating route
    fetch('/update_rating', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if (response.ok) {
        // manipulate DOM to reflect updated rating
        document.querySelector(`#rating`).innerText = newScore;
        // document.querySelector(`#avg_rating`).innerText = newScore;
      } else {
        alert('Failed to update rating.');
      }
    });
  });
