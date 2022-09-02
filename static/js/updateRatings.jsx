function EditRating() {

const [newScore = prompt('What is your new star rating for this climb?'), setNewScore] = React.useState({});
const formInputs = {
  updated_score: newScore,
  rating_id: button.id,
  };

  // use AJAX to populate React component with info from Flask server
  React.useEffect(() => {
    fetch('/api/update_rating', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => response.json())
      .then((result) => {
        setNewScore(result);
      });
  }, []);


  return (
    <div>
      <div>{currentCount}</div>
      <button type="button" onClick={() => setCurrentCount(currentCount + 1)}>
        Click me to increase the count
      </button>
    </div>
  )
}



ReactDOM.render(<EditRating/>, document.querySelector('#button-container'));