// component
function EditRating() {

  function handleClick() {
   
    fetch('/update_rating')
      .then((response) => response.json())
      .then((data) => {
        alert(`The weather will be ${data.forecast}`);
      });
  }

  return (
    <button type="button" onClick={handleClick}>
      EDIT RATING
    </button>
  );
}
ReactDOM.render(<EditRating/>, document.querySelector('#button-container'));