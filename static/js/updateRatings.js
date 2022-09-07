editButtons = document.querySelectorAll('.edit-climbing-route-rating');

for (const button of editButtons) {
  button.addEventListener('click', () => {
    // first ask the user what they want the new rating to be
    const newScore = prompt('What is your new star rating for this climb?');
    const formInputs = {
      updated_score: newScore,
      rating_id: button.id,
    };

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
}