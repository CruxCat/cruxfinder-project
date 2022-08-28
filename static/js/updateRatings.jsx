function EditRating(props) {
    const [currentRating, setCurrentRating] = React.useState(props.initialRating);
    return (
      <div>
        <div>{currentRating}</div>
        <button type="button" onClick={() => setCurrentRating(currentRating + 1)}>
          Click to edit your star rating.
        </button>
      </div>
    )
  }
  ReactDOM.render(<EditRating/>, document.querySelector('#button-container'));