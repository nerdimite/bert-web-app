import React from "react";

class ReviewBox extends React.Component {
  state = { text: "" };

  onInputChange = event => {
    this.setState({ text: event.target.value });
  };

  onFormSubmit = event => {
    event.preventDefault();
    console.log(this.state.text);
    this.props.onFormSubmit(this.state.text);
  };

  render() {
    return (
      <div className="ui segment">
        <form className="ui form">
          <div className="field">
            <label>
              <h3 className="ui header">Write your review</h3>
            </label>
            <textarea
              type="text"
              placeholder="The movie was..."
              value={this.state.text}
              onChange={this.onInputChange}
            />
          </div>
          <button className="ui button" onClick={this.onFormSubmit}>
            Analyse Review
          </button>
        </form>
      </div>
    );
  }
}
export default ReviewBox;
