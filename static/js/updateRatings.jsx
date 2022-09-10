// component
function EditRating() {

  function handleClick() {
   
    fetch('/update_rating', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
      }).then((response) => {
        if (response.ok) {
          document.querySelector(`#rating1`).innerText = newScore;
        } else {
          alert('Failed to update rating.');
      }
    });
  }

  return (
    <button type="button" onClick={handleClick}>
      EDIT RATING
    </button>
  );
}
ReactDOM.render(<EditRating/>, document.querySelector('#button-container'));